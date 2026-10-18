from pathlib import Path
import json, shutil, html
BASE='https://ioditor.github.io/zero.github.io/'
root=Path(__file__).resolve().parent
data=json.loads((root/'content.json').read_text(encoding='utf-8'))
dest=root/'dist'
assert dest.resolve().parent == root.resolve() and dest.name == 'dist'
if dest.exists():
 for child in dest.iterdir():
  if child.is_dir(): shutil.rmtree(child)
  else: child.unlink()
shutil.copytree(root/'site',dest,dirs_exist_ok=True)
stems=['01-Poster','02-Type-Landscape','03-Pen-Landscape','04-Mind-Map','05-Hand-Drawn-Table','06-Diagram','07-Story-Showcase']
for lang,d in data.items():
 other='en' if lang=='ru' else 'ru'
 page='1' if lang=='ru' else '2'
 assets='../assets/'
 def image(i): return assets+'examples/'+stems[i]+'-'+lang.upper()+'.png'
 nav=''.join(f'<a href="#{id}">{text}</a>' for id,text in zip(['features','examples','download'],d['nav']))
 nav=nav.replace('<a href="#download">',f'<a href="#fonts">{d["fonts"]["nav"]}</a><a href="#download">')
 fonts=''.join(f'<article class="font-card"><div class="font-label"><h3>{html.escape(c[0])}</h3><p>{html.escape(c[1])}</p></div><p class="font-sample font-{key}">{html.escape(c[3])}</p><p class="font-alphabet font-{key}">{html.escape(c[4])}<br>0123456789</p><p class="font-description">{html.escape(c[2])}</p></article>' for key,c in zip(['flow','still','mono'],d['fonts']['cards']))
 feats=''.join(f'<article class="feature"><span class="number">0{i+1}</span><h3>{title}</h3><p>{text}</p></article>' for i,(title,text) in enumerate(d['features']))
 gallery=''.join(f'<figure class="art"><a href="{image(i)}" aria-label="{d["full"]}: {d["names"][i]}"><img src="{image(i)}" alt="{d["names"][i]} — {d["types"][i]}" width="1240" height="1754" loading="lazy"></a><figcaption><span class="number">0{i+1} / {d["types"][i]}</span><h3>{d["names"][i]}</h3></figcaption></figure>' for i,stem in enumerate(stems))
 output=f'''<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{d['title']}</title><meta name="description" content="{d['desc']}"><link rel="canonical" href="{BASE}{lang}/"><link rel="alternate" hreflang="ru" href="{BASE}ru/"><link rel="alternate" hreflang="en" href="{BASE}en/"><link rel="alternate" hreflang="x-default" href="{BASE}"><meta property="og:type" content="website"><meta property="og:title" content="{d['title']}"><meta property="og:description" content="{d['desc']}"><meta property="og:url" content="{BASE}{lang}/"><meta property="og:locale" content="{'ru_RU' if lang=='ru' else 'en_US'}"><meta property="og:image" content="{BASE}assets/examples/03-Pen-Landscape-{lang.upper()}.png"><meta name="twitter:card" content="summary_large_image"><link rel="icon" href="{assets}favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="{assets}site.css"><script src="{assets}site.js" defer></script></head>
<body><a class="skip" href="#main">{d['skip']}</a><header><div class="wrap bar"><a class="brand" href="./" aria-label="Zero"><span aria-hidden="true"></span>Zero</a><button class="menu" aria-expanded="false" aria-controls="navigation">{d['menu']}</button><nav id="navigation" aria-label="{d['menu']}">{nav}</nav><div class="langs"><a data-language="ru" href="../ru/" lang="ru" aria-label="Русский" {'aria-current="page"' if lang=='ru' else ''}>RU</a><a data-language="en" href="../en/" lang="en" aria-label="English" {'aria-current="page"' if lang=='en' else ''}>EN</a></div></div></header>
<main id="main" class="wrap"><section class="hero"><div><p class="eyebrow">{d['tag']}</p><h1>{d['headline']}</h1><p class="intro">{d['intro']}</p><div class="actions"><a class="button" href="#download">{d['cta']}</a><a href="#examples">{d['explore']}</a></div><p class="quiet">{d['platform']}</p></div><figure><a href="{image(2)}"><img src="{image(2)}" alt="{d['names'][2]}" fetchpriority="high"></a><figcaption>{d['hero']}</figcaption></figure></section>
<section class="section" id="features"><div class="heading"><div><p class="eyebrow">{d['ftag']}</p><h2>{d['fh']}</h2></div><p>{d['fp']}</p></div><div class="features">{feats}</div></section>
<section class="section" id="examples"><div class="heading"><div><p class="eyebrow">{d['gtag']}</p><h2>{d['gh']}</h2></div></div><div class="gallery">{gallery}</div></section>
<section class="section" id="fonts"><div class="heading"><div><p class="eyebrow">{d['fonts']['tag']}</p><h2>{d['fonts']['heading']}</h2></div><p>{d['fonts']['intro']}</p></div><div class="font-grid">{fonts}</div></section>
<section class="section" id="download"><div class="heading"><div><p class="eyebrow">{d['dtag']}</p><h2>{d['dh']}</h2></div></div><div class="download"><div><h3>{d['dtitle']}</h3><a class="button" href="https://github.com/ioditor/zero.github.io/releases">{d['release']}</a></div></div></section></main>
<footer class="wrap"><a class="brand" href="./">Zero</a><span>{d['footer']}</span><a href="https://github.com/ioditor/zero.github.io">{d['repo']}</a></footer></body></html>'''
 (dest/lang).mkdir();(dest/lang/'index.html').write_text(output,encoding='utf-8')
(dest/'index.html').write_text('''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Zero — Русский / English</title><meta name="description" content="Zero — a space for text and drawing. Выберите язык / Choose your language."><link rel="canonical" href="'''+BASE+'''"><link rel="alternate" hreflang="ru" href="'''+BASE+'''ru/"><link rel="alternate" hreflang="en" href="'''+BASE+'''en/"><link rel="alternate" hreflang="x-default" href="'''+BASE+'''"><link rel="stylesheet" href="assets/site.css"><link rel="icon" href="assets/favicon.svg"><script defer src="assets/entry.js"></script></head><body><main class="landing"><h1>Zero</h1><p>Выберите язык / Choose your language</p><a href="ru/" lang="ru">Русский →</a><a href="en/" lang="en">English →</a></main></body></html>''',encoding='utf-8')
(dest/'assets/entry.js').write_text("let choice;try{choice=localStorage.getItem('zero-language')}catch{}if(!['ru','en'].includes(choice))choice=navigator.language.toLowerCase().startsWith('ru')?'ru':'en';location.replace('./'+choice+'/'+location.hash);",encoding='utf-8')
(dest/'.nojekyll').touch()
(dest/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>'+BASE+p+'</loc></url>' for p in ['', 'ru/','en/'])+'</urlset>',encoding='utf-8')
(dest/'404.html').write_text('<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Zero — 404</title><h1>404</h1><p>Страница не найдена / Page not found</p><a href="'+BASE+'ru/">Русский</a> · <a href="'+BASE+'en/">English</a></html>',encoding='utf-8')
print('Built dist: RU + EN; base URL = '+BASE)
