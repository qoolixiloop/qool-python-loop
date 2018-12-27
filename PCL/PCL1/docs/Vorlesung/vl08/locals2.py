#!/usr/bin/env python
# -*- coding: utf-8 -*-

# simon.clematide@uzh.ch
# PCL I

g = "Globale Variable"

def foo():
    a = g
    return a

def bar():
    b = a
    return b

a=foo()
print a
print bar()



# Mit Debugger bearbeiten.
