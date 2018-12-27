#!/usr/bin/env python
# -*- coding: utf-8 -*-

# simon.clematide@uzh.ch
# PCL I
#

import sys

#Den Inhalt dieser Datei
# ohne Leerzeilen printen
filename = "with_open.py"

with open(filename,'r') as f:
  for l in f:
    if l.rstrip() != '':
       sys.stdout.write(l)

