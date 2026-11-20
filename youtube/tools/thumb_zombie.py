import sys, random, math
from PIL import Image, ImageDraw, ImageFilter, ImageFont
src, out, text = sys.argv[1], sys.argv[2], sys.argv[3]
W, H = 1280, 720
random.seed(7)
SKIN = (241, 201, 165, 255)

# --- Kobi: shocked face edit ---
k = Image.open(src).convert("RGBA")
d = ImageDraw.Draw(k)
d.rectangle([160, 184, 320, 205], fill=SKIN)            # remove old eyebrows
d.rectangle([205, 258, 278, 292], fill=SKIN)            # remove smile
d.line([(165, 186), (215, 176)], fill=(38, 32, 29, 255), width=15)   # raised brows
d.line([(265, 176), (315, 186)], fill=(38, 32, 29, 255), width=15)
d.ellipse([222, 255, 260, 300], fill=(90, 45, 35, 255))  # open mouth
d.ellipse([230, 282, 252, 298], fill=(200, 90, 90, 255)) # tongue
for cx in (192, 290):                                    # bigger pupils/eyes white
    d.ellipse([cx-24, 198, cx+24, 246], fill=(255, 255, 255, 255))
    d.ellipse([cx-11, 211, cx+11, 233], fill=(38, 32, 29, 255))
    d.ellipse([cx-4, 214, cx+3, 221], fill=(255, 255, 255, 255))
bbox = k.getchannel("A").getbbox(); k = k.crop(bbox)
kh = 600; k = k.resize((int(k.width * kh / k.height), kh), Image.LANCZOS)

# --- background ---
img = Image.new("RGBA", (W, H))
px = img.load(); HZ = 440
for y in range(H):
    for x in range(W):
        if y < HZ:
            t = y / HZ; base = (int(8 + 10*t), int(12 + 18*t), int(32 + 30*t))
            red = max(0.0, 1 - (math.hypot((x - 120) / 650, (y - HZ) / 300)))  # burning glow left
            px[x, y] = (min(255, int(base[0] + 210*red**1.6)), int(base[1] + 40*red**2), int(base[2] + 10*red), 255)
        else:
            t = (y - HZ) / (H - HZ)
            px[x, y] = (int(6 + 6*t), int(28 - 10*t), int(52 - 20*t), 255)
d = ImageDraw.Draw(img)
for _ in range(90):                                       # stars on the calm side
    x, y = random.randint(740, W), random.randint(0, 380); r = random.choice([1, 1, 2])
    d.ellipse([x-r, y-r, x+r, y+r], fill=(230, 235, 255, 255))
glow = Image.new("RGBA", (W, H), (0, 0, 0, 0)); g = ImageDraw.Draw(glow)
g.ellipse([560, 20, 740, 200], fill=(255, 250, 220, 120)); glow = glow.filter(ImageFilter.GaussianBlur(30))
img = Image.alpha_composite(img, glow); d = ImageDraw.Draw(img)
d.ellipse([605, 65, 695, 155], fill=(250, 246, 225, 255))           # moon
for i in range(14):                                                    # moon reflection
    y = HZ + 20 + i*18; w = 70 - i*3
    d.line([(650 - w, y), (650 + w, y)], fill=(200, 210, 230, 120), width=3)
# distant shore (Java) with city silhouettes
d.polygon([(0, 510), (0, 420), (60, 405), (140, 412), (260, 400), (380, 418), (470, 440), (560, 510)], fill=(20, 10, 18, 255))
for x0, w, h in [(30, 26, 60), (70, 20, 90), (100, 34, 50), (150, 22, 110), (185, 30, 70), (230, 18, 95), (260, 40, 55), (320, 24, 75)]:
    d.rectangle([x0, 410 - h, x0 + w, 412], fill=(25, 12, 20, 255))
    for wy in range(410 - h + 8, 405, 14):
        if random.random() < .5: d.rectangle([x0+5, wy, x0+9, wy+5], fill=(255, 150, 60, 255))
# zombies on the shore, arms forward toward the island
def zombie(x, y, s):
    c = (110, 200, 90, 255); lw = max(3, int(5*s))
    d.ellipse([x-9*s, y-62*s, x+9*s, y-44*s], fill=c)
    d.ellipse([x+1*s, y-56*s, x+5*s, y-52*s], fill=(230, 30, 30, 255))
    d.line([(x, y-44*s), (x, y-18*s)], fill=c, width=lw)
    d.line([(x, y-36*s), (x+24*s, y-38*s)], fill=c, width=lw)
    d.line([(x, y-32*s), (x+22*s, y-30*s)], fill=c, width=lw)
    d.line([(x, y-18*s), (x-8*s, y)], fill=c, width=lw)
    d.line([(x, y-18*s), (x+9*s, y)], fill=c, width=lw)
for x, y, s in [(60, 500, 1.9), (160, 505, 2.1), (265, 498, 1.8), (370, 506, 2.2), (470, 502, 2.0)]:
    zombie(x, y, s)
# island + palm
d.ellipse([720, 590, 1290, 760], fill=(214, 182, 120, 255))
d.ellipse([720, 590, 1290, 640], fill=(232, 205, 145, 255))
d.line([(1215, 640), (1200, 540), (1180, 440)], fill=(110, 75, 40, 255), width=18)
for ang, ln in ((-170, 120), (-140, 110), (-100, 90), (-45, 110), (-10, 120), (25, 100), (160, 100)):
    a = math.radians(ang); pts = []
    for i in range(12):
        f = i / 11; pts.append((1180 + ln*f*math.cos(a), 440 + ln*f*math.sin(a) + 55*f*f))
    d.line(pts, fill=(40, 140, 70, 255), width=20, joint="curve")
# Kobi on the island
img.alpha_composite(k, (960 - k.width//2, 640 - kh))
# text
font = ImageFont.truetype("/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf", 175 if len(text) <= 6 else 130)
d = ImageDraw.Draw(img)
lines = text.split("|"); y = 70
for ln in lines:
    d.text((50, y), ln, font=font, fill=(255, 214, 0, 255), stroke_width=12, stroke_fill=(0, 0, 0, 255))
    y += font.size + 10
img.convert("RGB").save(out, quality=95)
print("saved", out)
