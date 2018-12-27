#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PCL-I: Uebung 4 - Aufgabe 4, HS15

# Autoren:
# c(Student, Martikelnummer) -> 	{'Roland Benz'			: '97-923-163', 
#									 'Lennart von Thiessen' : '11-185-790'}

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Aufruf des Programms:
# Version 1: python Aufgabe4.py --database tagged.txt --text 'Dies ist ein Test.'
# Version 2: python Aufgabe4.py --database tagged.txt --file input.txt
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

'''
4 Wortarten erkennen und annotieren
Diese Übung basiert auf der Aufgabe Wortendungen erkennen aus Übung 2.
Das Programm sollte nun so erweitert werden, dass erkannte Wörter in einer Datei zwischengespei-
chert werden, währenddessen die unbekannten Wörter mithilfe von regulären Ausdrücken erraten
und danach vom Nutzer bestätigt oder korrigiert werden können.
Wie können Wörter gespeichert werden, welche eine Wortform haben, aber zu mehreren Wortarten
gehören können?
Als Eingabe sollen zwei Möglichkeiten angeboten werden:
• Eingabe eines Satzes direkt von der Kommandozeile als Argument
• Eingabe von Sätzen aus einer Textdatei, welche als Argument gegeben wird.
Mögliche Syntax für die beiden Aufrufe:
• python aufgabe_3.py --database tagged.txt --text 'Dies ist ein Test.'
• python aufgabe_3.py --database tagged.txt --file input.txt
Die Ausgabe der vollständig annotierten Sätze erfolgt auf der Standardausgabe, oder (optional) in
eine weitere Textdatei. In beiden Fällen sollten die Resultate in einer geeigneten Form zwischenge-
speichert werden.
Als Tagset dient das STTS Tagset, in der Datei tagged.txt befinden sich einige Beispiele.

'''

print "########################################################################"
print 'Hi! Program 4 : Wortarten erkennen und annotieren (started)'
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

import sys
import re

#--------------------------------------------------------------------------------#
# Globale Variablen deklarieren und einige Fehler abfangen                       #
#--------------------------------------------------------------------------------#
ip = sys.argv
error_msg = "Arguments are wrong -> Fkt-call : \n 'python Aufgabe4.py --database tagged.txt --text 'Dies ist ein Test.'' \n 'python Aufgabe4.py --database tagged.txt --file input.txt'"

if(len(ip) == 1 or len(ip) != 5 or ip[1] != "--database"):
	sys.exit(error_msg)

sentinel = ip[3]
inString = []
db = {}
cTagged = 0

if(sentinel == '--file'):
	filename = sys.argv[4]
	infile = open(filename, 'r')
	
	for line in infile:
		line  = line.rstrip('\n')
		inString = inString + line.split()

	infile.close()
elif(sentinel == '--text'):
	tmp = ip[4].rstrip('\n')
	inString = tmp.split()
else:
	sys.exit(error_msg)

#--------------------------------------------------------------------------------#
# Database Textfile in Dictionary umwandeln                                      #
#--------------------------------------------------------------------------------#
filename = sys.argv[2]
infile = open(filename, 'r')

for line in infile:
	line = line.rstrip('\n')
	row = line.split()

	if(row[0] not in db):
		db[row[0]] = row[1]

#--------------------------------------------------------------------------------#
# Erzeuge Lösungsvektor (2-dim Liste: [[word,tag]])                              #
#--------------------------------------------------------------------------------#
sol = []
for i in range(0,len(inString)):
	sol.append([inString[i],"N/A"])

#--------------------------------------------------------------------------------#
# Erweitere die Datenbank ein wenig                                              #
#--------------------------------------------------------------------------------#

pronomen = {'ich':'PPER', 'du':'PPER', 'er':'PPER', 'wir':'PPER', 'ihr':'PPER', 'sie':'PPER', 'der':'ART', 'die':'ART', 'das':'ART', 'mein':'PPOSAT', 'meine':'PPOSAT', 'dein':'PPOSAT', \
			'deine':'PPOSAT', 'unser':'PPOSAT', 'unsere':'PPOSAT', 'mich':'PPER', 'dich':'PRF', 'sich':'PRF', 'uns':'PRF', 'euch':'PRF', 'eine':'ART', 'wer':'PWS', 'was':'PWS'} # usw.
mehr = {'und':'KON', 'oder':'KON', 'aber':'KON', 'als':'KOKOM', 'wie':'KOKOM', 'weil':'KOUS', 'dass':'KOUS', 'damit':'KOUS'}
db.update(pronomen)
db.update(mehr)

#--------------------------------------------------------------------------------#
# Naive regex für Worterkennung && Funktion für Benutzereingabe                  #
#--------------------------------------------------------------------------------#
regexNN = "(e|er|el|eur|ent|ei|euse|or|ant|ist|oge|us|f|ung|heit|keit|ion|ur|ar|ät|a|ie|in|ine|chen|lein|nis|um|ium)$" # allenfalls verb od adj
regexAD = "(ig|lich|isch|haft|bar|los|sam|er|sten)$"
regexVV = "(e|en|ln|st|t|te)$"

def ask(word, proposal):
	true = raw_input('Ist "' + word + '" ein "' + proposal + '"? (y/n)\n')
	if(true == 'y'):
		return proposal
	elif(true == 'n'):
		rigth = raw_input('Von welcher Wortart ist denn "' + word + '"?\n')
		return rigth
	else:
		sys.exit("Falsche Eingabe! Programm wurde beendet.")


#--------------------------------------------------------------------------------#
# Wortartenbestimmung basierend auf Database && Regex                            #
# Bei Schätzung durch Regex oder Unklarheiten wird der Benutzer gefragt.         #
#--------------------------------------------------------------------------------#
for i in range(0, len(sol)):
	if(sol[i][0].lower() in db):
		sol[i][1] = db[sol[i][0].lower()]
	elif((re.search(regexNN,sol[i][0])) != None):
		sol[i][1] = ask(sol[i][0], "NN")
	elif((re.search(regexAD,sol[i][0])) != None):
		sol[i][1] = ask(sol[i][0], "ADJD")
	elif((re.search(regexVV,sol[i][0])) != None):
		sol[i][1] = ask(sol[i][0], "VVFIN")
	else:
		sol[i][1] = raw_input('Von welcher Wortart ist "' + sol[i][0] + '"?\n')

	# Nach def neu in dict aufnehmen
	db.update({sol[i][0]:sol[i][1]})


#--------------------------------------------------------------------------------#
# Finale Lösung etwas aufbereiten für schönere Darstellung in Konsole            #
#--------------------------------------------------------------------------------#		
finalSol = ''
for i in range(0, len(sol)):
	finalSol = finalSol + sol[i][0] + "(" + sol[i][1] + ") "

print finalSol

print "########################################################################"
print "Bye Bye und bis bald! :-)"
print "########################################################################"

