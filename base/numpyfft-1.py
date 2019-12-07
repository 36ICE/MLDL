# -*- coding: utf-8 -*-

import cv2
import numpy as np
import matplotlib.pyplot as plt
img1=cv2.imread('./data/bg2017121301.jpg',0)
f=np.fft.fft2(img1)
fshift=np.fft.fftshift(f)
fshift1=np.fft.fftshift(f)
rows,cols=img1.shape
crow,ccol=np.ceil(rows/2),np.ceil(cols/2)
crow,ccol=np.int(crow),np.int(ccol)

#注意fshift是用来与原图像进行掩模操作的但是具体的，我也看着很抽象。这一部分与低通的有些相对的意思。
fshift[crow-20:crow+20,ccol-20:ccol+20]=0
fshift=(fshift/2+fshift1/2)

f_ishift=np.fft.ifftshift(fshift)
img_back=np.fft.ifft2(f_ishift)
img_back=np.abs(img_back)
plt.subplot(1,2,1),plt.imshow(img1,'gray')
plt.title('input image'),plt.xticks([]),plt.yticks([])
plt.subplot(1,2,2),plt.imshow(img_back, 'gray')
plt.title('image after HPF'),plt.xticks([]),plt.yticks([])
plt.show()
