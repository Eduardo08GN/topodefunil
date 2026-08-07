// Montador Vertical 3 — components/PreviewModal.tsx
// ⚠️ TRANSCRITO do editor do Google Flow em 2026-08-07 (ver README.md).
//
// Modal de conferência: 9:16 a 90vh, clique fora fecha, `stopPropagation` no
// player para o clique no vídeo não fechar o modal.

import React from 'react';
import { MediaItem } from 'flow-sdk';

interface PreviewModalProps {
  media: MediaItem | null;
  onClose: () => void;
}

export const PreviewModal: React.FC<PreviewModalProps> = ({ media, onClose }) => {
  if (!media) return null;

  return (
    <div
      className="fixed inset-0 z-[100] flex items-center justify-center bg-black/60 backdrop-blur-md p-4 animate-in fade-in duration-200"
      onClick={onClose}
    >
      <button
        className="fixed top-6 right-6 z-[110] w-12 h-12 flex items-center justify-center rounded-full bg-white/10 hover:bg-white/20 text-white transition-all shadow-xl"
        onClick={onClose}
      >
        <span className="material-symbols-outlined text-[28px]">close</span>
      </button>

      <div
        className="relative h-[90vh] aspect-[9/16] bg-black rounded-2xl overflow-hidden shadow-2xl border border-white/10 animate-in zoom-in-95 duration-300"
        onClick={(e) => e.stopPropagation()}
      >
        <video
          src={`data:${media.mimeType};base64,${media.base64}`}
          className="w-full h-full object-contain"
          controls
          autoPlay
          playsInline
        />
      </div>
    </div>
  );
};
