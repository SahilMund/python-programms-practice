#to work with brightness with python
from PIL import Image as i
from PIL import ImageEnhance as E
import os
img1=i.open('pix1.jpg')
enchancer=E.Brightness(img1)
enchancer.enhance(2).save('pix_brightened.jpg')
'''enhance method takes input as number and according to this number,the sharpness will decide'''
