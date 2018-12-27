#!/usr/bin/env python
# -*- coding: utf-8 -*-

# simon.clematide@uzh.ch
# PCL I

# Modul zur Zeitmessung von Python-Statements
#============================================
import timeit
setup = 'import random'

# Effekt von xrange vs. range bei random.sample
# Konstruiere 2 Timer-Objekte
tr = timeit.Timer('random.sample( range(1000000),100)', setup)
tx = timeit.Timer('random.sample(xrange(1000000),100)', setup)

# Führe Timings je einmal durch und speichere Anzahl Sekunden
trsecs = tr.timeit(1)   
txsecs = tx.timeit(1)

print "Aufgabe: Sample 100 Zahlen aus dem Bereich 0 bis 999999."
print "Zeit mit xrange:", txsecs, "Sekunden"
print "Zeit mit  range:", trsecs, "Sekunden"
print "xrange ist etwa", trsecs/txsecs, "Mal schneller!"
