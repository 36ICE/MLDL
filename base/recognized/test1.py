# -*- coding: utf-8 -*-

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('dog.jpg',0)
edges = cv2.Canny(img,100,200) #参数:图片，minval，maxval,kernel = 3

plt.subplot(121) #121表示行数，列数，图片的序号即共一行两列，第一张图
plt.imshow(img,cmap='gray') #cmap :colormap 设置颜色
plt.title('original image'),plt.xticks([]),plt.yticks([]) #坐标轴起点，终点的值
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('edge image'),plt.xticks([]),plt.yticks([])

plt.show()


import cv2
import matplotlib.pyplot as plt
import numpy as np

filename = 'dog.jpg'
image = cv2.imread(filename,1)

model_path = "/Users/zengcd/PycharmProjects/MLDL/base/recognized/"+"model.yml.gz"
if image.size == 0:
    print('cannot read file')
    exit(0)
img = np.float32(image)
img = img*(1.0/255.0)
retval = cv2.ximgproc.createStructuredEdgeDetection(model_path)
a = retval.detectEdges(img)
plt.subplot(121)
plt.imshow(image,cmap='gray')
plt.subplot(122)
plt.imshow(a,cmap= 'gray')
plt.show()