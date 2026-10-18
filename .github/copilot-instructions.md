# Instruções para o GitHub Copilot — Auditoria e Transparência de Igrejas Cristãs

## O que é este repositório
Site estático público (GitHub Pages) de um projeto cívico de investigação documental sobre
arrecadação, destinação e impacto de recursos de instituições cristãs, 1926–2026.
Idioma: português brasileiro.

## Estrutura
- `src/pages/*.html` — conteúdo de cada página (apenas o `<main>`). **Edite aqui.**
- `build.py` — injeta cabeçalho, navegação e rodapé e gera os `*.html` na raiz. Rode `python3 build.py` após editar.
- `style.css` / `base.css` — tokens de design (papel, tinta, vermelho-óxido), componentes (`.ficha`, `.ledger`, `.table`, `.badge`, `.calc`).
- `app.js` — menu móvel, filtros (`data-filter-group` + `data-tags`), calculadora de cenários, botão copiar.
- `assets/` — imagens otimizadas (JPEG ≤ 250 KB).

## Regras editoriais (obrigatórias)
1. Todo número vem acompanhado de link para a fonte primária, perímetro (pessoa jurídica, exercício) e limite de leitura.
2. Nunca inventar fontes, valores, datas ou decisões. Se não houver documento, escrever "não localizado nesta rodada".
3. Classificar cada caso com um dos badges: `badge--conden` (condenação criminal), `badge--civil` (civil/administrativa),
   `badge--inv` (investigação/relatório), `badge--pend` (pendente), `badge--enc` (arquivado/absolvido/prescrito).
4. Arquivamentos, absolvições e prescrições sempre aparecem ao lado da denúncia.
5. Não somar valores de entidades, moedas ou exercícios diferentes. Não apresentar "total desviado".
6. Não generalizar uma unidade para toda a denominação, nem uma denominação para todos os cristãos.
7. Links externos: `target="_blank" rel="noopener noreferrer"`.
8. Novas fichas de casos usam o componente `.ficha` com `data-tags` compatíveis com os filtros da página.

## Como adicionar um dossiê
1. Criar `<article class="ficha" id="dNN" data-tags="...">` em `src/pages/panorama.html` (ou `casos.html`).
2. Adicionar a fonte em `src/pages/fontes.html` com id, título, emissor, data e URL completa.
3. Rodar `python3 build.py` e conferir no navegador (desktop e 375px).
