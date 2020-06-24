
#for converting all .jpg format file to .png format
#editiing of images
from PIL import Image
import os

img1=Image.open('pix1.jpg')

for item in os.listdir():
    if item.endswith('.jpg'):
        img1=Image.open(item)
        filename,extension=os.path.splitext(item)
        img1.save(f'{filename}.png')


