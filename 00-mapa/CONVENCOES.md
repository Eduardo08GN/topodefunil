# Convenções de Documentação

Regras pra manter a base consistente e fácil de consultar/reaplicar.

## Princípios

1. **Uma ideia por arquivo.** Frameworks, princípios e swipes ficam cada um no seu `.md`.
2. **Destilar, não colar.** Material bruto vira conhecimento estruturado — não despejo de texto.
3. **Sempre com exemplo.** Todo framework/princípio precisa de ao menos 1 exemplo real ou aplicado.
4. **Linkar liberalmente.** Conectar com `[nome](caminho)` pra virar rede, não lista.
5. **Fonte rastreável.** Todo arquivo registra de onde veio (mentor, produto, aula, swipe).
6. **Português como padrão**, mas preservando o termo original em inglês entre parênteses na primeira menção — ex.: "grande ideia (*big idea*)".

## Template — Framework

```markdown
# [Nome do Framework]

- **Autor/Fonte:**
- **Serve para:**
- **Quando usar:**

## O passo a passo
1.
2.

## Por que funciona (psicologia)

## Exemplo aplicado

## Erros comuns

## Conexões
- [[link]]
```

## Template — Princípio

```markdown
# [Princípio]

> Frase-síntese em uma linha.

- **Fonte:**
- **A regra:**
- **Por quê:**
- **Como aplicar:**
- **Exemplo:**
- **Conexões:**
```

## Template — Swipe anotado

```markdown
# [Swipe] — origem

- **Formato:** (lead / VSL / email / headline / oferta...)
- **Autor:**
- **Produto/Nicho:**

## O trecho
> ...

## Dissecação
- **Gancho:**
- **Técnica usada:**
- **Gatilho psicológico:**
- **Por que converte:**

## Como roubar (aplicar)
```

## Nomenclatura de arquivos
- kebab-case, sem acento: `big-idea.md`, `rmbc-metodo.md`
- swipes: `AAAA-MM-autor-formato.md` quando fizer sentido a data
