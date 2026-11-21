import glob
import re
import os

html_files = sorted(glob.glob('*.html'))
print(f'Total HTML files: {len(html_files)}')

broken_links = []
images_found = []
images_missing = []

for hf in html_files:
    with open(hf, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check internal links
    links = re.findall(r'href=[\"\']([a-zA-Z0-9_\-]+\.html)[\"\']', content)
    for link in links:
        if not os.path.exists(link):
            broken_links.append((hf, link))
            
    # Check site images
    matches = re.finditer(r'<img[^>]+src=[\"\']([^\"\']+)[\"\'][^>]+alt=[\"\']([^\"\']+)[\"\']', content)
    for m in matches:
        src = m.group(1).strip()
        alt = m.group(2).strip()
        images_found.append({
            'page': hf,
            'src': src,
            'alt': alt
        })
        if not os.path.exists(src):
            images_missing.append((hf, src))

print(f'Broken internal links: {len(broken_links)}')
if broken_links:
    for src, tgt in broken_links:
        print(f'  {src} -> {tgt}')

print(f'Total image elements across site: {len(images_found)}')
print(f'Missing image files on disk: {len(images_missing)}')
if images_missing:
    for hf, src in images_missing:
        print(f'  Missing in {hf}: {src}')

unique_srcs = sorted(set(img['src'] for img in images_found))
print(f'Unique image sources: {len(unique_srcs)}')
for u in unique_srcs:
    size_kb = os.path.getsize(u) / 1024 if os.path.exists(u) else 0
    print(f'  - {u} ({size_kb:.1f} KB)')

# Also check if any old placeholders remain
old_placeholders = 0
for hf in html_files:
    with open(hf, 'r', encoding='utf-8') as f:
        if 'img-placeholder' in f.read():
            old_placeholders += 1
print(f'Pages with remaining old placeholders: {old_placeholders}')
