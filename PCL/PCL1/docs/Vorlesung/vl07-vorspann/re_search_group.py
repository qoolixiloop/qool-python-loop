#!/usr/bin/python
# -*- coding: utf-8 -*-

# simon.clematide@uzh.ch
# PCL I


import re

#Vorsicht: Innerhalb einer Klasse [.] hat der Punkt die
#Bedeutung eines Punktes und nicht jedes Zeichens ausser \n
text = 'my email is simon.clematide@uzh.ch and yours?'
pattern = r'([\w.]+)@([\w.]+)'

m = re.search(pattern, text)

# get whole match
print "Whole match:", m.group()

# get the first matched group
print "First group:", m.group(1)

# get the second matched group
print "Second group:", m.group(2)

# What is m?
print m
