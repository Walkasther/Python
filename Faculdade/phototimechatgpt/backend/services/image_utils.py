# app/image_utils.py
from PIL import Image, ImageEnhance, ImageFilter, ImageFont, ImageDraw
import os

def abrir_imagem(path):
    return Image.open(path).convert("RGB")

def aplicar_brilho(path_in, path_out, fator=1.2):
    img = abrir_imagem(path_in)
    enhancer = ImageEnhance.Brightness(img)
    img2 = enhancer.enhance(fator)
    img2.save(path_out, quality=95)

def aplicar_filtro_vintage(path_in, path_out):
    img = abrir_imagem(path_in)
    img = img.filter(ImageFilter.SMOOTH_MORE)
    # desaturar levemente
    enhancer = ImageEnhance.Color(img)
    img = enhancer.enhance(0.9)
    img.save(path_out, quality=95)

def cortar_proporcao(path_in, path_out, proporcao_w_h=(3,4)):
    img = abrir_imagem(path_in)
    w, h = img.size
    target_ratio = proporcao_w_h[0]/proporcao_w_h[1]
    current_ratio = w/h
    if current_ratio > target_ratio:
        # cortar largura
        novo_w = int(h * target_ratio)
        left = (w - novo_w) // 2
        box = (left, 0, left + novo_w, h)
    else:
        novo_h = int(w / target_ratio)
        top = (h - novo_h)//2
        box = (0, top, w, top + novo_h)
    img_crop = img.crop(box)
    img_crop.save(path_out, quality=95)

def inserir_texto(path_in, path_out, texto="PhotoTime", pos=(20,20), tamanho=48):
    img = abrir_imagem(path_in)
    draw = ImageDraw.Draw(img)
    # usar fonte embutida ou fornecer ttf
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", tamanho)
    draw.text(pos, texto, font=font, fill=(255,255,255))
    img.save(path_out, quality=95)

def preparar_para_impressao(path_in, path_out, dpi=300, largura_cm=None, altura_cm=None):
    img = abrir_imagem(path_in)
    if largura_cm and altura_cm:
        px_w = int(largura_cm/2.54 * dpi)
        px_h = int(altura_cm/2.54 * dpi)
        img = img.resize((px_w, px_h), Image.LANCZOS)
    img.save(path_out, dpi=(dpi,dpi), quality=95)
