import glob, re

files = sorted(
    glob.glob('knowledge/**/*.md', recursive=True) +
    glob.glob('articles/synthesis/*.md')
)
for f in files:
    if '/index.md' in f or 'README' in f or '.md/' in f:
        continue
    import os
    if os.path.isdir(f):
        continue
    with open(f) as fh:
        content = fh.read()
    if 'description:' not in content:
        m = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', content, re.MULTILINE)
        title = m.group(1).strip('"\'') if m else '(no title)'
        print(f'{f}|{title}')
