// AdBatch Vertical 3 — v2.5 · App.tsx
// ⚠️ TRANSCRITO do editor do Google Flow em 2026-08-07 (ver README.md desta
//    pasta). A indentação foi reconstruída; identificadores, literais e
//    constantes de configuração estão fiéis ao original.
//
// ⭐⭐ AS QUATRO CONSTANTES DO TOPO SÃO AS QUE MAIS IMPORTAM PARA A DOUTRINA:
//    o modelo de imagem, o modelo de vídeo, e — dentro de `Flow.generate.video`
//    — `durationSeconds: 10`. Ver a seção "O QUE O CÓDIGO REVELA" do README.

import React, { useState, useEffect, useCallback, useRef } from 'react';
import { Flow } from 'flow-sdk';
import JSZip from 'jszip';
import { AppStage, MediaSlot, RefState, VideoVariant } from './types';
import { parseBlocks } from './utils/parser';

// Constantes de Configuração
const IMAGE_MODEL = '🍌 Nano Banana 2';
const VIDEO_MODEL = 'Omni Flash';
const VALID_IMAGE_MODELS = ['🍌 Nano Banana Pro', '🍌 Nano Banana 2', '🍌 Nano Banana 2 Lite'];
const VALID_VIDEO_MODELS = ['Omni Flash', 'Veo 3.1 - Lite', 'Veo 3.1 - Fast', 'Veo 3.1 - Quality'];

const createInitialVariants = (): VideoVariant[] =>
  Array.from({ length: 4 }, () => ({ status: 'idle' }));

export default function AdBatchApp() {
  const [stage, setStage] = useState<AppStage>('images');
  const [scriptText, setScriptText] = useState('');
  const [ref, setRef] = useState<RefState>({ status: 'idle' });
  const [slots, setSlots] = useState<MediaSlot[]>(
    Array.from({ length: 3 }, (_, i) => ({
      index: i + 1,
      imageStatus: 'idle',
      variants: createInitialVariants(),
      chosenIndex: null,
      imagePrompt: { promptFromScript: '', prompt: '', promptDirty: false },
      videoPrompt: { promptFromScript: '', prompt: '', promptDirty: false },
    })),
  );
  const [modelError, setModelError] = useState<string | null>(null);
  const [previewVideo, setPreviewVideo] = useState<string | null>(null);
  const [isBatchLoading, setIsBatchLoading] = useState(false);

  // ⭐ TRAVA DE MODELO: se a constante não estiver na lista válida, a geração
  //    inteira é bloqueada. É o que impede um rename do lado do Flow de virar
  //    lote gerado no modelo errado sem ninguém perceber.
  useEffect(() => {
    const isImageValid = VALID_IMAGE_MODELS.includes(IMAGE_MODEL);
    const isVideoValid = VALID_VIDEO_MODELS.includes(VIDEO_MODEL);
    if (!isImageValid || !isVideoValid) {
      const missing = !isImageValid ? IMAGE_MODEL : VIDEO_MODEL;
      setModelError(`MODELO NÃO ENCONTRADO: "${missing}". Geração bloqueada por segurança.`);
    }
  }, []);

  // (bloco de <style> injetado — shimmer, scrollbar, overlay das variantes;
  //  omitido aqui por ser puramente cosmético. Ver o editor do Flow.)

  // ⭐⭐ SINCRONIZAÇÃO SCRIPT -> UI, blocos IMAGE.
  //    `slice(0, 4000)` é o TETO DE CARACTERES do prompt. Acima disso o texto
  //    é cortado EM SILÊNCIO — não há aviso na tela. Ver README.
  useEffect(() => {
    const parsed = parseBlocks(scriptText);
    setSlots(prev => prev.map(slot => {
      const block = parsed.find(
        b => b.type === 'IMAGE' && (b.index === slot.index || (b.index === null && slot.index === 1)),
      );
      if (!block) return slot;
      const content = block.content.slice(0, 4000);
      return {
        ...slot,
        imagePrompt: {
          ...slot.imagePrompt,
          promptFromScript: content,
          // ⭐ o par FromScript + Dirty: edição manual do operador NUNCA é
          //   sobrescrita por uma recolagem do roteiro
          prompt: slot.imagePrompt.promptDirty ? slot.imagePrompt.prompt : content,
        },
      };
    }));
  }, [scriptText]);

  // idem para os blocos TAKE
  useEffect(() => {
    const parsed = parseBlocks(scriptText);
    setSlots(prev => prev.map(slot => {
      const block = parsed.find(
        b => b.type === 'TAKE' && (b.index === slot.index || (b.index === null && slot.index === 1)),
      );
      if (!block) return slot;
      const content = block.content.slice(0, 4000);
      return {
        ...slot,
        videoPrompt: {
          ...slot.videoPrompt,
          promptFromScript: content,
          prompt: slot.videoPrompt.promptDirty ? slot.videoPrompt.prompt : content,
        },
      };
    }));
  }, [scriptText]);

  const handleRefUpload = async () => {
    try {
      const media = await Flow.media.select({ filter: 'image' });
      setRef({ status: 'success', mediaId: media.mediaId, base64: media.base64 });
    } catch (e) { console.error(e); }
  };

  // ⭐⭐ O CICLO DA ETAPA 1.
  //    1. Se há bloco REF no roteiro e nenhuma imagem de referência carregada,
  //       o REF é GERADO PRIMEIRO e o mediaId dele vira `referenceImageMediaIds`
  //       das três imagens. É o que segura o mesmo rosto nas três cenas.
  //    2. Só gera slots que ainda NÃO tiveram sucesso — rodar de novo não
  //       queima crédito no que já deu certo.
  const generateBatch = async () => {
    if (modelError || isBatchLoading) return;
    setIsBatchLoading(true);
    try {
      const parsed = parseBlocks(scriptText);
      const refBlock = parsed.find(b => b.type === 'REF');
      let currentRefId = ref.mediaId;

      if (refBlock && !currentRefId) {
        setRef(prev => ({ ...prev, status: 'loading', error: undefined }));
        try {
          const result = await Flow.generate.image({
            prompt: refBlock.content,
            modelDisplayName: IMAGE_MODEL,
            aspectRatio: '9:16',
          });
          currentRefId = result.mediaId;
          setRef({ status: 'success', mediaId: result.mediaId, base64: result.base64 });
        } catch (e: any) {
          setRef({ status: 'error', error: e.message });
          return;
        }
      }

      const slotsToGenerate = slots.filter(
        s => s.imageStatus !== 'success' && s.imagePrompt.prompt.trim(),
      );
      await Promise.allSettled(slotsToGenerate.map(async (slot) => {
        setSlots(prev => prev.map(s => s.index === slot.index
          ? { ...s, imageStatus: 'loading', error: undefined } : s));
        try {
          const result = await Flow.generate.image({
            prompt: slot.imagePrompt.prompt,
            modelDisplayName: IMAGE_MODEL,
            aspectRatio: '9:16',
            referenceImageMediaIds: currentRefId ? [currentRefId] : undefined,
          });
          setSlots(prev => prev.map(s => s.index === slot.index
            ? { ...s, imageStatus: 'success', imageMediaId: result.mediaId, imageBase64: result.base64 }
            : s));
        } catch (e: any) {
          setSlots(prev => prev.map(s => s.index === slot.index
            ? { ...s, imageStatus: 'error', error: e.message } : s));
        }
      }));
    } finally {
      setIsBatchLoading(false);
    }
  };

  const regenerateImage = async (idx: number) => {
    if (modelError || isBatchLoading) return;
    const slot = slots[idx - 1];
    setSlots(prev => prev.map(s => s.index === idx
      ? { ...s, imageStatus: 'loading', error: undefined } : s));
    try {
      const result = await Flow.generate.image({
        prompt: slot.imagePrompt.prompt,
        modelDisplayName: IMAGE_MODEL,
        aspectRatio: '9:16',
        referenceImageMediaIds: ref.mediaId ? [ref.mediaId] : undefined,
      });
      setSlots(prev => prev.map(s => s.index === idx
        ? { ...s, imageStatus: 'success', imageMediaId: result.mediaId, imageBase64: result.base64 }
        : s));
    } catch (e: any) {
      setSlots(prev => prev.map(s => s.index === idx
        ? { ...s, imageStatus: 'error', error: e.message } : s));
    }
  };

  // ⭐⭐ A CHAMADA DE VÍDEO. `durationSeconds: 10` e `firstFrameImageMediaId`
  //    ligam o take à imagem daquele slot — é o "anima a imagem fornecida".
  const generateSingleVariant = async (slotIdx: number, variantIdx: number) => {
    if (modelError || isBatchLoading) return;
    const slot = slots[slotIdx - 1];
    if (!slot.imageMediaId) return;
    setSlots(prev => prev.map(s => s.index === slotIdx ? {
      ...s,
      variants: s.variants.map((v, vI) => vI === variantIdx ? { status: 'loading' } : v),
    } : s));
    try {
      const result = await Flow.generate.video({
        prompt: slot.videoPrompt.prompt,
        modelDisplayName: VIDEO_MODEL,
        aspectRatio: '9:16',
        durationSeconds: 10,
        firstFrameImageMediaId: slot.imageMediaId,
      });
      setSlots(prev => prev.map(s => s.index === slotIdx ? {
        ...s,
        variants: s.variants.map((v, vI) => vI === variantIdx
          ? { status: 'success', mediaId: result.mediaId, base64: result.base64 } : v),
      } : s));
    } catch (e: any) {
      setSlots(prev => prev.map(s => s.index === slotIdx ? {
        ...s,
        variants: s.variants.map((v, vI) => vI === variantIdx
          ? { status: 'error', error: e.message } : v),
      } : s));
    }
  };

  // 4 variantes do MESMO slot, em paralelo
  const generateSlotVideos = async (slotIdx: number) => {
    if (modelError || isBatchLoading) return;
    const slot = slots[slotIdx - 1];
    if (!slot.imageMediaId) return;
    setSlots(prev => prev.map(s => s.index === slotIdx ? {
      ...s,
      variants: createInitialVariants().map(() => ({ status: 'loading' })),
      chosenIndex: null,
    } : s));
    const promises = Array.from({ length: 4 }).map((_, vI) => generateSingleVariant(slotIdx, vI));
    await Promise.allSettled(promises);
  };

  // ⭐ A SEQUÊNCIA 1 -> 2 -> 3: os slots são animados EM ORDEM (await por
  //   slot), e as 4 variantes de cada slot em paralelo entre si.
  const triggerVideoSequence = async () => {
    if (modelError || isBatchLoading) return;
    const slotsToAnimate = [...slots]
      .filter(s => s.imageStatus === 'success' && s.videoPrompt.prompt.trim())
      .sort((a, b) => a.index - b.index);
    if (slotsToAnimate.length === 0) return;
    setIsBatchLoading(true);
    try {
      for (const slot of slotsToAnimate) {
        setSlots(prev => prev.map(s => s.index === slot.index ? {
          ...s,
          variants: createInitialVariants().map(() => ({ status: 'loading' })),
          chosenIndex: null,
        } : s));
        const variantPromises = Array.from({ length: 4 }).map(async (_, vI) => {
          try {
            const result = await Flow.generate.video({
              prompt: slot.videoPrompt.prompt,
              modelDisplayName: VIDEO_MODEL,
              aspectRatio: '9:16',
              durationSeconds: 10,
              firstFrameImageMediaId: slot.imageMediaId,
            });
            setSlots(prev => prev.map(s => s.index === slot.index ? {
              ...s,
              variants: s.variants.map((v, idx) => idx === vI
                ? { status: 'success', mediaId: result.mediaId, base64: result.base64 } : v),
            } : s));
          } catch (e: any) {
            setSlots(prev => prev.map(s => s.index === slot.index ? {
              ...s,
              variants: s.variants.map((v, idx) => idx === vI
                ? { status: 'error', error: e.message } : v),
            } : s));
          }
        });
        await Promise.allSettled(variantPromises);
      }
    } finally {
      setIsBatchLoading(false);
    }
  };

  const selectVariant = (slotIdx: number, variantIdx: number) => {
    setSlots(prev => prev.map(s => s.index === slotIdx ? { ...s, chosenIndex: variantIdx } : s));
  };

  const downloadIndividual = async (slotIdx: number, variantIdx: number) => {
    const slot = slots[slotIdx - 1];
    const variant = slot.variants[variantIdx];
    if (variant.status === 'success' && variant.base64) {
      const label = ['A', 'B', 'C', 'D'][variantIdx];
      const filename = `slot_0${slot.index}_variant_${label}.mp4`;
      await Flow.download({ base64: variant.base64, mimeType: 'video/mp4', filename });
    }
  };

  // ⛔ o ZIP leva SÓ as variantes escolhidas (chosenIndex). Slot sem escolha
  //    fica de fora — e o aviso âmbar no rodapé lista quais faltam.
  const downloadZip = async () => {
    const zip = new JSZip();
    slots.forEach(s => {
      if (s.chosenIndex !== null) {
        const chosen = s.variants[s.chosenIndex];
        if (chosen.status === 'success' && chosen.base64) {
          zip.file(
            `slot_0${s.index}_variant_${['A', 'B', 'C', 'D'][s.chosenIndex]}.mp4`,
            chosen.base64,
            { base64: true },
          );
        }
      }
    });
    const content = await zip.generateAsync({ type: 'blob' });
    const reader = new FileReader();
    reader.onload = async () => {
      const b64 = (reader.result as string).split(',')[1];
      await Flow.download({
        base64: b64,
        mimeType: 'application/zip',
        filename: 'adbatch_vertical_output.zip',
      });
    };
    reader.readAsDataURL(content);
  };

  // (JSX omitido — aside de 300px com REF + textarea do roteiro, main com os
  //  três Cards, e o modal de preview. Ver o editor do Flow para o layout.)
}
