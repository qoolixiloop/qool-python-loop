#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PCL-I: Uebung 02 - Aufgabe 3, FS16

# Autoren:
# c(Student, Martikelnummer) -> 	{'Roland Benz'			: '97-923-163',
#									 'Linus Manser' 		: '13-791-132'}
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Aufruf des Programms:
# Version 1: python ex03.py
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


## necessary imports to parse an xml file
from lxml import etree
from StringIO import StringIO
import codecs
import sys


## parse the plants.xml file and save it as "tree"
tree = etree.parse("plants.xml")

# Frage 1
print "\n1) Welche Pflanzen haben bei der Eigenschaft 'Zone' einen Wert von 5?"

xpath1 = "/PLANTS/PLANT[@zone = '5']"
q1 = tree.xpath(xpath1)

print ">>> %s\n" % xpath1
for i in q1:
	print etree.tostring(i)
	
	
# Frage 2
print "\n2) Wieviel würde es kosten, wenn man eines jeder Pflanze kaufen würde?"

xpath2 = "sum(/PLANTS/PLANT/PRICE/text())"
q2 = tree.xpath(xpath2)

print ">>> %s\n" % xpath2
print q2


# Frage 3
print "\n3) Welche Pflanzen brauchen Schatten, 'Shade'? Nenne ihre botanischen Namen."

xpath3 = "/PLANTS/PLANT[./LIGHT/text() = 'Shade']/BOTANICAL/text()"
q3 = tree.xpath(xpath3)
ans = [i for i in set(q3)]

print ">>> %s\n" % xpath3
for i in ans:
	print "-",i
	
	
# Frage 4
print "\n4) Wieviele Pflanzen gibt es insgesamt?"

xpath4 = "count(/PLANTS/PLANT)"
q4 = tree.xpath(xpath4)

print ">>> %s\n" % xpath4
print int(q4)










