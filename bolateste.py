#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 10:44:23 2017

@author: luiz
"""

from skimage import io
import matplotlib.pyplot as plt
import numpy as np

image = io.imread("jogobola1.jpg")

print(image.shape)

lin,col,prof = image.shape

img2 = np.zeros((lin,col,prof),'uint8')
img3 =np.zeros((lin,col,prof),'uint8')

filtro = np.zeros((3,3))
filtro = filtro/9

print(image.shape)
lin,col,prof = image.shape
img2 =np.zeros((lin,col,prof),'uint8')
img3 =np.zeros((lin,col,prof),'uint8')

filtro=np.ones((3,3))
filtro=filtro/9

for l in range(1,lin-1):
    for c in range(1,col-1):
        R= np.multiply(image[l-1:l+2,c-1:c+2,0], filtro).sum()
        G= np.multiply(image[l-1:l+2,c-1:c+2,1], filtro).sum()
        B= np.multiply(image[l-1:l+2,c-1:c+2,2], filtro).sum()   
        img2[l,c,:] = R,G,B
        

        

plt.figure()
plt.subplot(241)
plt.imshow(img3)
plt.subplot(242)
plt.imshow(image[:,:,0],cmap="gray",vmin=0,vmax=255) #R
plt.subplot(243)
plt.imshow(image[:,:,1],cmap="gray",vmin=0,vmax=255) #G
plt.subplot(244)
plt.imshow(image[:,:,2],cmap="gray",vmin=0,vmax=255) #B

plt.subplot(245)
plt.imshow(img2)
plt.subplot(246)
plt.imshow(img2[:,:,0],cmap="gray",vmin=0,vmax=255) #C
plt.subplot(247)
plt.imshow(img2[:,:,1],cmap="gray",vmin=0,vmax=255) #M
plt.subplot(248)
plt.imshow(img2[:,:,2],cmap="gray",vmin=0,vmax=255) #Y
plt.show()
