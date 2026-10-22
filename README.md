# Auditoria e Transparência de Igrejas Cristãs ao Longo das Eras

**Projeto cívico e social de investigação documental** — dízimos, destino dos recursos, impacto social e ambiental, governança e casos judiciais envolvendo instituições cristãs entre 1926 e 2026.

Site público (GitHub Pages): https://aldenirfilho.github.io/AUDITORIA-E-TRANSPAR-NCIA-DE-IGREJAS-CRISTAS-AO-LONGO-DAS-ERAS-/

## Eixos

| Página | Conteúdo |
|---|---|
| `index.html` | Visão geral, regras de leitura, números-chave e caminhos para os dossiês |
| `cenario-atual.html` | Cenário evangélico brasileiro em 2026: IBGE, regime jurídico, imunidade, riscos e agenda de transparência |
| `agentes.html` | Arquitetura de 14 agentes para catalogação, investigação judicial, auditoria financeira, impacto social e contraditório |
| `investigacoes.html` | Oito dossiês documentados sobre fraude, desvio, governança e decisões oficiais |
| `dizimos.html` | Para onde vai o dízimo: 14 conjuntos de documentos (Mitra SP, IPB, USEB, UCB, Óbolo, Fortaleza, SUD, Universal, outros) |
| `impacto.html` | Agências auditadas (CRS, IOCC, ADRA), contas religiosas, meio ambiente e calculadora de cenários |
| `casos.html` | Fé, dinheiro e enriquecimento pessoal: 10 fichas com situação processual |
| `panorama.html` | 30 dossiês, 1926–2026, filtráveis por tradição e situação |
| `metodo.html` | Matriz de afirmações e provas, glossário jurídico, documentos a exigir e modelo de pedido de informação |
| `fontes.html` | Documentos primários, institucionais e jornalísticos com URL, emissor e data |
| `imagens.html` | Coleção editorial Turbo TEMI 360X sobre fé, dinheiro, poder e transparência |

## Cenário atual 2026

A nova síntese registra **47.418.024 pessoas evangélicas** no recorte de 10 anos ou mais do Panorama do Censo 2022 e descreve o marco jurídico vigente. O dado demográfico não é usado como indicador de arrecadação ou integridade.

A página também explicita cinco limites:

1. não existe soma nacional confiável de “corrupção das igrejas evangélicas”;
2. ausência de balanço público é lacuna de transparência, não prova criminal;
3. patrimônio pessoal, patrimônio institucional e empresas relacionadas são objetos distintos;
4. casos e valores devem ser individualizados por CNPJ, período e processo;
5. imunidade tributária não equivale a imunidade penal, civil, administrativa ou ética.

## Arquitetura de agentes 360

O sistema organiza 14 funções especializadas:

- catalogação de entidades e validação de identidade jurídica;
- investigação judicial e atualização de desfechos;
- auditoria financeira, patrimonial e de beneficiários;
- detecção documental de fraude, lavagem, corrupção e desvio;
- análise de captação, impacto social e déficit de transparência;
- contraditório, controle de qualidade e comunicação institucional.

A escala E1–E5 controla a linguagem usada em cada ficha. O **IRIR** organiza prioridade de pesquisa e não constitui sentença nem ranking automático de culpa.

## Como editar

```bash
# edite src/pages/<pagina>.html (somente o <main>)
python3 build.py        # gera os .html da raiz com cabeçalho, navegação e rodapé
python3 -m http.server  # pré-visualize em http://localhost:8000
```

Regras editoriais em [`.github/copilot-instructions.md`](.github/copilot-instructions.md) — valem para humanos e para o Copilot.

## Princípios

1. Todo número tem fonte primária, perímetro, período e limite de leitura.
2. Condenação, responsabilidade civil, acusação pendente e caso encerrado nunca se misturam.
3. Arquivamentos, absolvições e prescrições aparecem ao lado de cada denúncia.
4. Não se somam valores de entidades, moedas ou exercícios diferentes.
5. Ausência de dado publicado não é evidência de desvio.
6. Um dirigente ou CNPJ local não representa automaticamente toda a denominação.
7. O contraditório e as correções permanecem parte do registro público.

Data de revisão estrutural: **22 de outubro de 2026**. Autor: Aldenir Rocha de Oliveira Filho.

## Edição Turbo TEMI 360X / Turbo X Profânico

Oito dossiês em `investigacoes.html`, dados estruturados em `src/data/investigacoes.json`, uma coleção de dez ilustrações em `imagens.html`, o cenário brasileiro atualizado e a arquitetura de agentes de auditoria. O tema usa fontes locais do sistema e arquivos próprios, sem telemetria ou APIs em execução.

- [Cenário atual 2026](cenario-atual.html)
- [Arquitetura de agentes 360](agentes.html)
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
