#!/usr/bin/env python
# -*- coding: utf-8 -*-

# simon.clematide@uzh.ch
# PCL I

# Lade Modul book aus Package nltk und
# importiere alle Objekte und Funktionen ins aktuelle Modul
from nltk.book import *

# Objekte und Funktionen aus nltk.book können ohne
# Modulpräfixe bezeichnet werden.
print "Zweites Token aus text1:", text1[1] 

# Die vollqualifizierter Punktnotation geht dann nicht
print "Zweites Wort aus text1:", \
    nltk.book.text1[1] #Traceback (most recent call last):
