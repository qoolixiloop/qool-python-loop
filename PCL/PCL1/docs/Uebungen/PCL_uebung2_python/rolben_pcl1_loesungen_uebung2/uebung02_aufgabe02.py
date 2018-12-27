#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Author
#------
#Roland Benz, 97-923-163

#Dieses Programm ausführen mit: 
#------------------------------
#python uebung02_aufgabe02.py


#2 Begrüssung
#Wir wollen ein Programm erstellen, welches den Nutzer zuerst nach seinem Namen fragt, und ihn
#dann nach der Eingabe mit Vor- und Nachname begrüsst.
strFullName=raw_input("Dear user, please enter your full name:\n")
print "\nDear " + strFullName + ", welcome to my solution of task 2!\n"

#Danach soll die Länge des Nachnamens vermessen werden, ausgegeben 
listFullName=strFullName.split(" ")
intNameLen=len(listFullName[1])
print "Your second name has " + str(intNameLen) + " characters.\n" 

#und das Programm mit folgenden Ausgaben beenden:
#• Falls der Nachname 8 oder mehr Zeichen lang ist: Verabschiedung mit Nachnamen
#• Falls der Nachname zwischen 5 und 8 Zeichen lang ist: Verabschiedung mit Vor- und Nachname
#• Falls der Nachname weniger als 5 Zeichen lang ist: Verabschiedung mit Vorname
if intNameLen>8:
	print "Good bye, Mr./Mrs. " + listFullName[1]	+ "!\n"
elif intNameLen>=5 and intNameLen<=8:
	print "Good bye and ciao, " + listFullName[0] + " " + listFullName[1] + "!\n"
elif intNameLen<5 and intNameLen>2:
	print "Ciao, " + listFullName[0] + "!\n"
else:
	print "Ciao, " + listFullName[0] + ". You have a very short second name!\n"

	
#Der Programmablauf sollte ungefähr so aussehen:
#Willkommen , was i s t i h r Nachname?
#Bond
#Was i s t denn i h r Vorname?
#James
#Guten Tag James Bond .
#I h r Nachname hat 4 Z e i c h e n .
#Auf Wiedersehen James !
#Beigelegt ist ein Programm (vorlage_02.py), welches schon gewisse Teile ausführt, es kann als
#Vorlage für das vollständige Programm verwendet werden. Abzugeben ist das komplette, ausführbare
#Programm.
