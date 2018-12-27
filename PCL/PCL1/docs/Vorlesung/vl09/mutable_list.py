#!/usr/bin/env python
# -*- coding: utf-8 -*-

# simon.clematide@uzh.ch
# PCL I
# Demonstration von Wichtigem
from nltk.book import *

#Set
words = set(text1)
print "\n",len(words),"\n"
#print words[:20] #set hat kein Attribut __getitem__

#String
print ', '.join(words)[:20],"\n " #ersten 20 chars

#List
print list(words)[:20],"\n" #ersten 20 list elements

#List
longwords = [w for w in words if len(w)>15]
print longwords,"\n"

#List
l = []
l.append(3)          # ein Element anhängen
l.extend((4,'x',5))  # eine ganze Sequenz anhängen
print l
del l[3]             # ein Element löschen
l[2] = 2             # eine Element austauschen
l.sort(reverse=True) # in-place umgekehrt sortieren
print l
