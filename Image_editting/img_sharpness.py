#to work with sharpness with python
from PIL import Image as i
from PIL import ImageEnhance as E
import os
img1=i.open('pix1.jpg')
enchancer=E.Sharpness(img1)
enchancer.enhance(4).save('pix_sharpened.jpg')
'''enhance method takes input as number and according to this number,the sharpness will decide'''
#0:blurry
# 1:ORIGINAL IMAGE
#2:image with increase sharpness
# 3,4 .......... ==> more sharpened 
