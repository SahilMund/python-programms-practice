# working with color of image
from PIL import Image as i
from PIL import ImageEnhance as E
import os
img1=i.open('pix1.jpg')
enchancer=E.Color(img1)
enchancer.enhance(6).save('pix_coloered_clr.jpg')
'''enhance method takes input as number and according to this number,the color will decide'''
#0:black n white
# 1:ORIGINAL IMAGE
#2:image with chnage in color
# 3,4 .......... ==> diff coloered
