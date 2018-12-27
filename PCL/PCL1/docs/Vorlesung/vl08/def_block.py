#!/usr/bin/env python
# -*- coding: utf-8 -*-

# simon.clematide@uzh.ch
# PCL I
# Datei: def_block.py
def wc1(textfile):
    c = 0
    for line in textfile:
        for word in line.split():
            c += 1
    return c #count words of whole file

def wc2(textfile):
    c = 0
    for line in textfile:
        for word in line.split():
            c += 1
        return c #count words of first line

def wc3(textfile):
    c = 0
    for line in textfile:
        for word in line.split():
            c += 1
            return c #no count, return 1

#ruft sich selber auf
print "wc1:", wc1(open('def_block.py','r'))
print "wc2:", wc2(open('def_block.py','r'))
print "wc3:", wc3(open('def_block.py','r'))
