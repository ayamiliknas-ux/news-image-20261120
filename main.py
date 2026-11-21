# news-image-20261120: draw a newspaper-style infographic of Nov 20 2026 world news
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
INK = (18, 18, 22)
PAPER = (246, 243, 235)
ACCENT = (156, 22, 22)
GOLD = (255, 210, 120)
FD = "/usr/share/fonts/truetype/dejavu/"
def F(name, size): return ImageFont.truetype(FD + name, size)

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)
f_title = F("DejaVuSans-Bold.ttf", 26)
f_date = F("DejaVuSerif-Bold.ttf", 42)
f_head = F("DejaVuSans-Bold.ttf", 27)
f_body = F("DejaVuSans.ttf", 18)
f_small = F("DejaVuSans.ttf", 15)
f_cap = F("DejaVuSans-Bold.ttf", 15)
f_big = F("DejaVuSans-Bold.ttf", 30)

def wrap(text, font, maxw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= maxw: cur = t
        else: lines.append(cur); cur = w
    if cur: lines.append(cur)
    return lines

def para(x, y, text, font, maxw, lh, color=INK, maxlines=99):
    lines = wrap(text, font, maxw)[:maxlines]
    for i, ln in enumerate(lines):
        d.text((x, y + i * lh), ln, font=font, fill=color)
    return y + lh * len(lines)

# Masthead
d.rectangle([0, 0, W, 118], fill=INK)
d.text((36, 12), "WORLD NEWS IN ONE PICTURE", font=f_title, fill=(240, 236, 226))
d.text((36, 46), "Friday, November 20, 2026", font=f_date, fill=(250, 248, 240))
d.line([0, 118, W, 118], fill=ACCENT, width=4)

y = 134
# Hero: trilateral summit aftermath — Russia's biggest overnight barrage on Ukraine
d.rectangle([36, y, 988, y + 216], fill=(28, 46, 84))
d.rectangle([36, y, 988, y + 8], fill=ACCENT)
d.text((52, y + 18), "KYIV · SHENZHEN", font=f_cap, fill=GOLD)
d.text((52, y + 44), "Russia unleashes huge overnight barrage on Ukraine", font=f_head, fill=(255, 255, 255))
d.text((52, y + 78), "days after Trump-Xi-Putin Shenzhen summit; Kyiv bridges", font=f_head, fill=(255, 255, 255))
d.text((52, y + 112), "hit, 8 killed — Ukraine had bombed the Kerch Bridge", font=f_head, fill=(255, 255, 255))
# simple glyphs: falling missiles + broken bridge
for mx, my in [(720, y+150), (760, y+130), (800, y+160)]:
    d.polygon([(mx, my), (mx+8, my+22), (mx-8, my+22)], fill=(230, 226, 214))
d.line([640, y+185, 930, y+185], fill=(230, 226, 214), width=5)
d.line([700, y+185, 700, y+165], fill=(230, 226, 214), width=5)
d.line([820, y+185, 820, y+165], fill=(230, 226, 214), width=5)
y += 232

# Two columns
colw = 452
x1, x2 = 36, 572
y1 = y2 = y
stories = [
    (x1, "THE HAGUE", "ICJ: Myanmar guilty of Rohingya genocide",
     "The UN's top court ruled Myanmar bears state responsibility for genocide against the Rohingya — a first against any state in its 80-year history. Judges voted 9-6 over the 2017 Rakhine crackdown."),
    (x2, "ANTALYA", "COP31 draft drops fossil fuel phase-out",
     "The slimmed-down Antalya declaration text stripped all mention of fossil fuels, sparking 'shame' chants from activists; EU-UK in Brussels struck a post-Brexit reset deal on food trade and youth mobility."),
]
for x, tag, head, body in stories:
    yy = y1 if x == x1 else y2
    d.rectangle([x, yy, x + 8, yy + 20], fill=ACCENT)
    d.text((x + 16, yy), tag, font=f_cap, fill=ACCENT)
    yy += 28
    for i, ln in enumerate(wrap(head, f_head, colw)[:2]):
        d.text((x, yy + i * 32), ln, font=f_head, fill=INK)
    yy += 70
    yy = para(x, yy, body, f_body, colw, 23, maxlines=6)
    if x == x1: y1 = yy + 12
    else: y2 = yy + 12

# Numbers strip
yy = max(y1, y2)
d.rectangle([36, yy, 988, yy + 66], fill=INK)
nums = [
    ("$48bn+", "cost of US war", "on Iran"),
    ("1,101", "Dow points lost,", "below 50,000"),
    ("$100", "Anthropic IPO,", "largest ever"),
]
for i, (n, l1, l2) in enumerate(nums):
    nx = 60 + i * 320
    d.text((nx, yy + 8), n, font=f_big, fill=GOLD)
    d.text((nx, yy + 42), l1 + " " + l2, font=f_small, fill=(220, 216, 206))
yy += 78

# World briefs
d.rectangle([36, yy, 988, yy + 26], fill=INK)
d.text((46, yy + 3), "ALSO FRIDAY", font=f_cap, fill=(250, 248, 240))
yy += 34
briefs = [
    "Wall St: Dow falls 1,101 points to close below 50,000; Anthropic's record IPO trades near $100.",
    "Iran war: Senate rejects war powers limits 51-48; cost tops $48bn; Trump: Tehran wants a deal.",
    "Saudi-led coalition strikes Hodeidah as Houthis threaten Saudi power plant and Riyadh targets.",
    "Estonia to shut Russian border Dec 1 after GRU-linked sabotage; Poland sirens over missile incursion.",
    "Trump fires national cyber director after global Microsoft outage grounded ~20,000 US flights.",
    "France: de Villepin enters 2027 race; 10,000 protest in Tokyo against Takaichi's defence shift.",
]
for b in briefs:
    d.ellipse([36, yy + 6, 44, yy + 14], fill=ACCENT)
    yy = para(54, yy, b, f_body, 920, 22, maxlines=1) + 5
yy += 16

# Bottom feature panel: Iran war / markets split
d.rectangle([36, yy, 500, yy + 120], fill=(120, 30, 30))
d.text((52, yy + 14), "IRAN WAR", font=f_cap, fill=GOLD)
para(52, yy + 38, "Senate blocks war powers limits 51-48; Iraq moves on militia stronghold; Hegseth visits Venezuela.", f_body, 430, 21, color=(250, 244, 236), maxlines=3)
d.rectangle([524, yy, 988, yy + 120], fill=(24, 84, 48))
d.text((540, yy + 14), "MARKETS & TECH", font=f_cap, fill=GOLD)
para(540, yy + 38, "Anthropic's record IPO trades near $100; Dow closes below 50,000 amid outages.", f_body, 430, 21, color=(250, 244, 236), maxlines=3)
yy += 132

# Footer ticker
d.rectangle([0, H - 44, W, H], fill=INK)
d.text((36, H - 32), "NOV 20 2026 · UKRAINE BARRAGE · ICJ MYANMAR GENOCIDE RULING · COP31 FOSSIL-FUEL DRAFT · EU-UK RESET · DOW -1101",
       font=f_small, fill=(210, 206, 196))

import os
out = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "out"), "entry.png")
os.makedirs(os.environ.get("MAKEFUN_OUTPUT_DIR", "out"), exist_ok=True)
img.save(out)
print("saved", out, img.size)
