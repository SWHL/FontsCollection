#!/usr/bin/env python
# coding: utf-8
from pathlib import Path

from tqdm import tqdm
from PIL import Image, ImageFont, ImageDraw


text = '！@#￥%……&*（）《》？睚眦狻猊负螭吻'

font_path = Path(r'C:\Users\xxx\Desktop\hand_write')

save_img_dir = 'images'
if not Path(save_img_dir).exists():
    Path(save_img_dir).mkdir(parents=True, exist_ok=True)

for font_type in tqdm(font_path.iterdir()):
    img = Image.new('RGBA', (1500, 200), color=(255, 255, 255))

    font = ImageFont.truetype(str(font_type), 50)

    draw = ImageDraw.Draw(img)
    draw.text((10, 30), text, fill=(0, 0, 0), font=font)

    img.save(f'{save_img_dir}/{font_type.stem}.png')

