# -*- coding: utf-8 -*-

#PCL1-Ü2-Aufgabe 5
#ursprüngl. Katrin Affolter, modifiziert durch Adrian van der Lek, weiter modifiziert durch Raphael Balimann

#
#Gib hier an, was das Programm genau macht:
#
#Eingabe:
#Ausgabe:
#

usrinput = raw_input('Please enter desired height of the diamond: ')
char = raw_input('Which character should be used? ')

var1 = int(usrinput)
var2 = var1 * 2 - 1
 
varA = 0 
varB = 1
varC = 0

print "\n----------------------------\n"

while ( varA < var1 ): 
	if (var1 - varA) < var1/2:
		varC +=2
		if var1 - varA == 1 and varC >= 8:
			varD = (varC - 5)/2
			print " " * ((var2 - varB)/2) + char * (varB/2 - varC/2) + varD * " " + "SHINE" + varD * " " + char * (varB/2 - varC/2 + 2)
		else:
			print " " * ((var2 - varB)/2) + char * (varB/2 - varC/2) + varC * " " + char * (varB/2 - varC/2 + 1)
	else:
		print " " * ((var2 - varB)/2) + char * varB
	varA += 1
	varB += 2

varA -= 1
varB -= 2
	
while ( varA >= 0 ): 
	if (var1 - varA) < var1/2:
		varC -=2
		print " " * ((var2 - varB)/2) + char * (varB/2 - varC/2) + varC * " " + char * (varB/2 - varC/2 + 1)
	else:
		print " " * ((var2 - varB)/2) + char * varB
	varA -= 1
	varB -= 2

print "\n----------------------------\n"
