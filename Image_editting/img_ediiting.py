#editiing of images
from PIL import Image

img1=Image.open('pix1.jpg')
#converting the .jpg extension of image to .png
img1.save('pix2.png')   
#converting the .jpg extension of image to .pdf
img1.save('pix3.pdf')
#for showing the image
img1.show()

#resizing of image file:
max_size=(250,250)
img1.thumbnail(max_size)
img1.save('pix_1.jpg')
