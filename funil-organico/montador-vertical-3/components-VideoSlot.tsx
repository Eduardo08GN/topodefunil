// Montador Vertical 3 — components/VideoSlot.tsx
// ⚠️ TRANSCRITO do editor do Google Flow em 2026-08-07 (ver README.md).
//
// ⭐⭐ A LINHA QUE IMPORTA PARA A DOUTRINA é o `label`: os três slots são
//    rotulados HOOK / MECANISMO / CTA por ÍNDICE, na marra. Não há
//    configuração — o Montador assume a família de 3 takes do funil.

import React from 'react';
import { SlotState } from '../types';

interface VideoSlotProps {
  slot: SlotState;
  onSelect: (index: number) => void;
  onRemove: (index: number) => void;
  onSwap: (index: number, direction: 'left' | 'right') => void;
  onPreview: (media: any) => void;
  isFirst: boolean;
  isLast: boolean;
}

export const VideoSlot: React.FC<VideoSlotProps> = ({
  slot,
  onSelect,
  onRemove,
  onSwap,
  onPreview,
  isFirst,
  isLast,
}) => {
  // ⛔ HOOK / MECANISMO / CTA travados por índice — é o contrato da esteira.
  const label = slot.index === 0 ? 'HOOK' : slot.index === 1 ? 'MECANISMO' : 'CTA';

  return (
    <div className="flex flex-col gap-3 w-full">
      <div className="flex items-center justify-between px-2">
        <span className="text-[11px] font-medium text-white/40 tracking-wider">
          SLOT 0{slot.index + 1} — {label}
        </span>
        {slot.media && (
          <div className="flex gap-1">
            {/* setas de reordenação: só aparecem quando há vídeo no slot, e a
                da ponta fica desabilitada (isFirst / isLast) */}
            <button
              onClick={() => onSwap(slot.index, 'left')}
              disabled={isFirst}
              className="w-8 h-8 flex items-center justify-center rounded-lg border border-[#595959] hover:bg-white/5 transition-colors disabled:opacity-20 disabled:cursor-not-allowed"
            >
              <span className="material-symbols-outlined text-[18px] text-white">chevron_left</span>
            </button>
            <button
              onClick={() => onSwap(slot.index, 'right')}
              disabled={isLast}
              className="w-8 h-8 flex items-center justify-center rounded-lg border border-[#595959] hover:bg-white/5 transition-colors disabled:opacity-20 disabled:cursor-not-allowed"
            >
              <span className="material-symbols-outlined text-[18px] text-white">chevron_right</span>
            </button>
          </div>
        )}
      </div>

      <div
        className={`relative aspect-[9/16] w-full rounded-xl border-2 border-dashed transition-all overflow-hidden ${
          slot.media
            ? 'border-transparent bg-black'
            : 'border-[#595959] bg-white/5 hover:bg-white/10 hover:border-[#7a7a7a] cursor-pointer'
        }`}
        onClick={() => !slot.media && onSelect(slot.index)}
      >
        {slot.media ? (
          <>
            <video
              src={`data:${slot.media.mimeType};base64,${slot.media.base64}`}
              className="w-full h-full object-cover cursor-pointer"
              onClick={(e) => { e.stopPropagation(); onPreview(slot.media); }}
              playsInline
              muted
            />
            <div className="absolute bottom-0 left-0 right-0 p-3 bg-gradient-to-t from-black/80 to-transparent pointer-events-none">
              <p className="text-[10px] text-white/90 truncate font-medium">{slot.media.name}</p>
            </div>
          </>
        ) : (
          <div className="absolute inset-0 flex flex-col items-center justify-center gap-2">
            <span className="material-symbols-outlined text-[32px] text-white/20">video_library</span>
            <span className="text-[12px] font-medium text-white/40">Selecionar vídeo</span>
          </div>
        )}
      </div>

      {slot.media && (
        <div className="flex gap-2 w-full">
          <button
            onClick={() => onSelect(slot.index)}
            className="flex-1 h-8 bg-[#969696] hover:bg-[#a6a6a6] active:bg-[#868686] text-black text-[10px] font-bold tracking-tight rounded-lg uppercase"
          >
            Trocar
          </button>
          <button
            onClick={() => onRemove(slot.index)}
            className="flex-1 h-8 border border-[#595959] hover:bg-white/5 text-white text-[10px] font-bold tracking-tight rounded-lg uppercase"
          >
            Remover
          </button>
        </div>
      )}
    </div>
  );
};
