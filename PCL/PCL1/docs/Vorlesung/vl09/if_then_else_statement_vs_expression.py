#!/usr/bin/env python
# -*- coding: utf-8 -*-

# simon.clematide@uzh.ch
# PCL I

# Als Statement, Anweisung
sl = []
for c in "St. Moritz-Str. 23":
    if c.isalnum():
        sl.append(c)
    else:
        sl.append(' ')
print sl

# Als Expression, Ausdruck
el = [ c if c.isalnum() else ' ' for c in "St. Moritz-Str. 23" ]
print el

