// Prova que o swap IMUTAVEL que eu mando no prompt do Montador V2 funciona —
// e que o da V3 realmente muta o objeto original.
// ⛔ Codigo que vai num prompt tem de ser RODADO. Mandar o builder copiar uma
//    linha que eu nunca executei e' entregar defeito com cara de correcao.

function swapV3(prev, index, targetIndex) {       // como esta' na V3, hoje
  const newSlots = [...prev];
  const tempMedia = newSlots[index].media;
  newSlots[index].media = newSlots[targetIndex].media;
  newSlots[targetIndex].media = tempMedia;
  return newSlots;
}

function swapV2(prev, index, targetIndex) {       // o que o prompt manda
  return prev.map((s, i) =>
    i === index      ? { ...s, media: prev[targetIndex].media } :
    i === targetIndex ? { ...s, media: prev[index].media } : s);
}

function novo() {
  return [{ index: 0, media: 'A' }, { index: 1, media: 'B' }];
}

for (const [nome, fn] of [['V3 (raso)', swapV3], ['V2 (imutavel)', swapV2]]) {
  const antes = novo();
  const ref0 = antes[0];                 // guarda o objeto ORIGINAL do slot 0
  const snapshot = antes.map(s => s.media).join(',');
  const depois = fn(antes, 0, 1);
  console.log('%s', nome);
  console.log('   resultado do swap      : %s', depois.map(s => s.media).join(','));
  console.log('   o array e novo?        : %s', depois !== antes);
  console.log('   os OBJETOS sao novos?  : %s', depois[0] !== ref0);
  console.log('   o objeto ORIGINAL mudou: %s   <-- %s',
    ref0.media !== 'A',
    ref0.media !== 'A' ? 'MUTACAO (quebra se memoizar)' : 'intacto');
  console.log('   `prev` continuava %s durante a leitura', snapshot);
  console.log('');
}

// ⭐ o caso que realmente importa: o swapV2 le' `prev`, nao o array em
//    construcao. Se lesse o array novo, o segundo ramo leria o valor JA'
//    trocado e os dois slots ficariam iguais. Prova com 2 slots:
const r = swapV2(novo(), 0, 1);
console.log('sem perda de dado no swap: %s',
  r[0].media === 'B' && r[1].media === 'A' ? 'OK' : 'FALHOU -> ' + JSON.stringify(r));

// e o ZIP: buraco preservado
const slots = [{ index: 0, media: null }, { index: 1, media: 'X' }];
const nomes = [];
slots.forEach(s => { if (s.media) nomes.push('video_0' + (s.index + 1) + '.mp4'); });
console.log('so o slot 02 preenchido -> ZIP com: %s   %s',
  nomes.join(', '), nomes[0] === 'video_02.mp4' ? 'OK (buraco preservado)' : 'FALHOU');
