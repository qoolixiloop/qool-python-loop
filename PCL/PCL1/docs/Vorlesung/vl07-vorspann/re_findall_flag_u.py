#!/usr/bin/python
# -*- coding: utf-8 -*-

# simon.clematide@uzh.ch
# PCL I

import re

text = u"Viele Köche verderben den Brei."
pattern = ur"(\w+)"

# Alle Matches finden
m = re.findall(pattern, text)

for g in m:
    print g

print

# Das Flag (?u) aktiviert Unicode-Kategorien fuer \w und \b
pattern = ur"(?u)(\w+)"

# Resultat ist eine Liste
m = re.findall(pattern, text)

for s in m:
    print s
