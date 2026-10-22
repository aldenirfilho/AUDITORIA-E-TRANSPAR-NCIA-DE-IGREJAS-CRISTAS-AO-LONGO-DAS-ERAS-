#!/usr/bin/env python3
"""Monta as páginas finais (raiz do repositório) a partir de src/pages/*.html.

Uso: python3 build.py
Cada arquivo em src/pages contém apenas o <main>; o cabeçalho, a navegação e o rodapé
são injetados aqui. Metadados (título, descrição) ficam em PAGES.
"""
from pathlib import Path
import html

ROOT = Path(__file__).parent
SRC = ROOT / "src" / "pages"

PAGES = [
    ("index", "Início", "Fé não é cheque em branco | Transparência 360 X",
     "Fé respeitada. Poder fiscalizado. Investigações documentais sobre dinheiro, corrupção e prestação de contas em instituições cristãs. Edição Turbo TEMI 360X."),
    ("cenario-atual", "Cenário 2026", "Igrejas evangélicas no Brasil: cenário atual",
     "Dimensão social, regime jurídico, imunidade tributária, riscos de governança, lacunas de transparência e prioridades de auditoria das organizações evangélicas brasileiras."),
    ("agentes", "Agentes 360", "Arquitetura de agentes | Auditoria Religiosa 360",
     "Quatorze agentes para catalogação institucional, auditoria financeira, investigação judicial, impacto social, contraditório e controle de qualidade."),
    ("investigacoes", "Investigações", "Dinheiro sob investigação | Dossiês 360 X",
     "Novos dossiês sobre fraude, desvio e governança: decisões, documentos oficiais, contraditório e limites de cada caso. Fiscalizar instituições é respeitar quem acredita."),
    ("imagens", "Imagens", "Turbo X Profânico | 10 imagens sobre fé, dinheiro e poder",
     "Coleção de 10 ilustrações editoriais com IA. Frases diretas, contraste e metáforas visuais sobre transparência. Respeito aos fiéis e crítica ao abuso de poder."),
    ("dizimos", "Dízimos", "Para onde vai o dinheiro dos dízimos",
     "Balanços publicados por Mitra de São Paulo, IPB, Uniões adventistas, Óbolo de São Pedro, Fundo de Solidariedade de Fortaleza, Santos dos Últimos Dias e Universal: valores, categorias de despesa e limites de leitura."),
    ("impacto", "Impacto", "Destino dos recursos e potencial de impacto",
     "Quanto chega a assistência, educação e meio ambiente; agências auditadas; simulação de vidas e hectares por real realocado, com premissas e limites."),
    ("casos", "Fé e dinheiro", "Fé, dinheiro e enriquecimento pessoal",
     "Dez fichas de casos com condenação criminal, responsabilidade civil ou investigação encerrada: Dourados, Osório Lopes, Fogueira Santa, Regalado, Bakker, Fay, Valdemiro, Padre Robson, Renascer e Universal."),
    ("panorama", "100 anos", "Panorama 1926–2026: trinta dossiês",
     "Trinta dossiês sobre instituições cristãs em um século: abusos, finanças, tributos, crime organizado. Situação processual de cada caso e o que cada valor realmente representa."),
    ("metodo", "Método", "Método de auditoria cívica",
     "Critérios, documentos a exigir, matriz de afirmações e provas, erros a evitar, glossário jurídico e modelo de pedido de informação."),
    ("fontes", "Fontes", "Fontes e documentos",
     "Fontes primárias, institucionais e jornalísticas citadas no projeto, com links diretos, emissor e data."),
]

HEAD = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — Auditoria de Igrejas Cristãs</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:locale" content="pt_BR">
<meta name="theme-color" content="#101217">
<meta property="og:image" content="https://aldenirfilho.github.io/AUDITORIA-E-TRANSPAR-NCIA-DE-IGREJAS-CRISTAS-AO-LONGO-DAS-ERAS-/assets/capa-transparencia-360x.jpg">
<meta property="og:image:alt" content="Ilustração editorial de arquitetura e documentos financeiros sob luz vermelha">
<link rel="canonical" href="https://aldenirfilho.github.io/AUDITORIA-E-TRANSPAR-NCIA-DE-IGREJAS-CRISTAS-AO-LONGO-DAS-ERAS-/{slug}.html">
<link rel="icon" href="./assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="./base.css">
<link rel="stylesheet" href="./style.css">
<link rel="stylesheet" href="./turbo.css">
</head>
<body data-page="{slug}">
<a class="skip-link" href="#conteudo">Ir para o conteúdo</a>
<div class="edition-bar"><div class="wrap edition-bar__inner"><span><i aria-hidden="true"></i> INDEPENDÊNCIA EDITORIAL · EDIÇÃO 360 X</span><a href="./metodo.html#pacto">Fé respeitada. Poder fiscalizado. ↗</a></div></div>
<header class="header">
  <div class="wrap header__inner">
    <a class="brand" href="./index.html">
      <span class="brand__icon" aria-hidden="true">360<span>X</span></span>
      <span><span class="brand__mark">TRANSPARÊNCIA</span><span class="brand__sub">Igrejas · dinheiro · poder</span></span>
    </a>
    <button class="nav-toggle" aria-expanded="false" aria-controls="nav" aria-label="Abrir menu">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg>
    </button>
    <nav class="nav" id="nav" aria-label="Principal">
{nav}
    </nav>
  </div>
</header>
<div class="reading-progress" aria-hidden="true"><span></span></div>
<main id="conteudo">
"""

FOOT = """</main>
<footer class="footer">
  <div class="wrap footer__grid">
    <div>
      <span class="brand__mark">FÉ RESPEITADA.<br>PODER FISCALIZADO.</span>
      <p style="margin-top:var(--space-4);max-width:52ch">Auditoria e Transparência de Igrejas Cristãs. Projeto cívico de investigação documental. A crítica recai sobre atos, decisões e estruturas de poder; a dignidade dos fiéis é inegociável.</p>
      <p class="xs" style="margin-top:var(--space-3)">Turbo TEMI 360X · Edição revisada em 22 de outubro de 2026. Cada ficha informa a data do documento que sustenta seu status. A data da edição não certifica atualização integral de todos os processos.</p>
      <p style="margin-top:var(--space-3)"><a href="https://github.com/aldenirfilho/AUDITORIA-E-TRANSPAR-NCIA-DE-IGREJAS-CRISTAS-AO-LONGO-DAS-ERAS-" target="_blank" rel="noopener noreferrer">Repositório no GitHub</a> · Autor: Aldenir Rocha de Oliveira Filho</p>
    </div>
    <div>
      <p class="kicker" style="color:var(--color-text-muted)">Eixos</p>
      <ul>
        <li><a href="./cenario-atual.html">Cenário atual 2026</a></li>
        <li><a href="./agentes.html">Arquitetura de agentes 360</a></li>
        <li><a href="./investigacoes.html">Novas investigações documentadas</a></li>
        <li><a href="./dizimos.html">Para onde vai o dízimo</a></li>
        <li><a href="./impacto.html">Impacto social e ambiental</a></li>
        <li><a href="./casos.html">Fé, dinheiro e enriquecimento</a></li>
        <li><a href="./panorama.html">Trinta dossiês, 1926–2026</a></li>
        <li><a href="./auditoria-evangelica-360/">Auditoria Evangélica Brasil 360</a></li>
      </ul>
    </div>
    <div>
      <p class="kicker" style="color:var(--color-text-muted)">Apoio</p>
      <ul>
        <li><a href="./metodo.html#pacto">Pacto editorial e correções</a></li>
        <li><a href="./metodo.html#protecao">Proteção contra exploração financeira</a></li>
        <li><a href="./metodo.html#pedido">Modelo de pedido de informação</a></li>
        <li><a href="./fontes.html">Todas as fontes</a></li>
      </ul>
    </div>
  </div>
  <div class="wrap" style="margin-top:var(--space-10);padding-top:var(--space-5);border-top:1px solid var(--color-border)">
    <p class="xs">Pesquisa documental pública, com fontes rastreáveis. Não substitui auditoria contábil nem decisão judicial. Arrecadação, patrimônio, prejuízo e multa têm significados distintos. Ausência de dado publicado não é evidência de desvio.</p>
  </div>
</footer>
<script src="./app.js" defer></script>
</body>
</html>
"""


def nav_html(current):
    out = []
    for slug, label, _, _ in PAGES:
        cur = ' aria-current="page"' if slug == current else ""
        out.append(f'      <a href="./{slug}.html"{cur}>{html.escape(label)}</a>')
    return "\n".join(out)


def main():
    for slug, label, title, desc in PAGES:
        body = (SRC / f"{slug}.html").read_text(encoding="utf-8")
        page = HEAD.format(title=html.escape(title), desc=html.escape(desc), nav=nav_html(slug), slug=slug) + body + FOOT
        (ROOT / f"{slug}.html").write_text(page, encoding="utf-8")
        print("ok", slug)


if __name__ == "__main__":
    main()
