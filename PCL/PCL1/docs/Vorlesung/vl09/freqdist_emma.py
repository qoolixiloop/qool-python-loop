#!/usr/bin/env python
# -*- coding: utf-8 -*-

# simon.clematide@uzh.ch
# PCL I

import nltk
from nltk.corpus import gutenberg

#Load text
emma_words = gutenberg.words('austen-emma.txt')
print "\n", type(emma_words), "\n", len(emma_words)

#Calculate frequency distribution of words
emma_fd = nltk.FreqDist(emma_words)
print "\n", type(emma_fd),"\n", emma_fd

#Print frequency distribution of words
emma_fd_sorted=sorted(emma_fd, key=emma_fd.get, reverse=True )
print "\n", type(emma_fd_sorted),"\n", emma_fd_sorted[:20], "\n"
for w in emma_fd_sorted[:5]:
    print w, "\t\t", emma_fd[w]

#Tabuliere die häufigsten 20 Wörter
print "\n", type(emma_fd.tabulate)
emma_fd.tabulate(20)

#Plot frequency distribution of words
emma_fd.plot(10, cumulative=False)

# Finde alle Wörter für die gilt:
# - mehr als 10 Buchstaben und
# - kommen mindestens 7 mal vor
# - printe nur die ersten 20
wl = sorted([w for w in emma_fd.keys()
            if len(w)>10 and emma_fd[w]> 7])
print "\n", wl[:20], "\n"


