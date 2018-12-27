#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nltk.corpus import webtext

text6 = webtext.words('grail.txt')
word = 'GLOBAL'

def space1():
	word = text6[11]
	return word
	
def space2():
	word=""
	word2 = word
	return word2

print space1()
#KING
print space2()
#GLOBAL
