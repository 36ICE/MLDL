#coding:utf-8


from bs4 import BeautifulSoup

markup ="<b><!--This will be used in the crawler--></b><p>It's wonderful"
tags = []
# soup = BeautifulSoup(markup,'html.parser')

#环境问题，可能报错，暂时还没搞懂html.parser和lxml的区别，后续跟进，如果报错，就用下一行的代码
soup = BeautifulSoup(markup,'lxml')
fixed_html = soup.prettify()
print fixed_html