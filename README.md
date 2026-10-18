# Auditoria e Transparência de Igrejas Cristãs ao Longo das Eras

**Projeto cívico e social de investigação documental** — dízimos, destino dos recursos, impacto social e ambiental, e casos judiciais envolvendo instituições cristãs entre 1926 e 2026.

Site público (GitHub Pages): https://aldenirfilho.github.io/AUDITORIA-E-TRANSPAR-NCIA-DE-IGREJAS-CRISTAS-AO-LONGO-DAS-ERAS-/

## Eixos

| Página | Conteúdo |
|---|---|
| `index.html` | Visão geral, regras de leitura, números-chave, linha do tempo |
| `dizimos.html` | Para onde vai o dízimo: 14 conjuntos de documentos (Mitra SP, IPB, USEB, UCB, Óbolo, Fortaleza, SUD, Universal, outros) |
| `impacto.html` | Agências auditadas (CRS, IOCC, ADRA), contas religiosas, meio ambiente, calculadora de cenários (vidas × hectares) |
| `casos.html` | Fé, dinheiro e enriquecimento pessoal: 10 fichas com situação processual |
| `panorama.html` | 30 dossiês, 1926–2026, filtráveis por tradição e situação |
| `metodo.html` | Matriz de afirmações e provas, glossário jurídico, documentos a exigir, modelo de pedido de informação |
| `fontes.html` | Todos os documentos primários com URL |

## Como editar

```bash
# edite src/pages/<pagina>.html (somente o <main>)
python3 build.py        # gera os .html da raiz com cabeçalho, navegação e rodapé
python3 -m http.server  # pré-visualize em http://localhost:8000
```

Regras editoriais em [`.github/copilot-instructions.md`](.github/copilot-instructions.md) — valem para humanos e para o Copilot.

## Princípios

1. Todo número tem fonte primária, perímetro (pessoa jurídica, exercício) e limite de leitura.
2. Condenação, responsabilidade civil, acusação pendente e caso encerrado nunca se misturam.
3. Arquivamentos, absolvições e prescrições aparecem ao lado de cada denúncia.
4. Não se somam valores de entidades, moedas ou exercícios diferentes.
5. Ausência de dado publicado não é evidência de desvio.

Data de revisão das pesquisas: **18 de outubro de 2026**. Autor: Aldenir Rocha de Oliveira Filho.

## Edição Turbo TEMI 360X / Turbo X Profânico

Oito novos dossiês em `investigacoes.html`, com dados em `src/data/investigacoes.json`, e uma coleção de dez ilustrações em `imagens.html`. O tema usa fontes locais do sistema e arquivos próprios, sem telemetria ou APIs em execução.

- [Auditoria e validação](docs/AUDITORIA-2026-10-18.md)
- [Visão geral da coleção](docs/colecao-visual.html)
- [Prompts e origem das imagens](docs/prompts-turbo-x-profanico.json)
- [Manifesto de arquivos e hashes](assets/profanico/manifest.json)

Após editar, execute:

```bash
python3 build.py
python3 scripts/validate.py
node --check app.js
git diff --check
```

Os HTML da raiz devem corresponder às fontes. A data da edição não certifica atualização integral dos processos históricos. Revisão editorial humana e comparação visual antes/depois precedem o merge e a publicação.
