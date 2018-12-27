#!/usr/bin/env python
# -*- coding: utf-8 -*-
#PCL I, Übung 5, HS15
#Aufgabe 4

from nltk.corpus import webtext
text6 = webtext.words('grail.txt')

word = 'GLOBAL'

def space1():
    word = text6[11]
    return word
def space2():
    word2 = word
    return word2
    
print space1()
print space2()