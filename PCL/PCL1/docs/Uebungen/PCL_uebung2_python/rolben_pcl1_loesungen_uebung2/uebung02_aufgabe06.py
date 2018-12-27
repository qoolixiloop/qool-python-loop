#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Author
#------
#Roland Benz, 97-923-163

#Dieses Programm ausführen mit: 
#------------------------------
#python uebung02_aufgabe06.py


#6 Kommentare
#Kommentare helfen, ein Programm zu verstehen. Dies ist nicht nur für uns Tutoren wichtig, auch
#hilft es euch, an einem späteren Zeitpunkt zu verstehen, wie das Programm genau funktioniert.
#Um zu verdeutlichen, wie nützlich gute Kommentare sind, und zur Übung liegt das Python-Skript
#kommentieren.py bei. Öffne das Skript mit einem Editor nach Wahl und kommentiere das Skript in
#einer sinnvollen Weise (es sollte nicht jede Zeile kommentiert sein).
#Um herauszufinden, was eine bestimmte Zeile im Skript bewirkt, ist es hilfreich, die entsprechende
#Zeile auszukommentieren und zu sehen, wie sich der Programmablauf ändert.
#Abzugeben ist kommentieren.py mit den zusätzlichen Kommentaren.

#ursprüngl. Katrin Affolter, modifiziert durch Adrian van der Lek, weiter modifiziert durch Raphael Balimann

#
#Gib hier an, was das Programm genau macht:
#
#Eingabe: Erst eine Ganzzahl Z (Gleitkommazahl erzeugt Traceback) eingeben, 
#					dann einen beliebigen Buchstaben B (Buchstabenkombination möglich) eingeben.
#Ausgabe: gestrichelte Linie, Leerzeile, 2*Z Zeilen mit Buchstabenmuster, Leerzeile, gestrichelte Linie
#					Das Buchstabenmuster für Z= 3: 1*B, 3*B, 5*B,                                                                                                                 						      5*B, 3*B, 1*B
#					Das Buchstabenmuster für Z= 4: 1*B, 3*B, 5*B;                  5*B (Loch);                                                                                							   7*B, 5*B, 3*B, 1*B 
#					Das Buchstabenmuster für Z= 5: 1*B, 3*B, 5*B, 7*B;             7*B (Loch);                                                                          							    9*B, 7*B, 5*B, 3*B, 1*B 
#					Das Buchstabenmuster fpr Z= 6: 1*B, 3*B, 5*B, 7*B;             7*B (Loch),  7*B (Loch),                                        							  9*B (Loch);             9*B, 7*B, 5*B, 3*B, 1*B 
#					Das Buchstabenmuster für Z= 7: 1*B, 3*B, 5*B, 7*B, 9*B;        9*B (Loch),  9*B (Loch),                                        							 11*B (Loch);       11*B, 9*B, 7*B, 5*B, 3*B, 1*B 
#					Das Buchstabenmuster für Z=10: 1*B, 3*B, 5*B, 7*B, 9*B, 11*B; 11*B (Loch), 11*B (Loch), 11*B (Loch), 12*B (SHINE), 13*B (Loch), 13*B (Loch), 13*B (Loch); 13*B, 11*B, 9*B, 7*B, 5*B, 3*B, 1*B 
#					Für Z>=10 auf Zeile Z wird das Loch mit dem Wort SHINE gefüllt

#Debugging: True setzen, normaler call des scripts, s für step 
dBug=True
if dBug:                  #Diese umständliche Art des Debuggings ist OK für eine einzige Aufgabe.
	import pdb              #In Zukunft wäre ein Debug Plug-in im Editor ein riesiger Time-Saver! 
	pdb.set_trace()         #Könnte mir beim nächsten Tutoriat jemand helfen den Debugger für den Geany Editor zu installieren?

#Eingabe einer Ganzzahl, welche der halben Höhe des Diamantmusters entspricht
usrinput = raw_input('Please enter desired height of the diamond: ')

#Eingabe eines oder mehrerer Buchstaben, mit welchen das Diamantmuster gedruckt wird
char = raw_input('Which character should be used? ')

#Initialisierung der Variablen
#Annahme für die Kommentare: var1==10 !!!!
#----------------------------++++++++-----
var1 = int(usrinput)
var2 = var1 * 2 - 1
 
varA = 0 
varB = 1
varC = 0

#Drucken einer Leerzeile, einer gestrichelten Linie, und einer Leerzeile
print "\n----------------------------\n"

#Drucken des oberen Teils des Diamanten
#var1=[10, 10 ...                            ] bleibt konstant 10 bei jeder Iteration
#var2=[19, 19 ...                            ] bleibt konstant 19 bei jeder Iteration
#VarA=[ 0, 1, 2, 3, 4,  5,  6,  7,  8,  9, 10] an Programm-Zeile 77 
#varB=[ 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21] an Programm Zeile 77
#varC=[ 0, 0, ...           2   4,  6,  8,   ] an Programm-Zeile 83 
#varD=[ n  n, ...                       1,   ] an Programm-Zeile 89
if dBug:
	itr=0
while ( varA < var1 ): 
	#debugging
	if dBug:
		print "*********dBug:=" + str(dBug) + ", itr= " + str(itr) + ", varA= " + str(varA) + ", varB= " + str(varB) 
	#dann werden diese Zeilen geprintet (ab Iteration 6)
	if (var1 - varA) < var1/2:
		varC +=2
		#debugging
		if dBug:
			print "*********dBug:=" + str(dBug) + ", itr= " + str(itr) + ", varC= " + str(varC)
		#dann wird diese Zeile geprintet (nur einmal bei Iteration 9)
		if var1 - varA == 1 and varC >= 8:
			varD = (varC - 5)/2
			#debugging
			if dBug:
				print "*********dBug:=" + str(dBug) + ", itr= " + str(itr) + ", varD= " + str(varD)
			print " " * ((var2 - varB)/2) + char * (varB/2 - varC/2) + varD * " " + "SHINE" + varD * " " + char * (varB/2 - varC/2 + 2)
		#erst werden diese Zeilen geprintet (ab Iteration 6)
		else:
			print " " * ((var2 - varB)/2) + char * (varB/2 - varC/2) + varC * " " + char * (varB/2 - varC/2 + 1)
	#erst werden diese Zeilen geprintet (Iteration 0 bis 5), (NrOf Whitespace + NrOf B's)
	else:
		print " " * ((var2 - varB)/2) + char * varB
	#Inkrementierung bei jedem Durchgang
	varA += 1
	varB += 2
	if dBug:
		itr+=1
		
#Drucken des unteren Teils des Diamanten
#VarA=[ 9,  8,  7,  6,  5, 4, 3, 2, 1, 0] an Programm-Zeile 114 
#varB=[19, 17, 15, 13, 11, 9, 7, 5, 3, 1] an Programm Zeile 114
#varC=[ 6,  4,  2,  0, ...              ] an Programm-Zeile 120 
varA -= 1
varB -= 2
if dBug:
	itr=0
while ( varA >= 0 ): 
	#debugging
	if dBug:
		print "*********dBug:=" + str(dBug) + ", itr= " + str(itr) + ", varA= " + str(varA) + ", varB= " + str(varB)
	#erst werden diese Zeilen geprintet bis varC==0 (Iteration 0 bis 3)
	if (var1 - varA) < var1/2:
		varC -=2
		#debugging
		if dBug:
			print "*********dBug:=" + str(dBug) + ", itr= " + str(itr) + ", varC= " + str(varC)
		print " " * ((var2 - varB)/2) + char * (varB/2 - varC/2) + varC * " " + char * (varB/2 - varC/2 + 1)
	#dann werden diese Zeilen geprintet (ab Iteration 4)
	else:
		print " " * ((var2 - varB)/2) + char * varB
	#Dekrementierung bei jedem Durchgang
	varA -= 1
	varB -= 2
	if dBug:
		itr+=1
#Drucken einer Leerzeile, einer gestrichelten Linie, und einer Leerzeile
print "\n----------------------------\n"
