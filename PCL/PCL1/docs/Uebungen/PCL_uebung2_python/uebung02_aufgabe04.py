#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Author
#------
#Roland Benz, 97-923-163

#Dieses Programm ausführen mit: 
#------------------------------
#python uebung02_aufgabe04.py


#4 While
#Schreibe ein Programm, welches den Nutzer nach einer Eingabe fragt und dann die Zeichen vom
#dritten bis und mit dem fünften Zeichen ausgibt.
#Die Syntax einer While-Schleife ist:
#w h i l e ( a != b ) :
#print a
print "\nDear user, this script prints\n characters 3 to 5 of your input."
inputIsOK = False
while not inputIsOK:
	strIn=raw_input("\nPlease enter anything longer\n than 5 characters:\n")
	print "\nYou entered:\n" + strIn + "\n"
	inputIsOK=len(strIn)>5
	if inputIsOK:
		print "Characters 3 to 5 are:\n" +strIn[2:5]+ "\n" 
		cnt=2
		while cnt < 5:
			print strIn[cnt],
			cnt=cnt+1
	else:
		print "Oops, something went wrong!"
		continue

#a) Welche Probleme könnten sich bei diesem Programm ergeben?
#Sonderzeichen machen Probleme: 
#z.B. ç besteht aus zwei Zeichen und
#je nachdem, wo geschnitten wird, und ob mit 
#strIn[2:5] bzw. strIn[cnt] geprintet wird, gibts einen anderen Output.
#(1ç2345 -> �23 bzw. � 2 3) 
#(12ç345 -> ç3 bzw. � � 3)
#(123ç45 -> 3ç bzw. 3 � �)

#b) Wie könnten diese Probleme verhindert werden?
#Ein kluge und stabile Funktion schreiben, welche alle
#Spezialfälle abfängt und einheitlich behandelt.

#Abzugeben ist dein Programm mit Kommentaren zu den beiden Fragen.
