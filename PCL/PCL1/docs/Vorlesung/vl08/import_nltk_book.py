#!/usr/bin/env python
# -*- coding: utf-8 -*-

# simon.clematide@uzh.ch
# PCL I

# Importiere Modul book aus Package nltk
import nltk.book

# Objekte und Funktionen aus nltk.book können nur in
# vollqualifizierter Punktnotation bezeichnet werden.
print "Zweites Wort aus text1:", nltk.book.text1[1] 

# Objekte und Funktionen können nicht direkt bezeichnet werden:
print text1[1] #Traceback (most recent call last):
