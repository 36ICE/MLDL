# -*- coding: utf-8 -*-
import numpy as np
from scipy import fftpack
import matplotlib.pyplot as plt
import cv2 as cv
# moon = plt.imread('./data/bg2017121301.jpg')
moon = cv.imread('./data/bg2017121301.jpg', 0)
plt.figure(figsize=(12, 9))
plt.imshow(moon, cmap='gray')
plt.show()


moon_fft = fftpack.fft2(moon)

print(np.abs(moon_fft).mean())

cond = np.abs(moon_fft) > 7000

moon_fft[cond] = 0

moon_result = fftpack.ifft2(moon_fft)
moon_result = np.real(moon_result)
plt.figure(figsize=(12,9))

plt.imshow(moon_result,cmap = 'gray')
plt.imshow(np.real(moon_fft),cmap = 'gray')
plt.show()