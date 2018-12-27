#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Author
#------
#Roland Benz, 97-923-163

#Dieses Programm ausführen mit: 
#------------------------------
#python uebung02_aufgabe03.py


#3 Zahlen und deren Tücken
#Implementiere die folgenden Formeln in Python:
#x = (a + b + 3) / c
#y =(b − a^b) / x
#Die Werte von a, b und c sollten vom Nutzer eingegeben und als Variable gespeichert werden,
#die Werte x und y sollten am Schluss so genau wie möglich ausgegeben werden. Da die Eingaben
#von Nutzern immer als String (Zeichenketten) verarbeitet werden, müssen die Zahlen umgewandelt
#werden. Die Funktion int(argument) verwandelt das Argument in eine ganze Zahl (integer), die
#Funktion float(argument) in eine Fliesskommazahl (float).
print "Dear user, this script calculates\n x = (a + b + 3) / c\n and\n y =(b − a^b) / x"
inputIsOK = False
while not inputIsOK:
	strThreeNumbers=raw_input("\nPlease enter the three numbers\n (a b c) separated by a space: \n")
	print "\nYou entered: " + strThreeNumbers + "\n"
	listThreeNumbers=strThreeNumbers.split(" ")
	inputIsOK=len(listThreeNumbers)==3
	if inputIsOK:
		a=float(listThreeNumbers[0])
		b=float(listThreeNumbers[1])
		c=float(listThreeNumbers[2])
		x=(a+b+3)/c
		y=(b-a**b)/x
		print "Floating point calc:\n x= " + str(x) + ", and y= "+ str(y) + "\n"
		a=int(a)
		b=int(b)
		c=int(c)-1
		x=(a+b+3)/c
		y=(b-a**b)/x
		print "Integer calc:\n x= " + str(x) + ", and y= "+ str(y) + "\n"
	else:
		print "Oops, something went wrong!"
		continue

	
#a) Was ist der Unterschied zwischen diesen beiden Typen?
#Konversion von string zu float: 
#Es folgt eine Fliesskomma-Berechnung (float op float -> float) (reelle Zahlen R)
#Konversion von float zu int: 
#Es folgt eine Ganzzahlen-Berechnung (int op int -> int) (ganze Zahlen Z)
#Konversion von string zu float oder int: 
#Es folgt eine Gemischte Berechnung, wobei (float op int -> float) und (int op int -> int)

#b) Wie schlägt sich das auf die Ergebnisse der Berechnungen nieder?
#Fliesskomma Berechnung: 
#Die Genauigkeit ist von der Mantisse und der Charakteristik abhängig
#Ganzzahl Berechnung: 
#Nach jeder Operation wird auf die nächstkleinere Ganzzahl gerundet. 
#aus (X.875 wird X) und aus (-X.875 wird -X-1)

#Abzugeben ist dein Programm mit Kommentaren zu den beiden Fragen.
