from PIL import Image,ImageDraw,ImageFont
from pathlib import Path
p=Path(__file__).resolve().parents[1]
w,h=1800,680
im=Image.new('RGB',(w,h));pix=im.load()
for y in range(h):
 for x in range(w):
  glow=max(0,1-((x-1380)**2+(y-280)**2)**.5/950)
  pix[x,y]=(int(9+3*glow),int(17+14*glow),int(31+22*glow))
d=ImageDraw.Draw(im)
for x in range(1020,1800,65):d.line((x,0,x,h),fill=(20,38,55))
for y in range(0,h,65):d.line((1020,y,1800,y),fill=(20,38,55))
a=Image.open(p/'assets/scene.png').convert('RGBA');a.thumbnail((870,740));im.paste(a,(950,-5),a)
f='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf';b='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf';mono='/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'
def t(x,y,s,size,color,font=f):d.text((x,y),s,font=ImageFont.truetype(font,size),fill=color)
d.rounded_rectangle((80,75,422,120),radius=22,fill=(18,44,59),outline=(30,82,99));d.ellipse((101,92,111,102),fill=(70,221,213));t(126,86,'DEVELOPER / BUILDER',20,(127,224,229),mono)
t(76,171,'CHANDAN',83,(240,246,255),b);t(76,262,'KUMAR',83,(240,246,255),b)
t(82,383,'Full-Stack Developer',34,(91,221,232))
t(82,446,'Thoughtful interfaces.',27,(169,187,207));t(82,487,'Practical software.',27,(169,187,207))
d.line((82,569,162,569),fill=(70,215,230),width=4);t(183,552,'REACT  /  TYPESCRIPT  /  NEXT.JS',21,(147,169,194),mono)
im.save(p/'assets/hero.webp',quality=92,method=6)
print('Saved',p/'assets/hero.webp')
