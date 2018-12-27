#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Aufgabe 3.1
'''
lstText=[]
#some code to fill lstText
lstOutput=findWordsWithSuffixIng(lstText)
def findWordsWithSuffixIng(lstText):
	lstTmp=[]
	for word in set(lstText):
		if word >= 4 and word[-3:] == 'ing']:
			lstTmp.append(word.lower())
	return sorted(lstTmp)
'''
#Aufgabe 3.2
from nltk.corpus import webtext
text6 = webtext.words('grail.txt')

#Funktionsdefinition
#a) Worte mit Suffix -ing
def long_words(text):
	list_out = []
	for word in set(text):
		if len(word) > 7 and word[-3:] == 'ing':
			list_out.append(word.lower())
	return sorted(list_out, key = len)
#b) 2-Tupel aller unterschiedlichen Worte (Set()) und deren Anzahl Zeichen 
def tuples(text):
	list_out = []
	for word in set(text):
		length = len(word)
		list_out.append((word,length))
	return list_out
#c) 3-Tupel aus Trigrammen (Jedes Wort und seine zwei nachfolgenden Nachbarn)
def trigrams(text):
	list_out = []
	for i in range(2,len(text)):
		trigram = (text[i-2],text[i-1],text[i])
		list_out.append(trigram)
	return list_out

#Aufruf der Funktionen
print "\n", len(text6), " ---- ", text6[:10]
print "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~def foo():~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n"
a=long_words(text6)
print "\n", len(a), " ---- ", a[:10],"\n"
b=tuples(text6)
print "\n",len(b), " ---- ", b[:10],"\n"
c=trigrams(text6)
print "\n",len(c), " ---- ", c[:10],"\n"

#Listenkomprehension
print "\n~~~~~~~~~~~~~~~~~~~~~~Listenkomprehension~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n"
a=sorted([word.lower() for word in set(text6) \
			if len(word) > 7 and word[-3:] == 'ing'],key = len)
print "\n", len(a), " ---- ", a[:10],"\n"
b=[(word, len(word)) for word in set(text6)]
print "\n",len(b), " ---- ", b[:10],"\n"
c=[(text6[i-2],text6[i-1],text6[i]) for i in range(2,len(text6))]
print "\n",len(c), " ---- ", c[:10],"\n"
