from pathlib import Path
import shutil
r=Path(__file__).resolve().parents[1]
d=r/'dist'
if d.exists(): shutil.rmtree(d)
d.mkdir()
for name in ['index.html','404.html','robots.txt','sitemap.xml','assets','about','cv','notes','publications','research','projects','39']:
 p=r/name
 if p.is_dir(): shutil.copytree(p,d/name)
 else: shutil.copy2(p,d/name)
print('Prepared static deployment.')
