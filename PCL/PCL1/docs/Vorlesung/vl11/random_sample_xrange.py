#!/usr/bin/env python
# -*- coding: utf-8 -*-

# simon.clematide@uzh.ch
# PCL I


# Ziehe eine zufällige Auswahl von Vorkommen
# von Token aus einem Korpus
#===========================================
import nltk, random
corpus = nltk.corpus.nps_chat.words()

#xrange_=0,1,2,3...len(corpus)
xrange_=xrange(len(corpus))
print "\nfrom 1: ", xrange_, len(corpus)
#ziehe Anzahl (anz) Zufallszahlen aus xrange_
anz=20
randsamp=random.sample(xrange_,anz)
print "\nfrom 2: ", randsamp
#printe die Zufallswörter
for i in randsamp:
    print "\nfrom 3: ", corpus[i]

# as a reusable function with a generator return value
def sample_corpus1(text,size):
    return (text[i] for i in
            random.sample(xrange(len(text)),size))

# as a reusable function with a list return value
def sample_corpus2(text,size):
    return [text[i] for i in
            random.sample(xrange(len(text)),size)]

print "\nfrom 4: ", sample_corpus2(corpus,20)

