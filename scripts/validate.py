#!/usr/bin/env python3
"""Verifica integridade do site, arquivos gerados, links e acervo visual."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
from collections import Counter
import hashlib
import importlib.util
import json

ROOT = Path(__file__).resolve().parents[1]
errors = []
spec = importlib.util.spec_from_file_location('site_build', ROOT / 'build.py')
build = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build)

class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids=[]; self.links=[]; self.assets=[]; self.headings=0; self.articles=0
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if 'id' in a:self.ids.append(a['id'])
        if tag=='h1':self.headings+=1
        if tag=='article':self.articles+=1
        if tag=='a' and a.get('href'):self.links.append(a)
        if tag in ('script','img') and a.get('src'):self.assets.append(a['src'])
        if tag=='link' and a.get('rel') in ('stylesheet','icon'):self.assets.append(a.get('href',''))
        if tag=='img' and not a.get('alt'):errors.append('Imagem sem alternativa de texto')

pages={}
for slug,_,title,desc in build.PAGES:
    path=ROOT/(slug+'.html')
    parser=Page(); text=path.read_text(); parser.feed(text); pages[path.name]=parser
    expected=build.HEAD.format(title=build.html.escape(title),desc=build.html.escape(desc),nav=build.nav_html(slug),slug=slug)+(build.SRC/(slug+'.html')).read_text()+build.FOOT
    if text!=expected:errors.append(f'{path.name}: arquivo gerado diverge da fonte; rode build.py')
    if parser.headings!=1:errors.append(f'{path.name}: quantidade de h1 {parser.headings}')
    duplicates=[x for x,n in Counter(parser.ids).items() if n>1]
    if duplicates:errors.append(f'{path.name}: IDs duplicados {duplicates}')
    if 'truncated for brevity' in text or 'Footer content as before' in text:errors.append(f'{path.name}: marcador de truncamento')
for name,page in pages.items():
    for a in page.links:
        href=a['href']; u=urlsplit(href)
        if u.scheme in ('http','https'):
            if a.get('target')=='_blank' and not {'noopener','noreferrer'}.issubset(set(a.get('rel','').split())):errors.append(f'{name}: rel inseguro {href}')
        elif not u.scheme:
            target=ROOT/unquote(u.path or name)
            if not target.exists():errors.append(f'{name}: link ausente {href}')
            elif u.fragment and target.name in pages and unquote(u.fragment) not in pages[target.name].ids:errors.append(f'{name}: âncora ausente {href}')
    for src in page.assets:
        if not urlsplit(src).scheme and not (ROOT/unquote(src)).is_file():errors.append(f'{name}: asset ausente {src}')
cases=json.loads((ROOT/'src/data/investigacoes.json').read_text())['cases']
if len(cases)!=8 or pages['investigacoes.html'].articles!=8:errors.append('Acervo novo: esperado oito casos')
if len({c['id'] for c in cases})!=8:errors.append('Dossiês com IDs repetidos')
for c in cases:
    if not c.get('sources') or not c.get('defense') or not c.get('limits'):errors.append(f'Dossiê incompleto: {c["id"]}')
images=json.loads((ROOT/'src/data/imagens.json').read_text())
if len(images)!=10 or pages['imagens.html'].articles!=10:errors.append('Coleção: esperado dez imagens')
for row in images:
    path=ROOT/'assets/profanico'/row['file']; web=path.with_suffix('.jpg')
    if hashlib.sha256(path.read_bytes()).hexdigest()!=row['sha256']:errors.append(f'Hash divergente: {path.name}')
    if web.stat().st_size>250*1024:errors.append(f'JPEG acima de 250 KiB: {web.name}')
    if not path.read_bytes().startswith(b'\x89PNG\r\n\x1a\n'):errors.append(f'PNG inválido: {path.name}')
    if not web.read_bytes().startswith(b'\xff\xd8'):errors.append(f'JPEG inválido: {web.name}')
if pages['panorama.html'].articles!=30 or pages['casos.html'].articles!=10:errors.append('Contagem do acervo histórico alterada')
if errors:
    raise SystemExit('\n'.join(errors))
print(f'OK: {len(pages)} páginas sincronizadas; links, âncoras e assets locais íntegros; 8 dossiês; 10 imagens e hashes válidos; JPEGs ≤250 KiB.')
