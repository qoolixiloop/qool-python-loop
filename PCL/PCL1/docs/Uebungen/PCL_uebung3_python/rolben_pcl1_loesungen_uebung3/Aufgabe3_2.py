#!/usr/bin/env python
# -*- coding: utf-8 -*-

#PCL I, Übung 3, HS15
#Aufgabe 3_2
#Autor: Roland Benz
#Matrikel-Nr.: 97-923-163 

'''
Für diese Aufgabe steht das Buch ’Moby Dick; or The Whale’ von Herman Melville als .txt-Datei
moby_dick.txt bereit.
Schreibe nun ein Python-Programm, welches den Datei-Pfad oder den Namen (wenn sich die Datei
im selben Ordner wie das Programm befindet) einer Datei als Kommandozeilenargument erwartet.
Programm Aufruf soll so aussehen:
$ python Aufgabe3_2.py Dateiname.txt
Nutze für die Übung das Buch von Herman, aber dein Programm soll für jedes Buch in diesem
Format funktionieren.
Folgende Operationen sollen ausgeführt werden:
a) Tokenisiere jede Zeile mit der Funktion split(). Speichere nun jedes Wort, welches grösser als
6 Buchstaben ist, als Schlüssel in ein Dictionary und setze für dessen Wert für den Moment eine
beliebige Ganzzahl, z.B. 1. Was passiert, wenn ein Wort schon im Dictionary vorhanden ist?
b) Erweitere das Programm nun so, dass die Werte im Dictionary die Anzahl der Vorkommen jedes
Wortes (die Schlüssel) im Buch, welches grösser als 6 Buchstaben ist, angeben. Vorschlag: Wenn
ein Token zum ersten Mal auftaucht (d.h. es ist noch kein Schlüssel im Dictionary), füge es dem
Dictionary als Schlüssel mit dem Wert 1 zu. Befindet sich das Token schon im Dictionary, dann
erhöhe den aktuellen Wert um 1.
c) Lass das so aufgebaute Dictionary ausgeben, und zwar entweder sortiert nach dem Schlüssel
oder – wenn du herausfindest, wie – nach dem Wert (der Worthäufigkeit). Wiederum soll jedes
Schlüssel-Wert-Paar auf einer eigenen Zeile zu stehen kommen.
'''

'''
### Making a dictionary ###

data = {}
# OR
data = dict()

### Initially adding values ###

data = {'a':1,'b':2,'c':3}
# OR
data = dict(a=1, b=2, c=3)

### Inserting/Updating value ###

data['a']=1  # updates if 'a' exists, else adds 'a'
# OR
data.update({'a':1})
# OR
data.update(dict(a=1))
# OR
data.update(a=1)

### Merging 2 dictionaries ###

data.update(data2)  # Where data2 is also a dict.

### Deleting items in dictionary ###

del data[key] #Remove specific element in a dictionary
#OR
data.clear() #Clear entire dictionary
'''

#Debug:  python -m pdb Aufgabe3_2.py
#Call:   python Aufgabe3_2.py /media/benzro/OS/Users/benzro/Documents/LubuntuShared/"8) PCL-1"/Übungen/PCL_uebung3_python/moby_dick.txt

#Your code

#Schreibe nun ein Python-Programm, welches den Datei-Pfad oder den Namen (wenn sich die Datei
#im selben Ordner wie das Programm befindet) einer Datei als Kommandozeilenargument erwartet.
#Call from shell or from within Geany with Execute.

import sys
strPathAndFilename=""
try:
	strPathAndFilename=sys.argv[1] #Throws an IndexError Exception
except:
	strPath="/media/benzro/OS/Users/benzro/Documents/"\
			+"LubuntuShared/8) PCL-1/Übungen/PCL_uebung3_python/"
	strFilename="moby_dick.txt" 
	strPathAndFilename=strPath+strFilename

#Open and read book
import os.path
fileExists=os.path.isfile(strPathAndFilename)
if not fileExists:
	print "The file\n %s" % (strPathAndFilename)\
			+	"does not exist. Exit process.\n"
	sys.exit() #kills the phyton interpreter process
else:
	try:
		bookIn=open(strPathAndFilename, "r") #Throws an Exception
		#Comment next two lines, otherwise bookIn is in EOF state at line 109
		#strBookIn=bookIn.read()
		#lstBookIn=strBookIn.split() #"\n" does not remove blank and \r
	except:
		print "Could not open the file %s\n" % (strPathAndFilename)\
				+ "\nExit process.\n"

print "\nAwesome------------I made it that far!---------------\n"

#a) Tokenisiere jede Zeile mit der Funktion split(). Speichere nun jedes Wort, welches grösser als
#6 Buchstaben ist, als Schlüssel in ein Dictionary und setze für dessen Wert für den Moment eine
#beliebige Ganzzahl, z.B. 1. 
intConst=1
dictLongTokens={}
for line in bookIn.readlines():
    lstTokensInLine=line.split()
    for token in lstTokensInLine:
		if  len(token)>6:
			#check if key already exists in dictionary (dictLongToken.has_key(token))
			if token in dictLongTokens:
				#append key value pair (value = nr of occurences)
				intTmp=dictLongTokens.get(token)+1
				dictLongTokens.update({token:intTmp})
			else:
				#append key value pair
				dictLongTokens.update({token:intConst})

print "a) Dictionary of words with six or more characters: \n"\
	+ "  (print only the last 20)"
for key, value in dictLongTokens.items()[-20:]:
    print "Key: %s \t value: %s" %(key,value)

print "\nWas passiert, wenn ein Wort schon im Dictionary vorhanden ist?\n"\
+ "--> Dictionary.update({key:value}) method makes an update, i.e.\n"\
+ "    either appends a new pair or changes the value of an existing one.\n"
    
#b) Erweitere das Programm nun so, dass die Werte im Dictionary die Anzahl der Vorkommen jedes
#Wortes (die Schlüssel) im Buch, welches grösser als 6 Buchstaben ist, angeben. Vorschlag: Wenn
#ein Token zum ersten Mal auftaucht (d.h. es ist noch kein Schlüssel im Dictionary), füge es dem
#Dictionary als Schlüssel mit dem Wert 1 zu. Befindet sich das Token schon im Dictionary, dann
#erhöhe den aktuellen Wert um 1.
print "\nb) Extensions actually already been done by default in task a)" 

dictSomePairs = {key: dictLongTokens[key] for key in dictLongTokens.keys()[10:60]}
print "\nb) Print some pairs as dictionary:\n %s \n" %(dictSomePairs)

print "\nb) Print some pairs as key and value variables:"
for key,value in dictLongTokens.items()[10:30]:
		print "Key: %s \t value: %s" %(key,value)

#c) Lass das so aufgebaute Dictionary ausgeben, und zwar entweder sortiert nach dem Schlüssel
#oder – wenn du herausfindest, wie – nach dem Wert (der Worthäufigkeit). Wiederum soll jedes
#Schlüssel-Wert-Paar auf einer eigenen Zeile zu stehen kommen.
print "\nc) Dictionary sorted by key:\n"\
	+ "   (print only the first 20)" 
for key, value in sorted(dictLongTokens.items())[:20]:
  print "Key: %s \t value: %s" %(key,value)

print "\nc) Dictionary sorted by value:\n"\
	+ "   (print only the largest 20)" 
lstOfTplDictLongTokens = list(dictLongTokens.items())
lstOfTplTop20 = sorted(lstOfTplDictLongTokens, key=lambda tup: tup[1])[-20:]
for elem in lstOfTplTop20:
  print "Key: %s \t value: %s" %(elem[0],elem[1])
