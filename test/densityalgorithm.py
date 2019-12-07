# -*- coding: UTF-8 -*-

import re

import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import numpy as np


def remove_any_tag(s):
    # s = re.sub(r'''<[^>]+>''','',s)
    s = re.sub(re.compile(r'(?is)&lt;', re.S), '<', s)
    s = re.sub(re.compile(r'(?is)&gt;', re.S), '>', s)
    s = re.sub(re.compile(r'(?is)<!DOCTYPE.*?>', re.S), ' ', s)
    s = re.sub(re.compile(r'(?is)<!--.*?-->', re.S), ' ', s)
    s = re.sub(re.compile(r'(?is)<script.*?>.*?</script>', re.S), ' ', s)
    s = re.sub(re.compile(r'(?is)<style.*?>.*?</style>', re.S), ' ', s)
    s = re.sub(re.compile(r'&.{2,5};|&#.{2,5};', re.S), ' ', s)
    s = re.sub(re.compile(r'(?is)<.*?>', re.S), ' ', s)
    s = re.sub(re.compile(r'(?is)\\{.*?\\}', re.S), ' ', s)
    s = s.strip().replace(' ', '')
    return s.strip()


response = requests.get('http://society.people.com.cn/n1/2019/0902/c1008-31330284.html', params=None)
response.headers
response.encoding = 'utf-8'
# soup = BeautifulSoup(response.text, 'lxml')
# content = remove_any_tag(soup.prettify())
content = remove_any_tag(response.text)
# print content
# 假设content为已经拿到的html
# Ctext取周围k行(k<5),定为3
blocksWidth = 4

Ctext_len = []
# Ctext
lines = content.split('\n')
# lines = [x for x in content.split('\n') if x.__len__()>1]
# 去空格
for i in range(len(lines)):
    if lines[i] == ' ' or lines[i] == '\n':
        lines[i] = ''
# 计算纵坐标，每一个Ctext的长度
for i in range(0, len(lines) - blocksWidth):
    wordsNum = 0
    for j in range(i, i + blocksWidth):
        lines[j] = lines[j].replace("\s", "")
        wordsNum += len(lines[j])
    if wordsNum > 50:
        print lines[i]
        pass
    Ctext_len.append(wordsNum)
print Ctext_len

# 开始标识
start = -1
# 结束标识
end = -1
# 是否开始标识
boolstart = False
# 是否结束标识
boolend = False
# 行块的长度阈值
max_text_len = 88
# 文章主内容
main_text = []
# 没有分割出Ctext
if len(Ctext_len) < 3:
    print '没有正文'
for i in range(len(Ctext_len) - 3):
    # 如果高于这个阈值
    if (Ctext_len[i] > max_text_len and (not boolstart)):
        # Cblock下面3个都不为0，认为是正文
        if (Ctext_len[i + 1] != 0 or Ctext_len[i + 2] != 0 or Ctext_len[i + 3] != 0):
            boolstart = True
            start = i
            continue
    if (boolstart):
        # Cblock下面3个中有0，则结束
        if (Ctext_len[i] == 0 or Ctext_len[i + 1] == 0):
            end = i
            boolend = True
    tmp = []
    # 判断下面还有没有正文
    if (boolend):
        for ii in range(start, end + 1):
            if (len(lines[ii]) < 5):
                continue
            tmp.append(lines[ii] + "\n")
        str = "".join(list(tmp))
        # 去掉版权信息
        if (u"Copyright" in str or u"版权所有" in str):
            continue
        main_text.append(str)
        boolstart = boolend = False
# 返回主内容
result = "".join(list(main_text))

# print result


if Ctext_len.__len__() > 0:
    x = range(0, Ctext_len.__len__())
    print sum(Ctext_len) / Ctext_len.__len__()
    plt.figure()
    plt.plot(x, Ctext_len)
    plt.show()
