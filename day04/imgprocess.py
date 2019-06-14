#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 06:44:41 2019

@author: vikram
"""

from PIL import Image
image_name=input('enter an image name>')
img=Image.open(image_name)
print (img.size)
img_rotate = img.transpose(Image.ROTATE_90)
img_rotate.show()  
img_rotate.save("sample.jpg")
print(img.width)
print(img.height)
crop_im = img.crop(box=(0, 20, 204, 160))
crop_im.save('sample.jpg')
print(img.width)
print(img.height)
img.thumbnail((75, 75))
print(img.width, img.height)
img.save('sample.jpg')
