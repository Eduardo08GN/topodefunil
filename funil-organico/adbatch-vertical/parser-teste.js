// Porte VERBATIM do utils-parser.ts transcrito em funil-organico/adbatch-vertical/.
// So' foram removidos os tipos TypeScript — nenhuma logica mudou.
// ⛔ Rodar o parser DE VERDADE, em JS, e nao reimplementar em Python: a regex
//    e' JavaScript e um porte poderia divergir justamente no caso que importa.

function normalizeText(text) {
  if (!text) return '';
  return text
    .replace(/\r\n/g, '\n')
    .replace(/[\u200B-\u200D\uFEFF\u2060\u00AD]/g, '')
    .replace(/\u00A0/g, ' ');
}

function cleanContent(lines, type) {
  return lines.filter(line => {
    const trimmed = line.trim();
    if (/^([-=])\1+$/.test(trimmed)) return false;
    if (/^---.*---$/.test(trimmed)) return false;
    if (type === 'TAKE') {
      if (line.startsWith('Copy falada:')) return false;
      if (line.startsWith('Contagem:')) return false;
    }
    return true;
  });
}

function removeLabels(text) {
  return text.replace(
    /^(HOOK|CTA|REFORÇO|MECANISMO|INTRO|BODY|OUTRO|OFERTA)\s*([+:—–-])\s*/i,
    '',
  ).trim();
}

function parseBlocks(text) {
  const normalized = normalizeText(text);
  const lines = normalized.split('\n');
  const blocks = [];
  const headerRegex =
    /^(?:[*#> ]+)?(REF|IMAGE|TAKE)(?![A-Z])(?:\s*(\d+))?(?:[A-Z])?(?:\/\d+)?(?:\s*[:—–-])?\s*(.*)$/i;
  let currentBlock = null;

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
        type: match[1].toUpperCase(),
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

// --- o mapeamento bloco -> slot, copiado dos dois useEffect do App.tsx -------
// slots = Array.from({length: MAX_SLOTS})
// parsed.find(b => b.type === T && (b.index === slot.index || (b.index === null && slot.index === 1)))
function mapaSlots(parsed, MAX) {
  const out = [];
  for (let i = 1; i <= MAX; i++) {
    const img = parsed.find(b => b.type === 'IMAGE' && (b.index === i || (b.index === null && i === 1)));
    const tak = parsed.find(b => b.type === 'TAKE' && (b.index === i || (b.index === null && i === 1)));
    out.push({ slot: i, image: img ? img.content.length : null, take: tak ? tak.content.length : null });
  }
  return out;
}

const fs = require('fs');
const MAX = 2;
const alvo = process.argv[2];
const texto = fs.readFileSync(alvo, 'utf8');
const parsed = parseBlocks(texto);

console.log('BLOCOS DEVOLVIDOS PELO PARSER: ' + parsed.length);
for (const b of parsed) {
  console.log('  %s index=%s  %d chars%s',
    b.type.padEnd(5), String(b.index).padEnd(4), b.content.length,
    b.content.length > 4000 ? '   *** ACIMA DE 4000: CORTE SILENCIOSO ***' : '');
}
console.log('');
console.log('MAPEAMENTO PARA OS ' + MAX + ' SLOTS:');
for (const s of mapaSlots(parsed, MAX)) {
  console.log('  slot %d  IMAGE %s  TAKE %s', s.slot,
    s.image === null ? 'AUSENTE' : s.image + ' chars',
    s.take === null ? 'AUSENTE' : s.take + ' chars');
}
const descartados = parsed.filter(b => b.type !== 'REF' && b.index !== null && b.index > MAX);
console.log('');
console.log('DESCARTADOS (index > ' + MAX + '): ' + descartados.length
  + (descartados.length ? '  -> ' + descartados.map(b => b.type + ' ' + b.index).join(', ') : ''));

const takes = parsed.filter(b => b.type === 'TAKE');
console.log('');
console.log('CONTEUDO DOS TAKE — o que sobreviveu ao cleanContent:');
for (const t of takes) {
  const temDialogue = /(^|\n)Dialogue:/.test(t.content);
  const temAudio = /(^|\n)Audio:/.test(t.content);
  const temCopyFalada = /(^|\n)Copy falada:/.test(t.content);
  const temContagem = /(^|\n)Contagem:/.test(t.content);
  console.log('  TAKE %s  Dialogue:%s  Audio:%s  | "Copy falada:" ainda presente:%s  "Contagem:":%s',
    t.index, temDialogue ? 'SIM' : 'NAO ***', temAudio ? 'SIM' : 'NAO ***',
    temCopyFalada ? 'SIM ***' : 'nao', temContagem ? 'SIM ***' : 'nao');
}
