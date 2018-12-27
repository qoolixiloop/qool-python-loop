#!/usr/bin/env python
# -*- coding: utf-8 -*-

# simon.clematide@uzh.ch
# PCL I

# Demonstration von Generatorausdrücken
quadrat = (i*i for i in [10,11])

print quadrat
print type(quadrat)

# generator hat keine len()
# print len(quadrat)

# next() liefert nächstes Element zurück.
print quadrat.next()
print quadrat.next()

# Durchiterieren
quadrat = (i*i for i in xrange(10,13))
for q in quadrat:
  print q

