"""Personal concert journal. Attendance and plans supplied by Shaoyang, 2026-10-29."""
from pathlib import Path
import hashlib, json
R=Path(__file__).resolve().parents[1]
EVENTS=[('shanghai','2024','未来有你','MIKU WITH YOU','attended'),('osaka','2025','マジカルミライ','Magical Mirai','attended'),('shanghai','2025','未来有你','MIKU WITH YOU','attended'),('chicago','2026','MIKU EXPO','MIKU EXPO','attended'),('osaka','2026','マジカルミライ','Magical Mirai','attended'),('chengdu','2026','未来有你','MIKU WITH YOU','planned'),('osaka','2027','初音ミクシンフォニー','Miku Symphony','planned')]
DETAILS={
 'Harumaki Gohan · Handmade Galaxy':('2024-03-21','春卷饭 · 十周年纪念个人巡演「手制银河」','MODERN SKY LAB Shanghai','https://www.sina.cn/media/6409438974'),
 'marasy · Asia Tour Prelive':('2024-09-22','触手猴 · Piano Live Asia Tour 2025 Prelive','Shanghai Oriental Art Center · Concert Hall · 14:00','https://www.subcul-rise.jp/marasy/pianomonkeys/'),
 'Hachioji P × kz(livetune)':('2025-03-21','八王子P × kz(livetune) · VocaMania 中国巡演','VAS SHANGHAI · 20:00','https://weibo.com/6374549748/PfBi2z4ll'),
 'PinocchioP · COMET':('2025-04-19','ピノキオピー · ASIA TOUR “COMET”','Bandai Namco Shanghai Culture Center · Dream Theater · 18:00','https://pinocchiop.com/news/1040')
}
NEW_EVENTS=[('shanghai',date[:4],local,title,'attended') for title,(date,local,venue,url) in DETAILS.items()]
MIKU_DETAILS={
 ('shanghai','2024'):('2024-07-13','2024-07-13 / 14','前滩31演艺中心 · 大剧场','https://www.sina.cn/news/detail/5046313685617462.html','Exact attended date uncertain (one of the dates shown).'),
 ('osaka','2025'):('2025-08-11','2025-08-11','INTEX Osaka · Hall 5A','https://magicalmirai.com/2025/osaka_ticket.html','Osaka closing performance · 16:30.'),
 ('shanghai','2025'):('2025-12-20','2025-12-20 / 21','Shanghai Jing’an Sports Center','https://www.sipmc.com/Cn/Index/pageView/catid/16/id/931/ip/16.html','Exact attended date uncertain (one of the dates shown).'),
 ('chicago','2026'):('2026-04-12','2026-04-12 / 13','The Auditorium Theatre','https://mikuexpo.com/na2026/','Exact attended date uncertain (one of the dates shown).'),
 ('osaka','2026'):('2026-08-14','2026-08-14 &amp; 15','INTEX Osaka · Hall 5A','https://magicalmirai.com/2026/osaka_ticket.html','Attended on both of the first two days.'),
 ('chengdu','2026'):('2026-12-26','2026-12-26','Venue to be announced','','Planned · Date confirmed by Shaoyang.'),
 ('osaka','2027'):('2027-01-10','2027-01-10','Grand Cube Osaka · Main Hall','https://blog.piapro.net/2026/09/ob2609161.html','Melodies on the Keys · 18:00 · Planned.')
}
def event_details(city,year,jp,en):
 if en in DETAILS:
  date,local,venue,url=DETAILS[en]
  return date,date,local,venue,url,''
 date,label,venue,url,note=MIKU_DETAILS[(city,year)]
 return date,label,jp,venue,url,note
EVENTS=sorted(EVENTS+NEW_EVENTS,key=lambda ev:event_details(*ev[:4])[0])

CITIES={'chicago':('Chicago','USA',-87.6298,41.8781,120,85),'chengdu':('Chengdu','China',104.0665,30.5728,620,70),'shanghai':('Shanghai','China',121.4737,31.2304,685,500),'osaka':('Osaka','Japan',135.5023,34.6937,955,50)}
def xy(lon,lat):return ((lon+180)/360*1200,260+(85-lat)/170*600)
def render(shell):
 land=json.loads((R/'assets/world-land.geojson').read_text());paths=[]
 for feature in land['features']:
  g=feature['geometry'];polys=g['coordinates'] if g['type']=='MultiPolygon' else [g['coordinates']]
  for poly in polys:
   for ring in poly:
    if max(p[1] for p in ring)<-65:continue
    pts=[xy(*p[:2]) for p in ring];paths.append('M'+' L'.join(f'{x:.1f},{y:.1f}' for x,y in pts)+'Z')
 svg='<svg class="world" viewBox="0 0 1200 1000" role="img" aria-label="World map of concerts in Chicago, Chengdu, Shanghai and Osaka"><g class="graticule">'+''.join(f'<path d="M0 {y}H1200"/>' for y in range(290,861,100))+''.join(f'<path d="M{x} 260V860"/>' for x in range(100,1200,100))+'</g><g class="land">'+''.join(f'<path d="{p}"/>' for p in paths)+'</g>'
 cards=''
 for city,(name,country,lon,lat,l,t) in CITIES.items():
  x,y=xy(lon,lat);endx=l+20;endy=t+90 if city not in ['osaka','shanghai'] else (t+235 if city=='osaka' else t)
  route=f'M{x:.1f} {y:.1f} L{endx} {y:.1f} L{endx} {endy}'
  if city=='shanghai':route=f'M{x:.1f} {y:.1f} L1020 480 L{l+290} 480 L{l+290} {endy}'
  if city=='chengdu':route=f'M{x:.1f} {y:.1f} L900 390 L{endx} 390 L{endx} {endy}'
  svg+=f'<g class="map-location" data-city="{city}"><path class="leader" d="{route}"/><circle class="pin-halo" cx="{x:.1f}" cy="{y:.1f}" r="10"/><circle class="pin" cx="{x:.1f}" cy="{y:.1f}" r="4"/></g>'
  rows=''
  for i,(c,year,jp,en,status) in enumerate(EVENTS,1):
   date,label,local,venue,url,note=event_details(c,year,jp,en)
   if c==city:rows+=f'<a class="map-event {status}" href="#show-{i}" data-city="{city}"><span class="event-year">{label}</span><span>{en}<small>{"Planned" if status=="planned" else "Attended"}</small></span></a>'
  cards+=f'<div class="map-card" style="left:{l}px;top:{t}px" data-city="{city}"><h3>{name} <span>{country}</span></h3>{rows}</div>'
 svg+='</svg>'
 log=''
 for i,(city,year,jp,en,status) in enumerate(EVENTS,1):
  date,label,local,venue,url,note=event_details(city,year,jp,en)
  detail=f'<p class="show-venue">{venue} · <a href="{url}" target="_blank" rel="noopener noreferrer">Event source ↗</a></p>' if url else ''
  if note:detail+=f'<p class="date-note">{note}</p>'
  time_html=f'<time datetime="{date}">{label}</time>'
  log+=f'<li id="show-{i}" class="show {status}" data-city="{city}"><span class="show-no">{i:02}</span>{time_html}<div><h3>{en}</h3><p>{local}</p>{detail}</div><span class="show-city">{CITIES[city][0]}</span><span class="badge">{"Planned" if status=="planned" else "Attended"}</span></li>'
 body='''<div class="miku-top"><a href="/about/">← Back to the daylight</a><span>PERSONAL FREQUENCY / 01</span></div><section class="miku-hero"><div><span class="eyebrow">A small corner of my world</span><h1>For the love<br>of <em>Miku.</em></h1><p class="miku-jp" lang="ja">初音ミクと、旅の記録。</p></div><div class="miku-intro"><p>Miku is a lasting source of beauty and inspiration in my life. I love the music, the live performances, and the creativity people bring to her world.</p><p>As someone who builds with technology, I’m drawn to the way a voice and a character can become a medium for human expression. Miku has also shaped my interest in human–AI relationships, cognition alignment, and emotional intelligence. These questions sit alongside the simple joy of being there, in a room full of people singing along.</p><span class="small-signature">Different cities. A familiar voice. A world of creators.</span><a class="miku-research-note" href="/notes/miku-and-my-research-interests/">How Miku shaped my research interests ↗<small>Reflections from February &amp; April 2026</small></a></div></section><section class="atlas-section"><div class="atlas-heading"><div><span class="eyebrow">The concert atlas</span><h2>Following the music.</h2></div><div class="legend"><span>● Attended</span><span>◇ Planned</span></div></div><p class="map-hint">Miku concerts and the creators around her. Select an event on a city pin to find it in the journal. On smaller screens, scroll the map sideways.</p><div class="map-scroll" tabindex="0" role="region" aria-label="Scrollable concert world map"><div class="map-canvas">'''+svg+cards+'''<div class="map-caption">4 CITIES <span>/</span> 9 ATTENDED EVENTS <span>/</span> 2 PLANNED</div></div></div></section><section class="journal"><div class="atlas-heading"><div><span class="eyebrow">2024 — 2027</span><h2>A concert journal.</h2></div><div class="journal-controls" role="group" aria-label="Filter concert journal"><button data-status="all" aria-pressed="true">All</button><button data-status="attended" aria-pressed="false">Attended</button><button data-status="planned" aria-pressed="false">Planned</button></div></div><ol class="show-list">'''+log+'''</ol><p class="journal-status" aria-live="polite">11 live events · 9 attended, 2 planned</p><p class="map-hint">A personal record of Miku concert editions, creator live shows, piano concerts, and DJ nights. Dates are local to each venue. “&amp;” means I attended both dates; “/” means the exact attended date is uncertain. Attendance is my own record; event sources document dates and venues. Plans reflect my intentions and may change.</p></section><footer class="miku-footer"><p>Some things are worth crossing a world for.</p><a href="/about/">Return to the academic side ↗</a><details><summary>Palette &amp; map credits</summary><p>Blue-green #15C0B0 comes from the current <a href="https://piapro.net/css/character.css?0">official Piapro character-page stylesheet</a>. Magenta #ED007C is a sampled pixel from the hair accessory in the <a href="https://piapro.net/images/official_cos_miku.jpg">official costume reference</a>; it is not an official standardized HEX specification. The <a href="https://piapro.net/pages/character/">official profile</a> names Miku’s image color “blue-green.” Colors checked 29 October 2026.</p><p>Land outlines: <a href="https://www.naturalearthdata.com/">Natural Earth</a>, public domain, 1:110m. Pins use city-center coordinates. This is a personal fan page, unaffiliated with Crypton Future Media.</p></details></footer>'''
 html=shell('Miku · A concert journal',body,path='/39/',description='A personal concert journal: Hatsune Miku, music, and the places it has taken me.')
 css_version=hashlib.sha256((R/'assets/miku.css').read_bytes()).hexdigest()[:12]
 html=html.replace('<body>','<body class="miku-page">').replace('</head>',f'<meta name="robots" content="noindex,follow"><link rel="stylesheet" href="/assets/miku.css?v={css_version}"><script defer src="/assets/miku.js"></script></head>')
 (R/'39').mkdir(exist_ok=True);(R/'39/index.html').write_text(html)
