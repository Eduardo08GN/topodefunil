# 🖥️ RUNBOOK — do agente Markdown ao `.exe` na área de trabalho

> Como um agente de doutrina vira **ferramenta CLI**, depois **app desktop**, e
> por fim um **executável offline** entregue numa pasta do PC. Escrito a partir
> do primeiro caso completo: o **FLAGRANTE LUCAS**, 2026-07-30.
>
> Este arquivo é a etapa técnica. O pipeline conceitual (garimpo → leitura ótica
> → agente) mora em [`PIPELINE-NOVO-AGENTE.md`](../PIPELINE-NOVO-AGENTE.md).

---

## POR QUE PORTAR UM AGENTE PARA CÓDIGO

O agente Markdown é a **doutrina**; o app é o **operador dela**. A migração não
foi estética — nasceu de três custos medidos em produção:

| Custo | O que acontecia | O que o código resolve |
|---|---|---|
| **String travada corrompida** | eu reescrevia um bloco validado "com as minhas palavras" ao enxugar o prompt — o D1 virou esqueleto 3D | as strings viram **constantes**; não passam mais pela digitação |
| **Auditoria por julgamento** | eu contava a cota do órgão no olho e contei errado a meu favor (3/5 declarado como 4/5) | **linter em regex**: conta, soma e varre token banido |
| **Mode-collapse** | solto, o modelo (e eu) gravita pro mesmo protótipo | **sorteio de eixos** com ledger anti-repetição |

> **A regra de corte:** vai para o código o que é **mecânico e verificável**
> (strings travadas, contagem, token proibido, sorteio). Fica no Markdown o que
> é **julgamento** (o porquê da regra, a evidência, o arco narrativo). Código
> não substitui doutrina — ele impede que a doutrina seja violada por descuido.

---

## AS 3 CAMADAS DA FERRAMENTA

```
<agente>_lucas.py          ← MOTOR: pools + strings travadas + gerador + linter
<agente>_lucas_app.py      ← INTERFACE: tkinter, importa o motor
<AGENTE>-LUCAS.exe         ← DISTRIBUIÇÃO: PyInstaller --onefile --windowed
```

**Uma fonte de verdade.** O app **importa** o motor, nunca duplica. Regra nova
entra no motor e aparece no app e no `.exe` sem tocar em interface.

### Anatomia do motor

| Bloco | O que é | Regra |
|---|---|---|
| **Strings travadas** | `D1_IMAGE`, `D1_TAKE`, `IMOBILIDADE`, `NEGACAO_AVE`, `ANTICELEB`, `CAUDA`, `AGENCIA_*` | cópia literal da doutrina. ⛔ **Nunca reescrever nem comprimir** |
| **Pools sorteáveis** | ocasião, prop, ambiente, REF, vítima, mulher | cada item é um dict; ocasião carrega selo `V` (validada em render) ou `N` (nova) |
| **Pools de copy** | hooks, descobertas, rituais, redenções, CTAs + `QUEM_CONTOU`, `BARREIRAS`, `GATES` | templates com slots; o núcleo do órgão entra por `rng.sample(NUCLEO, 4)` — 4 distintos, cota garantida |
| **Linter** | `lint(spec, blocos)` → `[(nível, mensagem)]` | `ERRO` trava, `AVISO` só sinaliza |
| **Gerador** | `montar(spec)` → dict com os 11 blocos | ordem de entrega: BLOCO 0 → 5 IMAGE → 5 TAKE |
| **Ledger** | `.<agente>-ledger.json` | anti-repetição por eixo, por página |

### O que o linter cobre hoje

Cota do órgão ≥4/5 com rotação · teto de fala por cena e total · `gelatin trick`
literal · CTA = GELATIN e ⛔ `BOOK`/`YES` · tokens banidos **separados por
bloco** (`stiff`/`limp`/`pulse`/`geoduck`/`neck` só no TAKE · `large`/`big`/
`engorged`/`veins` no IMAGE · `the victim`/`the narrator` em qualquer lugar) ·
imobilidade declarada nos takes com prop · blocos travados íntegros.

> ⚠️ **Regra de contraste por construção.** No FLAGRANTE, o pool de REF só tem
> homens de cabeleira farta, barbeados e sem óculos; o de vítima, só carecas de
> bigode e óculos. Os 3 eixos do F4b nascem garantidos — nenhuma verificação
> necessária. **Preferir tornar a regra impossível de violar a checá-la depois.**

---

## A INTERFACE — o que a fez ficar intuitiva

Três decisões que valem para qualquer agente portado:

1. **Passos numerados** — `1 O vídeo sorteado` → `2 A copy` → `3 Copie para o
   AdBatch`. O olho sabe para onde ir sem manual.
2. **Resumo em português** antes de qualquer inglês: *"Num casamento, o colega
   segura um geoduck murcho no próprio colo enquanto o narrador aponta e a mesa
   ri."* É o que permite aprovar ou re-sortear em dois segundos.
3. **Troca por eixo, não só re-sorteio total.** Um botão `trocar` por eixo. Não
   gostou só do prop, troca o prop. ⚠️ Trocar a ocasião **reescreve hook e cena
   4**, porque o evento e o eco vivem nessas falas — sem isso o vídeo fala de um
   casamento com imagem de clube de golfe.

Mais: contador `n/teto` de palavras por cena que fica amarelo ao estourar · botão
que **pisca verde** ao copiar · `copiar os 5 IMAGE` / `copiar os 5 TAKE` (o
formato de entrega, agrupado) · duplo-clique no bloco copia · `Ctrl+R` sorteia ·
`Ctrl+S` salva.

**Paleta:** fill sólido, contraste alto, zero cinza-sobre-cinza, zero emoji e
zero box gratuito — a mesma régua anti-slop das bridge pages.

⚠️ **O botão `marcar como usado`.** O app **lê** o ledger mas **não grava** ao
sortear: se gravasse, cada troca de eixo poluiria o histórico com combinações
descartadas. Só grava quando o operador clica, quando o lote foi de fato usado.

---

## O BUILD DO `.exe`

**Pré-requisito:** `pip install pyinstaller` (única coisa que precisa de rede —
o app em si é 100% offline).

```bash
cd funil-organico
python -m PyInstaller --noconfirm --clean --onefile --windowed \
  --name "FLAGRANTE-LUCAS" \
  --paths "C:\Users\edlut\Topodefunil\funil-organico" \
  --hidden-import flagrante_lucas \
  --distpath "%TEMP%\flagbuild\dist" --workpath "%TEMP%\flagbuild\build" \
  --specpath "%TEMP%\flagbuild" \
  flagrante_lucas_app.py
```

Saída: **um arquivo de ~10 MB**, sem instalador, sem Python no destino.

### Os 3 gotchas que custaram tentativa

| Sintoma | Causa | Correção |
|---|---|---|
| `Unable to find ... when adding binary and data files` | `--add-data` resolve o caminho **relativo ao `--specpath`**, não ao cwd | usar **`--paths` + `--hidden-import`** e deixar a análise de import fazer o trabalho — o motor é importado no topo do app |
| ledger sumindo a cada execução | congelado, `__file__` aponta para a pasta temporária `_MEIPASS`, que é destruída ao fechar | detectar `sys.frozen` e ancorar o ledger em `os.path.dirname(sys.executable)` |
| lixo de build no repo | `dist/`, `build/`, `.spec` nascem no cwd | mandar os três para `%TEMP%` com `--distpath/--workpath/--specpath` |

O trecho que resolve o segundo, no topo do app:

```python
if getattr(sys, "frozen", False):          # rodando como .exe do PyInstaller
    BASE = os.path.dirname(sys.executable)
    sys.path.insert(0, sys._MEIPASS)
else:
    BASE = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, BASE)
import flagrante_lucas as motor
motor.LEDGER = os.path.join(BASE, ".flagrante-ledger.json")
```

---

## A ENTREGA NO PC

Pasta de destino: **`C:\Users\edlut\Desktop\agentes_py`** — plural de propósito,
é a casa de todos os agentes portados.

| Arquivo | Papel |
|---|---|
| `<AGENTE>-LUCAS.exe` | o app. Duplo-clique |
| `<agente>_lucas.py` · `<agente>_lucas_app.py` | fonte, para rodar via Python se preciso |
| `ATUALIZAR.bat` | copia os `.py` novos do repo (⚠️ **não** atualiza o `.exe` — esse exige recompilar) |
| `.<agente>-ledger.json` | histórico anti-repetição, nasce ao lado do `.exe` |

### Validação obrigatória antes de entregar

Não basta compilar — **abrir o `.exe` de verdade e tirar print**. O smoke test
que pega erro de construção sem abrir o `mainloop`:

```python
app = App(); app.update_idletasks()
app.trocar_eixo("ocasiao"); app.aplicar_copy()
app.copiar_grupo("IMAGE"); app.copiar_bloco()
app.destroy()
```

E o teste do executável, que é o que de fato prova (PowerShell): abrir com
`Start-Process`, esperar ~9 s, conferir que o processo **continua vivo** (se
morreu sozinho, houve exceção invisível por causa do `--windowed`), capturar a
tela com `System.Drawing` e encerrar.

⚠️ **`--windowed` engole o traceback.** Se o `.exe` fechar sozinho, recompile
**sem** `--windowed` e rode pelo terminal para ver o erro.

---

## CHECKLIST DE PORTE DE UM AGENTE NOVO

- [ ] As **strings travadas** do agente foram extraídas para constantes — copiadas caractere por caractere da doutrina?
- [ ] Os **pools** cobrem os eixos que o agente declara, e cada ocasião tem selo `V`/`N`?
- [ ] O **linter** cobre o checklist mecânico do agente (cota, tetos, tokens banidos, blocos íntegros)?
- [ ] Alguma regra virou **impossível de violar por construção** em vez de checada depois?
- [ ] O **ledger** tem nome próprio do agente e sobrevive ao congelamento?
- [ ] A interface tem **passos numerados**, **resumo em português** e **troca por eixo**?
- [ ] Trocar um eixo que alimenta a copy **reescreve as falas dependentes**?
- [ ] Smoke test roda sem `mainloop` e exercita as ações principais?
- [ ] O `.exe` foi **aberto de verdade**, sobreviveu 9 s e rendeu print?
- [ ] Entregue em `agentes_py` com `ATUALIZAR.bat`, e o lixo de build ficou no `%TEMP%`?

---

## Conexões

- [`PIPELINE-NOVO-AGENTE.md`](../PIPELINE-NOVO-AGENTE.md) — o pipeline conceitual (etapas 1-8); este runbook é o detalhe das etapas 9-11
- [`AGENTE_ED_FLAGRANTE_V1.md`](../AGENTE_ED_FLAGRANTE_V1.md) — a doutrina que o `flagrante_lucas.py` executa
- [`licoes-producao-veo.md`](licoes-producao-veo.md) — por que as strings travadas e o linter existem
- [`prop-metaforas.md`](prop-metaforas.md) — fonte da verdade das strings travadas de prop
