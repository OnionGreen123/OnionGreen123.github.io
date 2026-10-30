#!/usr/bin/env python3
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import re, sys
ROOT=Path(__file__).resolve().parents[1]
class Page(HTMLParser):
 def __init__(self,text):
  super().__init__();self.ids=[];self.links=[];self.h1=0;self.title=False;self.desc=False;self.images=[];self.feed(text)
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.append(a['id'])
  if tag=='h1':self.h1+=1
  if tag=='title':self.title=True
  if tag=='meta' and a.get('name')=='description':self.desc=True
  if tag=='img':self.images.append(a)
  for k in ('href','src'):
   if a.get(k):self.links.append(a[k])
files=[p for p in ROOT.rglob('*.html') if not any(x in p.parts for x in ['.git','.openai','dist'])]
parsed={p:Page(p.read_text()) for p in files};errors=[];count=0
for p,obj in parsed.items():
 if obj.h1!=1:errors.append(f'{p}: expected one h1')
 if len(obj.ids)!=len(set(obj.ids)):errors.append(f'{p}: duplicate IDs')
 if not obj.title or not obj.desc:errors.append(f'{p}: missing metadata')
 for im in obj.images:
  if not im.get('alt'):errors.append(f'{p}: missing image alt')
 for link in obj.links:
  u=urlsplit(link)
  if u.scheme or u.netloc:continue
  path=unquote(u.path)
  target=(ROOT/path.lstrip('/')) if path.startswith('/') else (p.parent/path if path else p)
  if target.is_dir():target=target/'index.html'
  if not target.exists():errors.append(f'{p.relative_to(ROOT)}: broken local link {link}')
  if u.fragment and target in parsed and u.fragment not in parsed[target].ids:errors.append(f'{p}: broken anchor {link}')
  count+=1
 text=p.read_text()
 for pattern in [r'[a-z0-9-]+\.chatgpt\.site/login',r'\b[a-z]+-admin\b',r'overleaf\.com/project',r'\b\d{3}-\d{3}-\d{4}\b',r'(?i)password\s*=',r'(?i)aggregate result slots',r'(?i)activation offsets']:
  if re.search(pattern,text):errors.append(f'{p}: nonpublic content marker')
try:
 import fitz
 pdf=fitz.open(ROOT/'assets/Shaoyang_Zhang_CV.pdf')
 if len(pdf)!=1:errors.append('Public CV should have exactly one page')
 for page in pdf:
  text=page.get_text()
  for private in ['null-space','target latent','overleaf.com']:
   if private in text:errors.append('Nonpublic content in CV')
except ImportError:print('PDF check skipped: install PyMuPDF for PDF checks')
if errors:print('\n'.join(errors));sys.exit(1)
print(f'PASS: {len(files)} HTML pages; {count} local links/assets; unique IDs, anchors, image alt text, metadata, and public-content checks.')
