"""English personal homepage content, aligned with the current CV."""

UPDATED = '2026-09-27'

EMAIL_DISPLAY = 'hgzhou2003 at outlook.com'

GITHUB = 'https://github.com/loftea'

ADVISOR = 'http://penghuiyao.info/'

AUTHOR_URLS = {
    'Yangjing Dong': 'https://yangjingdong.com/',
    'Li Gao': 'https://sites.google.com/site/ligaomath/home',
    # No verified personal homepage; use the matching DBLP author profile.
    'Fengning Ou': 'https://dblp.org/pid/407/4287.html',
    'Penghui Yao': 'https://penghuiyao.info/',
    'Minglong Qin': 'https://tsdjh.github.io/',
    'Mingnan Zhao': 'https://mingnanzh.github.io/',
}

INTRO = [
    'I am a Ph.D. student in the <a href="https://tcs.nju.edu.cn/">Theoretical Computer Science (TCS) group</a> at Nanjing University, '
    f'supervised by <a href="{ADVISOR}">Prof. Penghui Yao</a>. My research interests are '
    'quantum computing, quantum information, and quantum complexity theory.',
    'I am also interested in large language models (LLM) and AI for Science. In 2025, I interned at '
    '<a href="https://www.minimax.io/">MiniMax</a>, '
    'where I contributed to training <a href="https://arxiv.org/abs/2506.13585">MiniMax-M1</a>, '
    'focusing on supervised fine-tuning and reinforcement learning for mathematical reasoning. '
    'I was also invited as a company representative to attend '
    '<a href="https://worldaic.com.cn/">WAIC 2025</a> '
    '(<a href="https://sheitc.sh.gov.cn/zxxx/20250728/974925ba5f954a68bc0278a9e7601d4b.html">'
    'news coverage</a>).',
    'Outside of research, I enjoy photography and learning languages. I am currently learning '
    'Japanese and French. Thanks to AI, I never run out of ways to learn and practice! '
    'I have also written a reusable AI-agent skill for building a Japanese learning website, '
    'available in my <a href="https://github.com/loftea/jp-study-site">Japanese Study Studio project</a>.',
]

EDUCATION = [{'title': 'Nanjing University',
  'date': 'Sep. 2023 — Present',
  'role': 'Ph.D. Student in Computer Science and Technology',
  'metadata': 'Advisor: <a href="http://penghuiyao.info/">Prof. Penghui Yao</a>'},
 {'title': 'Tsinghua University',
  'date': 'Sep. 2019 — June 2023',
  'role': 'B.S. in Mathematics and Applied Mathematics'}]

PAPERS = [{'title': 'Dimension-Free Approximate Tensorization of Quantum Hypercontractivity for Qudit Depolarizing '
           'Semigroups',
  'authors': ['Yangjing Dong', 'Li Gao', 'Fengning Ou', 'Penghui Yao', 'Haigang Zhou'],
  'status': 'AQIS 2026 · IEEE TIT (under review)',
  'year': 2026,
  'arxiv': '2606.17729',
  'category': 'publications'},
 {'title': 'Fooling Thresholds of Halfspaces',
  'authors': ['Minglong Qin', 'Penghui Yao', 'Mingnan Zhao', 'Haigang Zhou'],
  'status': 'SODA 2027 (under review)',
  'year': 2026,
  'arxiv': '2609.21329',
  'category': 'manuscripts'},
 {'title': 'MiniMax-M1: Scaling Test-Time Compute Efficiently with Lightning Attention',
  'authors': ['MiniMax Team'],
  'status': 'Technical report',
  'year': 2025,
  'arxiv': '2506.13585',
  'category': 'technical-reports'}]

PROJECTS = [{'title': 'Japanese Study Studio',
  'url': 'https://github.com/loftea/jp-study-site',
  'date': 'Sep. 2026',
  'role': 'Personal Project · Python / JavaScript',
  'text': 'Developed a local AI Japanese learning site in Python and JavaScript, integrating Codex CLI and '
          'Anki’s native review scheduling through AnkiConnect. Implemented interactive tutoring, persistent '
          'cross-session memory, and structured storage for learning records, textbooks, and supplementary '
          'reading materials.'}]

AWARDS = [{'title': 'Outstanding Graduate Student', 'organization': 'Nanjing University', 'date': 'Dec. 2025'},
 {'title': 'President’s Scholarship', 'organization': 'Nanjing University', 'date': 'Oct. 2023'},
 {'title': 'Research Innovation Award', 'organization': 'Department of Mathematical Sciences, Tsinghua University', 'date': 'Mar. 2023'},
 {'title': 'Second Prize', 'organization': 'Chinese Mathematics Competitions for College Students (Major Group)', 'date': 'Mar. 2020'},
 {'title': 'Silver Prize', 'organization': 'CMO (Chinese Mathematical Olympiad Winter Camp)', 'date': 'Dec. 2018'}]

TEACHING = [{'title': 'Computational Complexity',
  'institution': 'Nanjing University',
  'date': 'Spring 2026',
  'metadata': 'Teaching Assistant · Instructor: <a href="http://penghuiyao.info/">Prof. Penghui Yao</a>'},
 {'title': 'Foundations of Data Science',
  'institution': 'Nanjing University',
  'date': 'Fall 2025',
  'metadata': 'Teaching Assistant · Instructor: <a '
          'href="https://njusz.nju.edu.cn/55/c6/c53016a742854/page.htm">Assoc. Prof. Mingmou Liu</a>'},
 {'title': 'Quantum Computing Talent Development Program',
  'institution': 'USTC',
  'date': 'Summer 2025',
  'metadata': 'Mentor · Program Lead: <a '
          'href="https://faculty.ustc.edu.cn/zfsu/zh_CN/kyxm/990249/content/21787.htm">Assoc. Researcher '
          'Zhaofeng Su</a>'},
 {'title': 'Information Theory',
  'institution': 'Nanjing University',
  'date': 'Spring 2025, 2024',
  'metadata': 'Teaching Assistant · Instructor: <a href="http://penghuiyao.info/">Prof. Penghui Yao</a>'}]

ACTIVITIES = [{'title': 'Photography Association of Nanjing University', 'role': 'President', 'date': 'June 2025 — Present'},
 {'title': 'Students International Exchanges & Cooperation Association (SIECA), Nanjing University',
  'role': 'Member', 'date': 'Aug. 2024 — Jan. 2026'},
 {'title': 'Linguistic Association of Tsinghua University', 'role': 'Management', 'date': 'Mar. 2021 — Oct. 2021'}]
