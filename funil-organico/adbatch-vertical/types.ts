// AdBatch Vertical 3 — v2.5
// ⚠️ TRANSCRITO do editor do Google Flow em 2026-08-07, não exportado do git
// dele. A indentação foi reconstruída (o painel perde recuo ao copiar); os
// identificadores, tipos e literais estão fiéis. Ver README.md desta pasta.

export type MediaType = 'image' | 'video';

export interface PromptState {
  promptFromScript: string;
  prompt: string;
  promptDirty: boolean;
}

export interface VideoVariant {
  status: 'idle' | 'loading' | 'success' | 'error';
  mediaId?: string;
  base64?: string;
  error?: string;
}

export interface MediaSlot {
  index: number; // 1, 2, 3
  imageStatus: 'idle' | 'loading' | 'success' | 'error';
  imageMediaId?: string;
  imageBase64?: string;
  // v2.3: 4 variants per slot (A, B, C, D)
  variants: VideoVariant[];
  chosenIndex: number | null; // 0..3 or null
  imagePrompt: PromptState;
  videoPrompt: PromptState;
  error?: string;
}

export interface RefState {
  status: 'idle' | 'loading' | 'success' | 'error';
  mediaId?: string;
  base64?: string;
  error?: string;
}

export type AppStage = 'images' | 'videos';
