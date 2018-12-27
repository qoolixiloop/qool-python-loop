#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# PCL1-Ü2-Aufgabe 5
# Vorlage von Raphael Balimann (raphael.balimann@uzh.ch) - HS 2015
#


# Eingabe des Names vom Nutzer, jedoch nur Nachname, danach Begrüssung durch Programm
usrinput = raw_input('Bitte gebe deinen Nachnamen ein: ')
print "Hallo" + usrinput

# Vermessung der Eingabe
length = len(usrinput)

# Ausgabe je nach Länge des Namens, jedoch relativ ungenau
if (length == 4):
	print "Dein Nachname hat 4 Zeichen."
else:
	print "Dein Nachname hat mehr oder weniger als 4 Zeichen."
	
# Keine Verabschiedung durch das Programm