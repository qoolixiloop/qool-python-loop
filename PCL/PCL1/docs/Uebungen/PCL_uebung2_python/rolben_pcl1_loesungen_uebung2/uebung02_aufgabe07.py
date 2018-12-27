#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Author
#------
#Roland Benz, 97-923-163

#Dieses Programm ausführen mit: 
#------------------------------
#python uebung02_aufgabe07.py


#7 Zusatzaufgabe: Wortwelle
#Schreibe ein Programm, welches ein Wort vom Nutzer entgegennimmt und dieses Wort dann in einer
#Wellenform ausgibt.
print "\nDear user, this script prints\n a wave."
inputIsOK = False
while not inputIsOK:
	strIn=raw_input("\nPlease enter anything longer\n than 10 characters:\n")
	print "\nYou entered:\n" + strIn + "\n"
	inputIsOK=(len(strIn)>10)
	if inputIsOK:
		#oberer Teil der Welle (zunehmender Teil inkl. Maximum)
		cnt=0
		while cnt < len(strIn):
			print strIn[:(cnt+1)]+ "\n" ,
			cnt+=1
		#unterer Teil der Welle (abnehmender Teil)
		cnt-=2
		while cnt > 0:
			print strIn[:(cnt+1)]+ "\n" ,
			cnt-=1
	else:
		print "Oops, something went wrong!"
		continue

#Beispielhafter Programmablauf:
#B i t t e gebe e i n ( l a n g e s ) Wort e i n :
#Welle
#We
#Wel
#Well
#Welle
#Well
#Wel
#We
#Die Aufgabe muss nicht abgegeben werden, je kreativer eine Ausgabe, desto besser!
#Mögliche Variationen:
