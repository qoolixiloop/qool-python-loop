#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PCL-I: Uebung 02 - Aufgabe 2, FS16

# Autoren:
# c(Student, Martikelnummer) -> 	{'Roland Benz'			: '97-923-163',
#									 'Linus Manser' 		: '13-791-132'}
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Aufruf des Programms:
# Version 1: python ex02_testscript.py
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


## necessary imports to parse an xml file
from lxml import etree
from StringIO import StringIO
import codecs
import sys


## parse the plants.xml file and save it as "tree"
tree = etree.parse("plants.xml")

# Frage 1
print "\n1) Der botanische Name der zweiten Pflanze?"

xpath1 = "/PLANTS/PLANT[2]/BOTANICAL/text()"
q1 = tree.xpath(xpath1)

print ">>> %s\n" % xpath1
print q1[0]


# Frage 2
print "\n2) Anzahl Pflanzen mit Zone ‘Annual’?"

xpath2 = "count(/PLANTS/PLANT[@zone = 'Annual'])"
q2 = tree.xpath(xpath2)

print ">>> %s\n" % xpath2
print q2


# Frage 3
print "\n3) Die Zone der Pflanzen mit ‘Shade’ als Lichtbedingung?"

xpath3 = "/PLANTS/PLANT[./LIGHT = 'Shade']/@zone"
q3 = tree.xpath(xpath3)
ans = [i for i in set(q3)]

print ">>> %s\n" % xpath3
for i in ans:
	print "-",i


# Frage 4
print "\n4) Alle Namen der Pflanzen mit Zone ‘2’?"

xpath4 = "/PLANTS/PLANT[@zone = '2']/BOTANICAL/text()"
q4 = tree.xpath(xpath4)

print ">>> %s\n" % xpath4
for i in q4:
    print i

# Frage 5
print "\n5) Pflanzen, welche einen Preis groesser als 5 haben?"

xpath5 = "/PLANTS/PLANT[./PRICE > '5']"
q5 = tree.xpath(xpath5)

print ">>> %s\n" % xpath5
for i in q5:
    print etree.tostring(i)