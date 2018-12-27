#!/usr/bin/python
# -*- coding: utf-8 -*-
import re

text = "Hässliche Köche verdürben das Gebräu" #utf8
text2 = u"Hässliche Köche verdürben das Gebräu" #unicode

pattern = r"([aeioäöü]+)" #utf-8
pattern2 = ur"([aeioäöü]+)" #unicode

print "\n",repr(text),repr(pattern),repr(text2),repr(pattern2)

# Im Ersetzungstext können gematchte Gruppen eingefügt werden.
# \N (N ist die N-te gruppierende Klammer im Pattern)
replacement = r"[\1]"
replacement2 = ur"[\1]"

print "\n",repr(replacement),repr(replacement2),"\n"

#pattern und text müssen beide Typ String oder beide Typ unicode
#sein, um die Umlaute zu finden
print re.sub(pattern, replacement, text) #alle
print re.sub(pattern, replacement, text2) #ohne äöü
print re.sub(pattern, replacement2, text) #alle
print re.sub(pattern2, replacement, text) #ohne äöü
print re.sub(pattern, replacement2, text2) #ohne äöü
print re.sub(pattern2, replacement2, text) #ohne äöü
print re.sub(pattern2, replacement, text2) #alle
print re.sub(pattern2, replacement2, text2) #alle


# Hinweis: Testen Sie aus, was passiert, wenn im text das u beim \
# String-Literal entfernt wird.
