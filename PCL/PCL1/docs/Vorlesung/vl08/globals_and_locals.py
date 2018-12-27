#!/usr/bin/env python
# -*- coding: utf-8 -*-

# simon.clematide@uzh.ch
# PCL I

__doc__ = 'Code zum Demonstrieren von globalen und lokalen Namen'

a = "Globale Variable"

def foo(a):
    print "In Funktion: a =", a
    return a

c = foo("Lokale Variable")

print "In Modul: a =", a



# Mit Debugger bearbeiten.
