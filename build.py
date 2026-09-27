#!/usr/bin/env python3
"""Build the English static homepage for GitHub Pages."""
from html import escape
from hashlib import sha256
from pathlib import Path
from shutil import copy2
from urllib.parse import quote
import content as c

ROOT = Path(__file__).resolve().parent
DIST = ROOT / 'dist'
ICON_PATHS = {
    'education': '<path d="m2 8 10-5 10 5-10 5Z"/><path d="M6 10v6c4 3 8 3 12 0v-6M22 8v7"/>',
    'publications': '<path d="M12 5v15M3 4c3-1 6 0 9 1 3-1 6-2 9-1v15c-3-1-6 0-9 1-3-1-6-2-9-1Z"/>',
    'manuscripts': '<path d="M13 3H5v18h14v-8M10 14l1-4 8-8 3 3-8 8Z"/>',
    'projects': '<rect x="3" y="4" width="18" height="16" rx="2"/><path d="m8 9 3 3-3 3m6 0h3"/>',
    'awards': '<circle cx="12" cy="8" r="5"/><path d="m8 12-2 9 6-3 6 3-2-9"/>',
    'teaching': '<path d="M3 3h18v13H3ZM12 16v5m-4 0h8M7 8h5M7 11h9"/>',
    'activities': '<circle cx="9" cy="7" r="3"/><path d="M3 21v-3a6 6 0 0 1 12 0v3M16 4a3 3 0 0 1 0 6m2 4a5 5 0 0 1 3 4v3"/>',
    'mail': '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m4 6 8 7 8-7"/>',
    'file': '<path d="M14 3H5v18h14V8ZM14 3v5h5M8 13h8m-8 4h6"/>',
    'external': '<path d="M14 3h7v7m0-7L10 14M10 5H4v15h15v-6"/>',
}
SECTIONS = [
    ('education', ('教育背景', 'Education')),
    ('publications', ('论文发表', 'Publications')),
    ('manuscripts', ('在投论文', 'Manuscripts under review')),
    ('projects', ('项目经历', 'Projects')),
    ('awards', ('获奖情况', 'Awards')),
    ('teaching', ('教学经历', 'Teaching')),
    ('activities', ('社团和志愿活动', 'Activities')),
]

def local(value, lang):
    return value[lang] if isinstance(value, (tuple, list)) else value

def icon(name, extra_class=''):
    return f'<svg class="icon {extra_class}" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">{ICON_PATHS[name]}</svg>'

def entry(item, lang):
    title = escape(local(item['title'], lang))
    if item.get('url'):
        title = f'<a href="{escape(item["url"], quote=True)}">{title}</a>'
    body = f'<div class="entry-heading"><h3>{title}</h3><span class="date">{escape(local(item["date"], lang))}</span></div>'
    if item.get('role'):
        body += f'<p class="role">{escape(local(item["role"], lang))}</p>'
    if item.get('metadata'):
        body += f'<p class="metadata">{local(item["metadata"], lang)}</p>'
    if item.get('text'):
        body += f'<p>{local(item["text"], lang)}</p>'
    if item.get('bullets'):
        body += '<ul class="details">' + ''.join(f'<li>{local(b, lang)}</li>' for b in item['bullets']) + '</ul>'
    return f'<article class="entry">{body}</article>'

def author(name):
    label = escape(name)
    if name == 'Haigang Zhou':
        return f'<strong>{label}</strong>'
    url = c.AUTHOR_URLS.get(name)
    if url:
        return f'<a href="{escape(url, quote=True)}">{label}</a>'
    return label

def papers(category, lang):
    result = []
    for paper in c.PAPERS:
        if paper['category'] != category:
            continue
        title = escape(paper['title'])
        if paper.get('arxiv'):
            title = f'<a href="https://arxiv.org/abs/{paper["arxiv"]}">{title}</a>'
        authors = ', '.join(author(a) for a in paper['authors'])
        link = f'<a class="paper-link" href="https://arxiv.org/abs/{paper["arxiv"]}">{icon("external")}arXiv:{paper["arxiv"]}</a>' if paper.get('arxiv') else ''
        result.append(f'<article class="entry paper"><div class="entry-heading"><h3 lang="en">{title}</h3><span class="date">2026</span></div><p class="authors" lang="en">{authors}</p><p class="venue">{local(paper["status"], lang)}{link}</p></article>')
    return ''.join(result)

def rows(items, lang):
    result = []
    for item in items:
        label = f'<strong>{escape(local(item["title"], lang))}</strong>'
        if item.get('organization'):
            label += f', {escape(local(item["organization"], lang))}'
        if item.get('role'):
            label += f' · <span class="role">{escape(local(item["role"], lang))}</span>'
        result.append(f'<li><span>{label}</span><span class="date">{escape(local(item["date"], lang))}</span></li>')
    return '<ul class="rows">' + ''.join(result) + '</ul>'

def render(lang=1):
    tr = lambda value: local(value, lang)
    prefix = './'
    style_version = sha256((ROOT / 'assets/style.css').read_bytes()).hexdigest()[:12]
    cv_version = sha256((ROOT / 'assets/CV_HaigangZhou_en_US.pdf').read_bytes()).hexdigest()[:12]
    content = {
        'education': ''.join(entry(e, lang) for e in c.EDUCATION),
        'publications': '<p class="author-note">Paper authors are listed alphabetically by surname.</p>' + papers('publications', lang),
        'manuscripts': papers('manuscripts', lang),
        'projects': ''.join(entry(e, lang) for e in c.PROJECTS),
        'awards': rows(c.AWARDS, lang),
        'teaching': ''.join(entry(e, lang) for e in c.TEACHING),
        'activities': rows(c.ACTIVITIES, lang),
    }
    sections = ''.join(f'<section id="{key}" aria-labelledby="{key}-title"><h2 id="{key}-title">{icon(key, "section-icon")}{tr(title)}</h2>{content[key]}</section>' for key, title in SECTIONS)
    intro = '<div class="intro">' + ''.join(f'<p>{paragraph}</p>' for paragraph in c.INTRO) + '</div>'
    name = 'Haigang Zhou'
    description = tr(('周海刚，南京大学计算机科学与技术博士生。论文、项目和教学经历。', 'Haigang Zhou, Ph.D. student in Computer Science and Technology at Nanjing University. Publications, projects, and teaching.'))
    favicon = quote('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 40 40"><rect width="40" height="40" rx="6" fill="#244f80"/><text x="20" y="28" text-anchor="middle" font-family="Arial,sans-serif" font-size="23" fill="white">Z</text></svg>')
    return f'''<!doctype html>
<html lang="{tr(('zh-CN', 'en'))}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{escape(description, quote=True)}">
  <meta name="color-scheme" content="light">
  <title>Haigang Zhou · 周海刚</title>
  <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,{favicon}">
  <link rel="preload" href="{prefix}assets/name-wenkai.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="{prefix}assets/style.css?v={style_version}">
</head>
<body>
  <a class="skip-link" href="#main">{tr(('跳到正文', 'Skip to content'))}</a>
  <div class="page" id="top">
    <header class="profile">
      <div class="identity"><h1><span>{name}</span><span class="native-name" lang="zh-CN">周海刚</span></h1>
        <p class="affiliation">{tr(('南京大学 · 计算机科学与技术博士生', 'Ph.D. Student · Computer Science and Technology'))}</p>
      </div>
      <div class="contact"><span class="email">{icon('mail')}{escape(c.EMAIL_DISPLAY)}</span><a href="{c.GITHUB}"><img class="icon github-logo" src="{prefix}assets/logos/github.svg" alt="" width="16" height="16">GitHub / loftea</a>
        <div class="downloads"><a href="{prefix}assets/CV_HaigangZhou_en_US.pdf?v={cv_version}" download>{icon('file')}Curriculum vitae (PDF)</a></div>
      </div>
    </header>
    <div class="layout">
      <main id="main" tabindex="-1">{intro}{sections}</main>
    </div>
    <footer><span>© {c.UPDATED[:4]} Haigang Zhou</span><span>{tr(('更新于', 'Updated'))} <time datetime="{c.UPDATED}">{c.UPDATED.replace('-', '.')}</time></span><a href="#top">{tr(('返回顶部', 'Back to top'))} ↑</a></footer>
  </div>
</body>
</html>
'''

def build():
    (DIST / 'assets').mkdir(parents=True, exist_ok=True)
    (DIST / 'index.html').write_text(render(), encoding='utf-8')
    for name in ('style.css',):
        copy2(ROOT / 'assets' / name, DIST / 'assets' / name)
    for name in ('SourceSans3-Regular.otf', 'SourceSans3-Semibold.otf', 'SourceSans3-RegularIt.otf', 'SourceSans3-SemiboldIt.otf', 'LICENSE.txt', 'name-wenkai.woff2', 'wenkai-OFL.txt', 'FONT-SOURCES.txt'):
        copy2(ROOT / 'assets' / 'fonts' / name, DIST / 'assets' / name)
    (DIST / 'assets' / 'logos').mkdir(exist_ok=True)
    for name in ('github.svg',):
        copy2(ROOT / 'assets' / 'logos' / name, DIST / 'assets' / 'logos' / name)
    name = 'CV_HaigangZhou_en_US.pdf'
    copy2(ROOT / 'assets' / name, DIST / 'assets' / name)
    (DIST / '.nojekyll').touch()
    print(f'Built English homepage in {DIST}')

if __name__ == '__main__':
    build()
