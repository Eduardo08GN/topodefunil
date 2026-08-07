// Montador Vertical 3 — types.ts
// ⚠️ TRANSCRITO do editor do Google Flow em 2026-08-07 (ver README.md).
//
// ⭐ O estado inteiro do Montador cabe aqui: três slots, cada um com um
//    `MediaItem` do Flow ou nada. Não há prompt, não há geração — o Montador
//    NÃO cria vídeo, ele ORDENA vídeo que já existe.

import { MediaItem } from 'flow-sdk';

export interface SlotState {
  index: number;
  media: MediaItem | null;
}
