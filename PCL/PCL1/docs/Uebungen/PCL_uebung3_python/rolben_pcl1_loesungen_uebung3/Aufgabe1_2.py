#!/usr/bin/env python
# -*- coding: utf-8 -*-


#PCL I, Übung 3, HS15
#Aufgabe 1_2
#Autor: Roland Benz
#Matrikel-Nr.: 97-923-163 

'''
Für diese Aufgabe steht die .txt-Datei kafka_trial.txt bereit. Diese Datei beinhaltet das Buch
’The Trial’ von Franz Kafka.
a) Schreibe ein Programm, welches von der BenutzerIn Endungen einliest, welche mindestens vier
Buchstaben lang sind. Es soll dann im Buch von Kafka nach Wörtern suchen, welche diese En-
dung haben. Das Programm soll so lange nach neuen Endungen fragen, bis mindestens 150 Wörter
gefunden worden sind. Beispielsausgabe:
Please enter a 4-letter ending you want to look for:
tter
The ending 'tter' was found 97 times.
Please enter a 4-letter ending you want to look for:
illy
The ending 'illy' was found 3 times.
...
You have found more than 150 words!
Wenn eine eingegebene Endung kürzer ist als 4 Buchstaben, nicht nur Buchstaben enthält oder
schonmal eingegeben wurde, soll eine Fehlermeldung kommen und die BenutzerIn nochmals nach
einer Endung fragen.
Beachte: Wörter die kürzer sind als 4 Buchstaben sollen nicht überprüft werden.
b) Erweitere das Programm nun so, dass es am Schluss ausgibt, wie viele und welche Endungen
eingegeben und wie viele unterschiedliche Wörter (Hinweis: set()) gefunden wurden. Auch soll
es mitteilen, welche und wie lange die 5 längsten gefundenen Wörter sind.
c) Zusatz: Das Programm soll nur Endungen akzeptieren, welche in mehr als 5 Wörtern vorkommen.
Kommentiere dein Programm sinnvoll. Abzugeben ist das komplette von dir ergänzte, ausführbare
Skript. (Bitte benenne das Dokument wie oben definiert.)
'''

#Debug flag
dBug=False
if dBug:                  
	import pdb
	pdb.set_trace() 
	         
#Call from shell or from within Geany with Execute
import sys
strPathAndFilename=""
try:
	strPathAndFilename=sys.argv[1] #Throws an IndexError Exception
except:
	strPath="/media/benzro/OS/Users/benzro/Documents/"\
			+"LubuntuShared/8) PCL-1/Übungen/PCL_uebung3_python/"
	strFilename="kafka_verwandlung_vert.txt" 
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
		strBookIn=bookIn.read()
		lstBookIn=strBookIn.split() #"\n" does not remove blank and \r
	except:
		print "Could not open the file %s\n" % (strPathAndFilename)\
				+ "\nExit process.\n"

#Variables and containers
strIn="" #string of user input
lstIn=[] #list of user inputs
strLstIn="" #string of list of user inputs
lstFndWrdsTotal=[] #list of found words in total
setFndWrdsTotal=set() #unique list or set of found words in total
cntFndWrdsTotal=0 #counter of found words in total

#Find 150 word that match the suffixes entered by the user
cntIter=0 # counts the number of rounds
enoughWordsFound = (cntFndWrdsTotal>=150)
while not enoughWordsFound:
	cntIter+=1 #update iterations
	#Input of suffix from user
	strIn=raw_input("\nPlease enter a suffix that is\n"\
				+ "at least four characters long.\n"\
				+ "->Need help? Enter: help\n"\
				+ "->Want to exit? Enter: quit\n")				
	#Check input
	if (strIn == "quit"):
		bookIn.close()
		sys.exit()								
	if (strIn == "help"):
		print "\nTry: gent, dent, nich, lich, iker, rist, ling,\n"\
			+ "     schaft, itis, sive, rung, bung, chen, icht,\n"\
			+ "     ship, tion, ious,lein, ment, ness, heit, keit\n"
		cntIter-=1
		continue
	inputIsOK = (len(strIn)>=4 and not (strIn in lstIn))
	if not inputIsOK:
		if (strIn in lstIn):
			print "\nYou already entered: <%s>. Try again." % (strIn)	
		else:
			print "\nYou entered: <%s>. Try a longer one." % (strIn)
		cntIter-=1
		continue
	else:
		print "\nYou entered: <%s>.\n" % (strIn)
		lstIn+=[strIn] #update user input list
	#Search	
	cntFndWrds=0 # counter of words found in one round
	lstFndWrds=[] #list of words found in one round
	for strWord in lstBookIn:
		strWordLengthOK=(len(strWord)>len(strIn)) #otherwise it's not a suffix
		wordMatch=(strIn==strWord[-4:]) #the suffix matches
		if not (strWordLengthOK and wordMatch):
			continue
		#update list, flag and counters
		lstFndWrds+=[strWord] 
		cntFndWrds+=1
		cntFndWrdsTotal+=1
		enoughWordsFound=(cntFndWrdsTotal>=150)
	#Search Results for round cntIter
	lstFndWrdsTotal+=lstFndWrds
	print "Round %d: Suffix <%s> was found %d times."\
	% (cntIter, strIn, cntFndWrds)
	if (len(lstIn)>1):
		strLstIn= ', '.join(map(str, lstIn)) #convert list to string
		print "Round %d: Suffixes <%s>\n        were found %d times."\
				% (cntIter, strLstIn, cntFndWrdsTotal)
#Summary output
#How many and which suffixes were entered
nrOfUserInputs=len(lstIn)
print "\n---Summary:----\n"\
	+	"You entered the following %d suffixes: \n" % (nrOfUserInputs)\
	+ strLstIn
#How many different words have been found
setFndWrdsTotal=sorted(set(lstFndWrdsTotal))
nrOfDiffWords= len(setFndWrdsTotal)
print "\nThe following %d different words " % (nrOfDiffWords)\
	+ "have been found: "
print "\n".join(setFndWrdsTotal)
#Which and how long are the 5 longest words
setFndWrdsTotal_5Longest=setFndWrdsTotal[:5]
it=iter(setFndWrdsTotal_5Longest)
lstOfTpl=[(len(x),x) for x in it]
print "\nThe five longest words found and their length:\n"
for intWrdLen, strWrd in lstOfTpl:
	print "word\t <%s>    \thas length <%d>\n" % (strWrd, intWrdLen)
#Close book
bookIn.close()

