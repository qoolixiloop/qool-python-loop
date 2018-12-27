#!/usr/bin/env python
# -*- coding: utf-8 -*-

# simon.clematide@uzh.ch
# PCL I

import re

teststr = '''This
is a
Test.'''

# Traditionelle Funktionsdefinition
def sf(s):
    # \s is any white space character
    # and equivalent to [ \t \n \r \f]
    return re.sub(r'\s+','',s)
print sf(teststr)

def isf(s):
    return re.sub(r'[ \t \n \r \f]+','',s)
print isf(teststr)

# Funktionsdefinition mit Lambda-Ausdruck
ef = lambda s: re.sub(r'\s+','',s)
print ef(teststr)

# Was passiert, wenn kein return Statement existiert?
def sf2(s):
    re.sub(r'\s+','',s)
print sf2(teststr)

# Was passiert, wenn ich schreibe:
# SyntaxError: invalid syntax -> return
# ef = lambda s: return re.sub(r'\s+','',s)
# print sf(teststr)