# -*- coding: utf-8 -*-

import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# 创建3D对象
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# 分别生成x、y坐标数据
xcord = np.arange(-5, 5, 0.5)
ycord = np.arange(-5, 5, 0.5)
# 将坐标向量转换成坐标矩阵(vectors -> matrices)
xcord, ycord = np.meshgrid(xcord, ycord)
# 生成z坐标数据
r = np.sqrt(xcord**2 + ycord**2)
zcord = r
# 绘制散点图，将图形分成两部分，用不同颜色绘制
ax.scatter(xcord[:10], ycord[:10], zcord[:10], c='r')
ax.scatter(xcord[10:], ycord[10:], zcord[10:], c='g')
plt.show()