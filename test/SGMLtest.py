#coding:utf-8

from sgmllib import SGMLParser
from urllib import urlopen
from urlparse import urljoin

class AllTextParser(SGMLParser):
    def __init__(self, url):
        SGMLParser.__init__(self)
        self.url = url
        self.is_js = False
        self.is_st = False
        self.div = []
        self.charset = 'utf-8'
        self.all_div = []
        www = urlopen(url)
        self.feed(www.read())
        www.close()

    def start_script(self, a):
        self.is_js = True
    def end_script(self):
        self.is_js = False
    def start_style(self, a):
        self.is_st = True
    def end_style(self):
        self.is_st = False
    def start_p(self, a):
        if self.div:
            self.div[-1][0] += '<p>'

    def end_p(self):
        if self.div:
            self.div[-1][0] += '</p>'

    def start_a(self, a):
        if self.div:
            d = dict(a)
            try:self.div[-1][0] += '<a target="_blank" href="%s">' % urljoin(self.url, d['href'])
            except:pass

    def end_a(self):
        if self.div:
            self.div[-1][0] += '</a>'

    def start_img(self, a):
        if self.div:
            d = dict(a)
            try:self.div[-1][0] += '<img src="%s" border="0" alt="%s" />' % (urljoin(self.url, d['src']), d.get('alt', ''))
            except:pass
    def start_meta(self, a):
        d = dict(a)
        if d.get('http-equiv') == 'Content-Type':
            try:
                self.charset = d.get('content').split('=')[1].lower()
                if self.charset[:2] == 'gb':
                    self.charset = 'gb18030'
                self.type = d.get('content').split(';')[0]
            except:pass
        '''elif d.has_key('name'):
            try:setattr(self, d.get('name'), d.get('content'))
            except:pass'''

    def start_br(self, a):
        if self.div:
            self.div[-1][0] += '<br />'

    def start_div(self, a):
        self.div.append(['', 0])

    def end_div(self):
        try:
            self.all_div.append(self.div[-1])
            del(self.div[-1])
        except: pass

    def handle_data(self, text):
        if self.is_js or self.is_st:
            pass
        elif self.div:
            self.div[-1][0] += text
            self.div[-1][1] += len(text)

    def get_result(self):
        m = 0
        c = 0
        mc = 0
        for x in self.all_div:
            l = x[1]
            if l > m:
                mc = c
                m = l
            c += 1
        if self.charset not in ['utf-8', 'utf8']:
            return self.all_div[mc][0].decode(self.charset).encode('utf8')
        return self.all_div[mc][0]

if __name__ == '__main__':
    webSite = AllTextParser('http://outofmemory.cn/code-snippet/1625/Hibernate-how-achieve-pagination-search')
    print webSite.get_result().replace('/<[^>]+>/g'," ")