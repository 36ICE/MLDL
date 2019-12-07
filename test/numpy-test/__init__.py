#-*-coding:utf-8-*-

import numpy as np

# 设置了 dtype
x = np.arange(5, dtype =  float)
print (x)
x = np.arange(10,20,2)
print (x)

import numpy as np

a = np.arange(10)
s = slice(2, 7, 2)  # 从索引 2 开始到索引 7 停止，间隔为2
print (a[s])