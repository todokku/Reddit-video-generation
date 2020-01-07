# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont
from math import ceil
font_type = ImageFont.truetype(r'C:\Windows.old.000\Windows\Fonts\verdana.ttf', 25)

images=[]
def drawImage(x, author, comments_parts ,y_location):
    for i in range(len(comments_parts)):
        if i==0:
            image = Image.new('RGB', (1280,720), color =(24,25,26))
            draw = ImageDraw.Draw(image)
            draw.text(xy=(100,y_location - 40), text=author, fill =(89,161,210), font=font_type) 
            draw.text(xy=(100,y_location + 40*i), text=comments_parts[i], fill =(211,233,233), font=font_type)
            image.save(r'C:\Users\wong\part' + str(x) + '-' + str(i) +'.jpg')
        elif i>0:
            image = Image.open('part'+ str(x) + '-' + str(i-1) +'.jpg')
            draw = ImageDraw.Draw(image)
            draw.text(xy=(100,y_location + 40*i), text=comments_parts[i], fill =(211,233,233), font=font_type)
            image.save(r'C:\Users\wong\part' + str(x) + '-' + str(i) +'.jpg')
            
            
