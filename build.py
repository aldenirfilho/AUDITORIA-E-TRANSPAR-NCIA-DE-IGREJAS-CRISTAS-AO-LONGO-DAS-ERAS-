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
    ("index", "Início", "Auditoria e transparência de igrejas cristãs ao longo das eras",
     "Investigação documental sobre dízimos, destino dos recursos, impacto social e casos judiciais envolvendo instituições cristãs, 1926–2026. Fontes primárias, limites explícitos e método público."),
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
     "Lista completa de documentos primários citados no projeto, com links diretos, emissor e data."),
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
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' fill='%231f1b17'/%3E%3Ctext x='16' y='22' font-family='Georgia,serif' font-size='18' text-anchor='middle' fill='%23f3efe6'%3EA%3C/text%3E%3C/svg%3E">
<link rel="preconnect" href="https://api.fontshare.com">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://api.fontshare.com/v2/css?f[]=zodiak@400,500,700&f[]=satoshi@400,500,700&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="./base.css">
<link rel="stylesheet" href="./style.css">
</head>
<body>
<a class="skip-link" href="#conteudo">Ir para o conteúdo</a>
<header class="header">
  <div class="wrap header__inner">
    <a class="brand" href="./index.html">
      <span class="brand__mark">Auditoria de Igrejas</span>
      <span class="brand__sub">1926–2026 · projeto cívico</span>
    </a>
    <button class="nav-toggle" aria-expanded="false" aria-controls="nav" aria-label="Abrir menu">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg>
    </button>
    <nav class="nav" id="nav" aria-label="Principal">
{nav}
    </nav>
  </div>
</header>
<main id="conteudo">
"""

FOOT = """</main>
<footer class="footer">
  <div class="wrap footer__grid">
    <div>
      <span class="brand__mark">Auditoria de Igrejas Cristãs</span>
      <p style="margin-top:var(--space-3);max-width:52ch">Projeto cívico e social de investigação documental. Cada número vem acompanhado da fonte primária, do perímetro que cobre e do que ele não demonstra. Última revisão das pesquisas: 18 de outubro de 2026.</p>
      <p style="margin-top:var(--space-3)"><a href="https://github.com/aldenirfilho/AUDITORIA-E-TRANSPAR-NCIA-DE-IGREJAS-CRISTAS-AO-LONGO-DAS-ERAS-" target="_blank" rel="noopener noreferrer">Repositório no GitHub</a> · Autor: Aldenir Rocha de Oliveira Filho</p>
    </div>
    <div>
      <p class="kicker" style="color:var(--color-text-muted)">Eixos</p>
      <ul>
        <li><a href="./dizimos.html">Para onde vai o dízimo</a></li>
        <li><a href="./impacto.html">Impacto social e ambiental</a></li>
        <li><a href="./casos.html">Fé, dinheiro e enriquecimento</a></li>
        <li><a href="./panorama.html">Trinta dossiês, 1926–2026</a></li>
      </ul>
    </div>
    <div>
      <p class="kicker" style="color:var(--color-text-muted)">Apoio</p>
      <ul>
        <li><a href="./metodo.html">Método e critérios</a></li>
        <li><a href="./metodo.html#pedido">Modelo de pedido de informação</a></li>
        <li><a href="./fontes.html">Todas as fontes</a></li>
      </ul>
    </div>
  </div>
  <div class="wrap" style="margin-top:var(--space-10);padding-top:var(--space-5);border-top:1px solid var(--color-border)">
    <p class="xs">Nada aqui constitui acusação criminal, parecer jurídico ou auditoria contábil das transações individuais. Arquivamentos, absolvições e prescrições são registrados ao lado de cada denúncia. Ausência de dado publicado não é evidência de desvio.</p>
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
        page = HEAD.format(title=html.escape(title), desc=html.escape(desc), nav=nav_html(slug)) + body + FOOT
        (ROOT / f"{slug}.html").write_text(page, encoding="utf-8")
        print("ok", slug)


if __name__ == "__main__":
    main()
