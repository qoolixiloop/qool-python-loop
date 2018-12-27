#!/usr/bin/env python
# -*- coding: utf-8 -*-

# simon.clematide@uzh.ch
# PCL I

from nltk.book import *

words = set(text1)

longwords = [w for w in words if len(w)>15]

print longwords
