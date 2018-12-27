#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Demo Tour of NLTK
from __future__ import division

from nltk.book import *

text1

text1[1:50]

# Concordancing
print "here 1: "
text1.concordance("man")
print "here 2: "
text2.concordance("man")

# Similarity
print "here 3: "
text1.similar("man")
print "here 4: "
text2.similar("man")
print "here 5: "
text1.similar("love")
print "here 6: "
text2.similar("love")
print "here 7: "

text1.collocations()   # Sperm whale=Pottwal
text4.generate() # Politische Rede? Sich inspirieren lassen von präsidialer Ansprache
text4.common_contexts(['crisis','honor'])

# Dispersion Plots
text4.dispersion_plot(["freedom","war"])
text4.dispersion_plot(["economy","war"])

# Generation
print "here 8: "
text1.generate()
print "here 9: "
text2.generate()
print "here 10: "

# Frequency Distributions
fdist2 = FreqDist(text2)
vocabulary2=fdist2.keys()
vocabulary2[:50]
fdist2.plot(50,cumulative=True)

# List comprehension
V = set(text2)
long_words = [w for w in V if len(w)>15]
long_words


# Defining functions
def lexical_diversity(text):
    return len(text) / len(set(text))


lexical_diversity(text1)


