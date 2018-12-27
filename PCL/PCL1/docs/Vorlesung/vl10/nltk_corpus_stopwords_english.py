#!/usr/bin/env python
# -*- coding: utf-8 -*-

# simon.clematide@uzh.ch
# PCL I

import nltk

stopwords_en = nltk.corpus.stopwords.words('english')
print len(stopwords_en), stopwords_en[::20]  # 127
    # [u'i', u'herself', u'was', u'because', u'from',
    # u'any', u't']

### Using German stopword list this way suffers from
### encoding problems
stopwords_de = nltk.corpus.stopwords.words('german')
print len(stopwords_de), sorted(stopwords_de)[::20] # 231
    # [u'aber', u'auch', u'dem', u'dieser', u'er', u'hin',
    # u'jeder', u'manchem', u'nur', u'solches', u'warst',
    # u'wollen']
