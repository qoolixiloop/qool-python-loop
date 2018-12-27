#!/usr/bin/env python
# -*- coding: utf-8 -*-

#PCL I, Übung 3, HS15
#Aufgabe 2_2
#Autor: Roland Benz
#Matrikel-Nr.: 97-923-163 

'''
2.2 Buchstabensuppe
Nimm den String „gesundheitswiederherstellungsmittelmischungsverhaeltniskundiger“, das das längs-
te Wort des Text+Berg Korpus (SAC-Jahrbuch 1905) ist, und lass dieses mit Hilfe einer for-Schleife
ausgeben. In jedem Durchlauf der for-Schleife soll jeweils nur ein einziger Buchstabe des Wortes aus-
gegeben werden, und zwar so oft wie seine Position im Alphabet. Zum Beispiel tritt „g“ im Alphabet
an 6ter Stelle auf. Darum wird es 6 mal ausgegeben. Wenn beispielsweise das Programm nur die
Zeichen „gesundheit“ liest, sieht die Ausgabe so aus:
gggggg
eeee
sssssssssssssssssss
uuuuuuuuuuuuuuuuuuuuu
nnnnnnnnnnnnnn
dddd
hhhhhhhh
eeeee
iiiiiiiii
tttttttttttttttttttt
Tipp: Du erhältst die Position eines Zeichens im Alphabet mit der Funktion string.lowercase.index():
import string
letter_pos = string.lowercase.index(a_letter)
'''

#Debug:  python -m pdb <fileName.py>

#Your code
from random import choice
from string import lowercase
import string

strLongWrd="gesundheitswiederherstellungsmittel"\
			+"mischungsverhaeltniskundiger"
print "\n %s \n" % (strLongWrd)

#Solution 1
i=0			
for char in strLongWrd:
	i+=1
	charPosABC = string.lowercase.index(char) + 1
	strToPrint = "".join(char for i in range(charPosABC))
	print " %d : <%d> \t %s \n" % (i,charPosABC,strToPrint)
	#print "%d:   " + strToPrint + "\n"	% (i)
	
#Solution 2
i=0
for char in strLongWrd:
	i+=1
	charPosABC = string.lowercase.index(char) + 1
	strToPrint = char * charPosABC	
	print " %d : <%d> \t %s \n" % (i,charPosABC,strToPrint)
		
#With randomized strings
i=0
for char in strLongWrd:
	i+=1
	charPosABC = string.lowercase.index(char) + 1
	strToPrint = "".join(choice(lowercase) for i in range(charPosABC))	
	print " %d : <%d> \t %s \n" % (i,charPosABC,strToPrint)
			
			
			
			
			
