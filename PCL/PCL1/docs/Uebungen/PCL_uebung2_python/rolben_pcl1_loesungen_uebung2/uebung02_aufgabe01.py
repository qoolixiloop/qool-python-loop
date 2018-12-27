#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Author
#------
#Roland Benz, 97-923-163

#Dieses Programm ausführen mit: 
#------------------------------
#python uebung02_aufgabe01.py


#1 Erste Schritte mit Python
#Öffne in einem Terminal den Python-Interpreter mit dem Befehl python. Spiele mit den bisher in
#der Vorlesung genannten Funktionen herum, und probiere die folgenden Dinge:
#• Eine Variable definieren, ausgeben und wieder neu definieren
myStringVar="Hi Phyton"
print myStringVar
myStringVar="Ciao"
print myStringVar
#• Eine Schleife deiner Wahl benutzen
count=0
while count<5:
	print count, myStringVar
	count=count+1
#• Eine Unterscheidung mit if durchführen
inVar=raw_input("Enter Hello or Ciao: ")
if inVar == "Hello":
	print "Right! you entered:", inVar
elif inVar== "Ciao":
	print "Right! you entered:", inVar
else:
	print "Wrong! you entered:", inVar
#• Python mit exit() verlassen
exit()
#Abzugeben ist hier nichts, bitte vergewissere dich jedoch, dass Python 2.7 geöffnet wurde.

