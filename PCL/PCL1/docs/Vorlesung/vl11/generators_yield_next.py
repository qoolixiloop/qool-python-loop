#!/usr/bin/env python
# -*- coding: utf-8 -*-

# simon.clematide@uzh.ch
# PCL I

# Demonstration von Funktionen mit yield
#=======================================
def quadriere(iterierbar):
    for i in iterierbar:
        yield i*i

quadrat = quadriere([10,11])

print "from 1: ", quadrat
print "from 2: ",type(quadrat)

# next() liefert nächstes Element zurück.
print "from 3: ",quadrat.next()
print "from 4: ",quadrat.next()

#Falls keines mehr erhältlich ist, entsteht eine Ausnahme.
# In Iterationskontexten führt diese Ausnahme dazu,
# dass die Iteration beendet wird.
# Die Ausnahme wird "entsprechend" behandelt.
#print "from 5: ",quadrat.next()

# Generatoren sind erschöpft nach einem Durchgang
print "from 7: ",sum(quadrat)

#Aggregationsfunktion auf Generator anwenden
print "from 6: ",sum(quadriere([10,11]))


