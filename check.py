from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import json,hashlib
root=Path(__file__).resolve().parent;dist=root/'dist'
class Page(HTMLParser):
 def __init__(self,text):
  super().__init__();self.refs=[];self.ids=set();self.images=[];self.feed(text)
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a: self.ids.add(a['id'])
  for k in ['href','src']:
   if k in a:self.refs.append(a[k])
  if tag=='img':self.images.append(a)
pages={p:Page(p.read_text(encoding='utf-8')) for p in dist.rglob('*.html')}
count=0
for p,page in pages.items():
 for ref in page.refs:
  u=urlsplit(ref)
  if u.scheme or u.netloc:continue
  assert not u.path.startswith('/'),(p,ref,'root-absolute URL breaks project Pages')
  target=(p.parent/unquote(u.path)).resolve() if u.path else p.resolve()
  if target.is_dir():target=target/'index.html'
  assert target.is_file(),(p,ref)
  if u.fragment and target.suffix=='.html':assert u.fragment in pages[target].ids,(p,ref)
  count+=1
for lang in ['ru','en']:
 p=dist/lang/'index.html';t=p.read_text(encoding='utf-8');page=pages[p]
 assert f'<html lang="{lang}">' in t
 assert len(page.images)==8
 assert all('-'+lang.upper()+'.png' in im['src'] for im in page.images)
 assert 'https://ioditor.github.io/zero.github.io/'+lang+'/' in t
 assert 'https://github.com/ioditor/zero.github.io/releases' in t
 assert 'aria-controls="navigation"' in t
for item in json.loads((root/'material-manifest.json').read_text(encoding='utf-8')):
 p=dist/'assets/examples'/item['file']
 assert hashlib.sha256(p.read_bytes()).hexdigest()==item['sha256'],p
print(f'PASS: {count} internal references; 2 locales; 14 localized gallery images; all original material hashes.')

# Webfont assets, localized specimens and project-relative CSS resources.
import re
css=dist/'assets/site.css'
for ref in re.findall(r'url\(["\']?([^"\')]+)',css.read_text(encoding='utf-8')):
 assert not urlsplit(ref).scheme and not ref.startswith('/'),ref
 assert (css.parent/ref).is_file(),ref
for item in json.loads((root/'font-manifest.json').read_text(encoding='utf-8')):
 p=dist/'assets/fonts'/item['webfont']
 assert p.read_bytes()[:4]==b'wOF2'
 assert hashlib.sha256(p.read_bytes()).hexdigest()==item['webfont_sha256']
assert not list(dist.rglob('*.ttf'))
for lang in ['ru','en']:
 t=(dist/lang/'index.html').read_text(encoding='utf-8')
 assert t.count('class="font-card"')==3
 assert 'id="fonts"' in t and 'href="#fonts"' in t
 assert ('Мысль начинается' if lang=='ru' else 'A thought begins') in t
print('PASS: 3 local WOFF2 assets, CSS paths, hashes, RU/EN font specimens; no TTF.')

for lang in ['ru','en']:
 t=(dist/lang/'index.html').read_text(encoding='utf-8')
 assert 'id="paper"' in t and 'href="#paper"' in t
 assert f'../assets/paper/Zero-Brochure-{lang.upper()}-folds.pdf' in t
 assert (dist/f'assets/paper/Zero-Brochure-{lang.upper()}-folds.pdf').read_bytes().startswith(b'%PDF-')
print('PASS: RU/EN Paper section and localized PDFs.')
