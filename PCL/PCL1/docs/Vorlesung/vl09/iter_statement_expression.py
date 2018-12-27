#!/usr/bin/env python
# -*- coding: utf-8 -*-

# simon.clematide@uzh.ch
# PCL I

# Listenbildung mit iterativen Statements
sl = list()
for c in "St. Moritz-Str. 23":
    if c.isalnum():
        sl.append(c.lower())
print sl

# Listenbildung mit Listenkomprehensionsausdruck
el = [c.lower() for c in "St. Moritz-Str. 23" if c.isalnum()]
print el
