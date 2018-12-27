#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

text = u"Viele Köche verderben den Brei."
pattern_ur = ur"(\w+)"
pattern_u = u"(\w+)"
pattern_r = r"(\w+)"
pattern = "(\w+)"
print "\n",pattern_ur, pattern_u, pattern_r, pattern,"\n"
print repr(pattern_ur), repr(pattern_u), repr(pattern_r),\
    repr(pattern),"\n"
# Alle Matches finden
m_ur = re.findall(pattern_ur, text)
m_u = re.findall(pattern_u, text)
m_r = re.findall(pattern_r, text)
m = re.findall(pattern, text)
for g in m_ur:
    print g
print ""
for g in m_u:
    print g
print ""
for g in m_r:
    print g
print ""
for g in m:
    print g