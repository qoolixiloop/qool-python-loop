#!/usr/bin/env python
# -*- coding: utf-8 -*-

# simon.clematide@uzh.ch
# PCL I
# See page 44 Bird and Klein 2009

import nltk
from nltk.corpus import brown

#Conditional Frequency Distribution
cfd = nltk.ConditionalFreqDist([
    (genre, word)
    for genre in brown.categories()
    for word in brown.words(categories=genre)])
print "\n",type(cfd),"\n",cfd,"\n"

#Wie oft kommen die modals (samples)
# conditional in den genres (conditions) vor
genres = ['news', 'religion', 'hobbies',
         'science_fiction', 'romance', 'humor']

modals = ['can', 'could', 'may', 'might', 'must', 'will']

cfd.tabulate(conditions=genres, samples=modals)
