#!/usr/bin/env python
# -*- coding: utf-8 -*-
#PCL I, Übung 5, HS15
#Aufgabe 2

def wc1(textfile):
    c = 0
    for line in textfile:
        for word in line.split():
            c += 1
    return c


def wc2(textfile):
    c = 0
    for line in textfile:
        for word in line.split():
            c += 1
        return c

def wc3(textfile):
    c = 0
    for line in textfile:
        for word in line.split():
            c += 1
            return c


print "wc1:", wc1(open('def_block.py','r'))
print "wc2:", wc2(open('def_block.py','r'))
print "wc3:", wc3(open('def_block.py','r'))
