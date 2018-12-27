#!/usr/bin/python
# -*- coding: utf-8 -*-

# simon.clematide@uzh.ch
# PCL I

# Data type str

# Einzeilige (!) Zeichenkette 
# mit Escape-Sequenzen
s1 = "a\n\x61"
print "Canonical s1: ",repr(s1)
print "Printed   s1: ",s1

# Rohe Sequenz r"..."
# ohne Escapes
s2 = r"a\n\x61"
print "Canonical s2: ",repr(s2)
print "Printed   s2: ",s2

# Longstring
s3 = """a
a"""
print "Canonical s3: ",repr(s3)
print "Printed   s3: ",s3

# Rohe Longstring
s4 = r"""a
a"""
print "Canonical s4: ",repr(s4)
print "Printed   s4: ",s4

print
print "Type of s1:", type(s1)
print "Type of s2:", type(s2)
print "Type of s3:", type(s3)
print "Type of s4:", type(s4)

print
print "Test: s1 == s2 Result:", s1 == s2
print "Test: s1 == s3 Result:", s1 == s3
print "Test: s2 == s4 Result:", s2 == s4
print "Test: s1 == s4 Result:", s1 == s4
