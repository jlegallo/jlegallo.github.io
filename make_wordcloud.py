import re
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

with open("publications.qmd", encoding="utf-8") as f:
    raw_text = f.read()

# Only process the "By Type" section to avoid duplicates from the "By Theme" tab
by_type_section = raw_text.split("## By Theme")[0]

def strip_md_link(s):
    """[text](url) → text, *text* → text"""
    s = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', s)
    s = re.sub(r'\*([^*]+)\*', r'\1', s)
    return s.strip()

entries = []   # (year, title)
seen = set()

for line in by_type_section.splitlines():
    line = line.strip()
    if not line.startswith("-"):
        continue

    # Skip edited books (contain "(Eds.)" or "(contributor)")
    if "(Eds.)" in line or "(contributor)" in line:
        continue

    yr_match = re.search(r'\((\d{4})\)', line)
    forth = "forthcoming" in line.lower()
    year = int(yr_match.group(1)) if yr_match else (2025 if forth else None)
    if year is None:
        continue

    title = None

    # Book chapter: title is between "). " and ". In ["  or  ". In *"
    m = re.search(r'\)\.\s+(.+?)\.\s+In\s+[\[\*]', line)
    if m:
        title = strip_md_link(m.group(1))
    else:
        # Article with linked title immediately after year
        m = re.search(r'\)\.\s+\[([^\]]+)\]\(https?://', line)
        if not m:
            m = re.search(r'forthcoming\)[^[]*\[([^\]]+)\]\(https?://', line)
        if m:
            title = m.group(1).strip()
        else:
            # Article without link: text between "). " and ". *Journal*"
            m = re.search(r'\)\.\s+([^\[\*]+?)\.\s+\*', line)
            if m:
                title = m.group(1).strip()

    if title and title not in seen:
        seen.add(title)
        entries.append((year, title))

print(f"Total unique titles: {len(entries)}")

# Weight: >=2020 ×6, 2015-2019 ×3, <2015 ×1
def weight(year):
    if year >= 2020: return 6
    elif year >= 2015: return 3
    else: return 1

weighted = []
for year, title in entries:
    weighted.extend([title] * weight(year))

corpus = " ".join(weighted)

stopwords = set(STOPWORDS)
stopwords.update([
    # English function words
    'a', 'an', 'the', 'of', 'in', 'on', 'at', 'to', 'for', 'with', 'by',
    'from', 'and', 'or', 'but', 'as', 'is', 'are', 'was', 'were', 'be',
    'been', 'has', 'have', 'had', 'its', 'their', 'this', 'that', 'these',
    'those', 'not', 'do', 'does', 'vs', 'versus', 'some', 'more', 'most',
    'other', 'new', 'between', 'across', 'among', 'under', 'over', 'when',
    'how', 'what', 'which', 'where', 'toward', 'towards', 'beyond', 'during',
    'since', 'after', 'before', 'about', 'around', 'through', 'whether',
    'without', 'within', 'into', 'upon', 'per',
    # French function words
    'et', 'de', 'du', 'des', 'les', 'le', 'la', 'un', 'une', 'sur', 'au',
    'aux', 'dans', 'par', 'pour', 'avec', 'que', 'qui', 'à', 'en', 'ou',
    'est', 'ses', 'nos', 'leur', 'leurs', 'vers', 'entre',
    # Generic academic filler
    'using', 'revisiting', 'assessing', 'evaluating', 'exploring', 'examining',
    'investigating', 'testing', 'measuring', 'estimating', 'identifying',
    'analysis', 'analyses', 'approach', 'approaches', 'introduction',
    'review', 'overview', 'case', 'evidence', 'study', 'note', 'comment',
    'recent', 'further', 'additional', 'method', 'methods', 'methodology',
    'application', 'applications', 'based', 'comparison', 'comparative',
    'empirical', 'theoretical', 'role', 'effects', 'effect', 'impact',
    'impacts', 'determinants', 'drivers', 'factors', 'challenges', 'issues',
    'perspective', 'perspectives', 'contribution', 'contribution', 'grand',
])

# Custom color: spatial → dark navy, convergence-related → pale blue
DARK_BLUE  = np.array(mcolors.to_rgb('#1a3560'))
LIGHT_BLUE = np.array(mcolors.to_rgb('#a8cfe8'))
BLUES = ['#2166ac', '#3182bd', '#4393c3', '#6baed6', '#9ecae1']

def color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    w = word.lower()
    if w == 'spatial':
        r, g, b = (DARK_BLUE * 255).astype(int)
    elif w in ('regional', 'convergence', 'regions', 'disparities',
               'european', 'europe', 'gdp', 'productivity'):
        r, g, b = (LIGHT_BLUE * 255).astype(int)
    else:
        c = np.array(mcolors.to_rgb(BLUES[abs(hash(word)) % len(BLUES)]))
        r, g, b = (c * 255).astype(int)
    return f"rgb({r},{g},{b})"

# Elliptical mask: 0 = word zone, 255 = background
W, H = 1400, 700
ys, xs = np.ogrid[:H, :W]
mask = np.where(
    ((xs - W/2) / (W/2 * 0.97))**2 + ((ys - H/2) / (H/2 * 0.97))**2 <= 1,
    0, 255
).astype(np.uint8)

wc = WordCloud(
    mask=mask,
    background_color=None,
    mode="RGBA",
    color_func=color_func,
    stopwords=stopwords,
    min_font_size=11,
    max_words=120,
    prefer_horizontal=0.85,
    collocations=False,
).generate(corpus)

plt.figure(figsize=(14, 7), facecolor='none')
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.tight_layout(pad=0)
plt.savefig('images/wordcloud_publications.png', dpi=150, bbox_inches='tight',
            transparent=True)
print(f"Image saved — {len(entries)} titles, {len(weighted)} weighted")
