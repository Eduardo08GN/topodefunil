// AdBatch Vertical 3 — v2.5 · utils/parser.ts
// ⚠️ TRANSCRITO do editor do Google Flow em 2026-08-07 (ver README.md).
//
// ⭐ ESTE ARQUIVO É O CONTRATO DE ENTRADA DOS NOSSOS 19 MOTORES. Tudo o que os
//    `<angulo>_short.py` emitem passa por aqui antes de virar imagem ou vídeo.

/**
 * Normaliza o texto removendo caracteres invisíveis, normalizando quebras de linha
 * e espaços não-separáveis.
 */
export function normalizeText(text: string): string {
  if (!text) return '';
  return text
    .replace(/\r\n/g, '\n')
    .replace(/[\u200B-\u200D\uFEFF\u2060\u00AD]/g, '') // Zero-width e soft hyphens
    .replace(/\u00A0/g, ' '); // Non-breaking space
}

/**
 * Remove linhas decorativas e anotações de produção.
 */
function cleanContent(lines: string[], type: 'REF' | 'IMAGE' | 'TAKE'): string[] {
  return lines.filter(line => {
    const trimmed = line.trim();
    // Descartar decorativas
    if (/^([-=])\1+$/.test(trimmed)) return false;
    if (/^---.*---$/.test(trimmed)) return false;
    // Metadados TAKE
    if (type === 'TAKE') {
      if (line.startsWith('Copy falada:')) return false;
      if (line.startsWith('Contagem:')) return false;
    }
    return true;
  });
}

/**
 * Remove rótulos de beat (HOOK, CTA, etc.) do início da string.
 */
function removeLabels(text: string): string {
  return text.replace(
    /^(HOOK|CTA|REFORÇO|MECANISMO|INTRO|BODY|OUTRO|OFERTA)\s*([+:—–-])\s*/i,
    '',
  ).trim();
}

export interface ParsedBlock {
  type: 'REF' | 'IMAGE' | 'TAKE';
  index: number | null;
  content: string;
}

/**
 * Divide o texto em blocos baseados nos cabeçalhos REF, IMAGE e TAKE.
 */
export function parseBlocks(text: string): ParsedBlock[] {
  const normalized = normalizeText(text);
  const lines = normalized.split('\n');
  const blocks: ParsedBlock[] = [];
  const headerRegex =
    /^(?:[*#> ]+)?(REF|IMAGE|TAKE)(?![A-Z])(?:\s*(\d+))?(?:[A-Z])?(?:\/\d+)?(?:\s*[:—–-])?\s*(.*)$/i;
  let currentBlock: {
    type: 'REF' | 'IMAGE' | 'TAKE';
    index: number | null;
    lines: string[];
  } | null = null;

  for (const line of lines) {
    const match = line.match(headerRegex);
    if (match) {
      if (currentBlock) {
        blocks.push({
          type: currentBlock.type,
          index: currentBlock.index,
          content: removeLabels(
            cleanContent(currentBlock.lines, currentBlock.type).join('\n').trim(),
          ),
        });
      }
      currentBlock = {
        type: match[1].toUpperCase() as any,
        index: match[2] ? parseInt(match[2], 10) : null,
        lines: match[3] ? [match[3]] : [],
      };
    } else if (currentBlock) {
      currentBlock.lines.push(line);
    }
  }

  if (currentBlock) {
    blocks.push({
      type: currentBlock.type,
      index: currentBlock.index,
      content: removeLabels(
        cleanContent(currentBlock.lines, currentBlock.type).join('\n').trim(),
      ),
    });
  }

  return blocks;
}
