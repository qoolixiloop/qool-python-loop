#!/usr/bin/env python
# -*- coding: utf-8 -*-

# simon.clematide@uzh.ch
# PCL I


import nltk

entries = nltk.corpus.cmudict.entries()

print entries[71607] # ('love', ['L', 'AH1', 'V'])]

# Finde alle Wörter auf -n, welche als -M ausgeprochen werden.
print [ word for (word,pron) in entries
            if  pron[-1] == 'M'
            and word[-1] == 'n' ]


