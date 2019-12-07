from goose import Goose

url = 'http://epaper.anhuinews.com/html/ahrb/20181023/article_3701141.shtml'
g = Goose()
article = g.extract(url=url)
print 'title:'+article.title
print 'meta_description:'+article.meta_description
print 'cleaned_text:'+article.cleaned_text
# print 'top_image src:'+article.top_image