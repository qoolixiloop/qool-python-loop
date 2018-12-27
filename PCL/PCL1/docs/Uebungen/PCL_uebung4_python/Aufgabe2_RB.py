#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PCL-I: Uebung 4 - Aufgabe 2, HS15

# Autoren:
# c(Student, Martikelnummer) -> 	{'Roland Benz'			: '97-923-163', 
#									 'Lennart von Thiessen' : '11-185-790'}

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Aufruf des Programms:
# Version 1: python Aufgabe_2.py Aufgabe2_VerbList.txt
# Version 2: python Aufgabe_2.py Aufgabe2_VerbList.txt -v "e"
# Version 3: python Aufgabe_2.py Aufgabe2_VerbList.txt -s "ing"
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

'''
2 Stemming
Erstelle ein Programm, welches eine Textdatei mit je einem englischen Verb pro Zeile einliest und
danach bei jedem Wort den Stamm und die Endung mithilfe von regulären Ausdrücken voneinander
trennt.
Die Ausgabe erfolgt auf der Standardausgabe und sollte wie folgt aussehen:
testing -> test ing
listens -> listen s
followed -> follow ed
claim -> claim
Erweitere das Programm, sodass es zusätzlich als Filter funktioniert, ähnlich wie die Werkzeuge aus
Übung 1, zum Beispiel grep.
'''

#Debug:  
#	python -m pdb <fileName.py>

print "\n########################################################################"
print 'Hi! Program 2 : Stemming; Stamm und Endung Trennen (started)'
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

#import packages
import sys ## necessary for command line arguments
import re  ## necessary for regular expressions
import codecs ##necessary to read file as UTF-8

#Command line arguments
try:
	inFilename = sys.argv[1] #get the filename	
	#inOption: -v für VerbStem, -s für Suffix
	inOption=str(sys.argv[2])
	inRegex=sys.argv[3]
except:
	inFilename= "Aufgabe2_VerbList.txt" 
	inOption= "-s"
	inRegex= "ing"
finally:
	#für jede for Schleife ein neues infile Objekt (end of file)
	infile = codecs.open(inFilename, 'r', encoding='utf-8')
	infile2 = codecs.open(inFilename, 'r', encoding='utf-8')

#Lösung I) mit Dictionnary (unten Lösung II mit Regex) 
#Annahme jede Zeile enthält genau ein Wort, das Wort ist ein Verb
print "\na) Solution I with dictionnary"
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"

dictSuffix={'ing':1,'s':1,'ed':1}
print "suffix dictionnary:"
print dictSuffix.keys()

dictTplVerbSuffix={}
for strLine in infile:
	SuffixFound=False
	strWord = strLine.rstrip('\n') #lstWord=strline.split()		
	#suche Suffix (der Länge 3,2,1,0)
	for position in range(len(strWord)-4,len(strWord)):
		verb=strWord[0:position]
		suffix=strWord[position:]
		if suffix in dictSuffix:
			dictTplVerbSuffix.update({verb:suffix})
			SuffixFound=True
			exit
	if not SuffixFound:	
		dictTplVerbSuffix.update({strWord:""})
			
print "\na) Print some pairs as key and value variables:"
for key,value in dictTplVerbSuffix.items()[0:30]:
		print "Key: %s \t value: %s" %(key,value)
		

#Lösung II) mit Regex (oben Lösung I mit Dictionnary) 
print "\na) Solution II with regex"
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"

strRegex = re.compile(r"(ing$|s$|ed$)")
print "Regex:"
print strRegex.pattern, "\n"

i_lines = 0
print "Print some pairs as key and value variables:"
for strLine in infile2:
	i_lines += 1
	strWord = strLine.rstrip('\n')
	#Speichere ersten Treffer in temporäre Liste
	#regexMatch = re.search(strRegex, strWord) #returns a match object
	#Speichere alle nichtüberlappenden Matches in temporäre Liste
	lstTmp = re.findall(strRegex, strWord) #returns a list of strings
	suffixFound=(len(lstTmp) != 0)
	if suffixFound:
		solution = strWord + ' -> ' + strWord[:-len(lstTmp[0])] + ' ' + lstTmp[0]
		print solution
	else:
		solution = strWord + ' -> ' + strWord
		print solution
print i_lines, ' Verben wurden überprüft'
					

#b) Filterung mit Command Line Argumenten:
print "\nb) filter found key-value pairs with command line arguments"
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
dictOutput={}
if inOption == "-v":
	for strKey, strValue in dictTplVerbSuffix.items():
		regexMatch = re.search(inRegex, strKey)
		print "\n1:", inRegex, regexMatch
		print "2:", strKey, strValue
		if not regexMatch == None: 
			print "3:", regexMatch.group(0)
			dictOutput.update({strKey:strValue})
	print "\nSolution:"
	print "~~~~~~~~~~"
	print "4:", dictOutput, "\n"
elif inOption == "-s":
	for strKey, strValue in dictTplVerbSuffix.items():
		regexMatch = re.search(inRegex, strValue)
		print "\n1:", inRegex, regexMatch
		print "2:", strKey, strValue 
		if not regexMatch == None: 
			print "3:", regexMatch.group(0)
			dictOutput.update({strKey:strValue})
	print "\nSolution:"
	print "~~~~~~~~~~"
	print "4:", dictOutput, "\n"
	
#close file
infile.close()

print "########################################################################"
print "Bye Bye und bis bald! :-)"
print "########################################################################"
