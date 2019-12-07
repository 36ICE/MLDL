# -*- coding:utf-8 -*-
from __future__ import print_function
from nltk.corpus import sinica_treebank
from nltk.corpus import inaugural


import nltk

# import nltk
# nltk.download('sinica_treebank')
# nltk.download('inaugural')
# sinica_text = nltk.Text(sinica_treebank.words())
# print sinica_text
#
# for (key, var) in sinica_treebank.tagged_words()[:8]:
#     print '%s/%s' % (key, var)
#
# sinica_treebank.parsed_sents()[15].draw()
#
# sinica_fd=nltk.FreqDist(sinica_treebank.words())
# top100=sinica_fd.items()[0:100]
# for (x,y) in top100:
#     print x, y

# print (nltk.corpus.gutenberg.fileids())
# print nltk.corpus.gutenberg.words('austen-emma.txt')

# from nltk.corpus import reuters
# for e in reuters.words('training/9865'):
#     print (e,end=' ')

print([fileid[:4] for fileid in inaugural.fileids()])
cfd = nltk.ConditionalFreqDist(
           (target, fileid[:4])
          for fileid in inaugural.fileids()
          for w in inaugural.words(fileid)
          for target in ['america', 'citizen']
          if w.lower().startswith(target))
cfd.plot()