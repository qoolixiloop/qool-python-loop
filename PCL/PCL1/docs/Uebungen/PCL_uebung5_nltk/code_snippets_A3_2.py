#!/usr/bin/env python
# -*- coding: utf-8 -*-
#PCL I, Übung 5, HS15
#Aufgabe 3.2

import nltk
from nltk.corpus import webtext
text6 = webtext.words('grail.txt')

def long_words(text):
	list_out = []
	for word in set(text):
		if len(word) > 7 and word[-3:] == 'ing':
			list_out.append(word.lower())
	return sorted(list_out, key = len)

def tuples(text):
	list_out = []
	for word in set(text):
		length = len(word)
		list_out.append((word,length))
	return list_out

def trigrams(text):
	list_out = []
	for i in range(2,len(text)):
		trigram = (text[i-2],text[i-1],text[i])
		list_out.append(trigram)
	return list_out


print "long_words: ",long_words(text6)[:10]
print "tuples: ", tuples(text6)[:10]
print "trigrams: ", trigrams(text6)[:10]