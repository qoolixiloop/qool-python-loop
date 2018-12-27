#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PCL-I: Uebung 02 - Aufgabe 3, FS16

# Autoren:
# c(Student, Martikelnummer) -> 	{'Roland Benz'			: '97-923-163',
#									 'Linus Manser' : '13-791-132'}

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


## necessary imports to parse an xml file
from lxml import etree
from StringIO import StringIO
import codecs
import sys


## parse the plants.xml file and save it as "tree"
tree = etree.parse("plants.xml")

print "\n1) Welche Pflanzen haben bei der Eigenschaft 'Zone' einen Wert von 5?"
xpath1 = "/PLANTS/PLANT[@zone = '5']"
print ">>>  %s\n" % xpath1

# for every question the same procedure:
# apply the xpath expression to 'tree' and display the return values accordingly (changes for every question)
q1 = tree.xpath(xpath1)
for i in q1:
	print etree.tostring(i)

print "\n2) Wieviel würde es kosten, wenn man eines jeder Pflanze kaufen würde?"
xpath2 = "/PLANTS/PLANT/PRICE/text()"
print ">>>  %s\n" % xpath2

q2 = tree.xpath(xpath2)
print sum(float(i) for i in q2)


print "\n3) Welche Pflanzen brauchen Schatten, 'Shade'? Nenne ihre botanischen Namen."
xpath3 = "/PLANTS/PLANT[./LIGHT/text() = 'Shade']/BOTANICAL/text()"
print ">>>  %s\n" % xpath3

q3 = tree.xpath(xpath3)
ans = [i for i in set(q3)]
for i in ans:
	print "-",i

print "\n4) Wieviele Pflanzen gibt es insgesamt?"
xpath4 = "count(/PLANTS/PLANT)"
print ">>>  %s\n" % xpath4

q4 = tree.xpath(xpath4)
print int(q4)










