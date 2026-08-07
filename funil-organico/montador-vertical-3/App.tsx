// Montador Vertical 3 — App.tsx
// ⚠️ TRANSCRITO do editor do Google Flow em 2026-08-07 (ver README.md).
//
// ⭐⭐ O QUE ESTA FERRAMENTA É: o último degrau da esteira. Ela NÃO gera nada
//    — pega três vídeos que já existem na mídia do Flow, deixa você ordenar,
//    e exporta `adbatch_vertical_3.zip` com os nomes `video_01..03.mp4`.
//    ⛔ A ORDEM DO ARQUIVO É A ORDEM DO SLOT, não a ordem em que você escolheu.

import React, { useState, useEffect, useCallback } from 'react';
import { Flow } from 'flow-sdk';
import JSZip from 'jszip';
import { SlotState } from './types';
import { VideoSlot } from './components/VideoSlot';
import { PreviewModal } from './components/PreviewModal';

export default function App() {
  const [slots, setSlots] = useState<SlotState[]>([
    { index: 0, media: null },
    { index: 1, media: null },
    { index: 2, media: null },
  ]);
  const [previewMedia, setPreviewMedia] = useState<any>(null);
  const [downloading, setDownloading] = useState(false);

  // ⭐ Só um vídeo toca por vez. Sem isto, os três autoplay ao mesmo tempo e
  //   não dá para julgar nenhum. Listener na fase de CAPTURA (`true`) porque
  //   o evento `play` não borbulha.
  useEffect(() => {
    const handlePlay = (e: Event) => {
      const playingVideo = e.target as HTMLVideoElement;
      if (playingVideo.tagName !== 'VIDEO') return;
      const allVideos = document.querySelectorAll('video');
      allVideos.forEach(v => { if (v !== playingVideo) v.pause(); });
    };
    window.addEventListener('play', handlePlay, true);
    return () => window.removeEventListener('play', handlePlay, true);
  }, []);

  const handleSelectMedia = async (index: number) => {
    try {
      const media = await Flow.media.select({ filter: 'video' });
      setSlots(prev => prev.map(s => s.index === index ? { ...s, media } : s));
    } catch (err) {
      console.error('Selection cancelled or failed');
    }
  };

  const handleRemoveMedia = (index: number) => {
    setSlots(prev => prev.map(s => s.index === index ? { ...s, media: null } : s));
  };

  // ⚠️ MUTAÇÃO NO ARRAY COPIADO: `[...prev]` é cópia RASA, então
  //    `newSlots[index].media = ...` escreve no objeto ORIGINAL. Funciona
  //    porque o `setSlots` devolve um array novo e o React re-renderiza, mas é
  //    o tipo de coisa que quebra se alguém memoizar o slot mais tarde.
  const handleSwap = (index: number, direction: 'left' | 'right') => {
    const targetIndex = direction === 'left' ? index - 1 : index + 1;
    if (targetIndex < 0 || targetIndex >= slots.length) return;
    setSlots(prev => {
      const newSlots = [...prev];
      const tempMedia = newSlots[index].media;
      newSlots[index].media = newSlots[targetIndex].media;
      newSlots[targetIndex].media = tempMedia;
      return newSlots;
    });
  };

  // ⛔ O ZIP É POR SLOT, NÃO POR PREENCHIDO. `slots.forEach` percorre os três
  //    em ordem e só escreve os que têm mídia — então um pacote incompleto sai
  //    com buraco no meio (video_01 + video_03), e não renumerado.
  const handleDownload = async () => {
    const activeMedia = slots.filter(s => s.media !== null);
    if (activeMedia.length === 0) return;
    setDownloading(true);
    try {
      const zip = new JSZip();
      slots.forEach((slot) => {
        if (slot.media) {
          // Internal naming: video_01.mp4, video_02.mp4, video_03.mp4
          const filename = `video_0${slot.index + 1}.mp4`;
          zip.file(filename, slot.media.base64, { base64: true });
        }
      });
      const blob = await zip.generateAsync({ type: 'blob' });
      const reader = new FileReader();
      reader.onload = async () => {
        const base64 = (reader.result as string).split(',')[1];
        await Flow.download({
          base64,
          mimeType: 'application/zip',
          filename: 'adbatch_vertical_3.zip',
        });
        setDownloading(false);
      };
      reader.readAsDataURL(blob);
    } catch (err) {
      console.error('Download failed', err);
      setDownloading(false);
    }
  };

  const filledCount = slots.filter(s => s.media !== null).length;
  const missingCount = 3 - filledCount;

  // (JSX omitido — grid de três VideoSlot, rodapé fixo com o aviso âmbar de
  //  "faltam N vídeos" e o botão de ZIP, mais o PreviewModal.)
}
