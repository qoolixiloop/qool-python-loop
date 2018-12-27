#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PCL-I: Uebung 4 - Aufgabe 3, HS15

# Autoren:
# c(Student, Martikelnummer) -> 	{'Roland Benz'			: '97-923-163', 
#									 'Lennart von Thiessen' : '11-185-790'}

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Aufruf des Programms:
# Version 1: python Aufgabe3_RB.py "Aufgabe3_EnglischText.txt" "Aufgabe3_DeutschText.txt" 
# Version 2: python Aufgabe3_RB.py "Aufgabe3_EnglischText.txt" "Aufgabe3_DeutschText.txt" "-sortedBy_frequency"
# Version 3: python Aufgabe3_RB.py "Aufgabe3_EnglischText.txt" "Aufgabe3_DeutschText.txt" "-sortedBy_alphabet"
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Debug:  python -m pdb <fileName.py>

'''
3 Identische Wörter erkennen
Erstelle ein Programm, welches, ähnlich wie in der Vorlesung vorgestellt, zwei Textdateien vergleicht
und die Wörter ausgibt, welche in beiden Dateien vorkommen. Zusätzlich zu den gemeinsamen Wör-
tern sollen auch deren jeweilige Häufigkeiten ausgegeben werden.
Die Wörter und die Häufigkeiten sollten in zwei Varianten welche als Argumente von der Komman-
dozeile mitgegeben wurden, auf der Standardausgabe ausgegeben werden:
• Sortiert nach Alphabet
• Sortiert nach Häufigkeit

'''

print "\n########################################################################"
print 'Hi! Program 3 : Identische Wörter erkennen (started)'
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

#import packages
import sys  ## necessary for command line arguments
import codecs
import operator

#Command line arguments
try:
	inFilename1 = sys.argv[1] #get the filename
	inFilename2 = sys.argv[2] #get the filename	
	option=sys.argv[3]	
except:
	inFilename1= "Aufgabe3_EnglischText.txt" 
	inFilename2= "Aufgabe3_DeutschText.txt" 
	option=False
	#option="-sortedBy_frequency"
	#option="-sortedBy_alphabet"
finally:
	infile1 = codecs.open(inFilename1, 'r', encoding='utf-8')
	infile2 = codecs.open(inFilename2, 'r', encoding='utf-8')


#Erste Datei: Tokenisieren
lstWord1 = [] #Liste aller Tokens aus Datei 1
dictWord1={} #Dictionnary aller Tokens aus Datei 1
for strLine in infile1:
	lstWord = strLine.split()
	for strWord in lstWord:
		lstWord1.append(strWord)
		if strWord not in dictWord1.keys():
			frequency=1 #neu
			dictWord1.update({strWord:frequency})
		else:
			frequency=dictWord1.get(strWord)+1 #bestehend
			dictWord1.update({strWord:frequency})
#print "\n\n", dictWord1
		
#Zweite Datei: Tokenisieren
lstWord2 = [] #Liste aller Tokens aus Datei 1
dictWord2={} #Dictionnary aller Tokens aus Datei 1
for strLine in infile2:
	lstWord = strLine.split()
	for strWord in lstWord:
		lstWord2.append(strWord)
		if strWord not in dictWord2.keys():
			frequency=1 #neu
			dictWord2.update({strWord:frequency})
		else:
			frequency=dictWord2.get(strWord)+1 #bestehend
			dictWord2.update({strWord:frequency})
#print "\n\n", dictWord2

#Dictionnary der gemeinsamen Wörter und ihrer Häufigkeit
dictTplCommonTokensAndFrequency = {} 
for key1,value1 in dictWord1.items():
	for key2, value2 in dictWord2.items():
		#Treffer
		if key2 == key1:
			dictTplCommonTokensAndFrequency.\
				update({key1:[inFilename1,value1,inFilename2,value2]})
			exit
print "\n\n", dictTplCommonTokensAndFrequency

#Dictionnary sortiert nach Häufigkeit der Treffer
dictTplCommonTokens_sortedByFrequency = \
		sorted(dictTplCommonTokensAndFrequency.items(), \
			key=lambda v: v[1][1] if v[1][1]<v[1][3] else v[1][3], reverse = True)
#Dictionnary sortiert sortiert nach Alphabet
dictTplCommonTokens_sortedByAscii = \
		sorted(dictTplCommonTokensAndFrequency.items(), \
			key=lambda k: k[0])

#Output
if option=="-sortedBy_frequency":
	print "\nCommon words, sorted by frequency of common matches:"
	print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	for key, value in dictTplCommonTokens_sortedByFrequency:
		print key, value
elif option=="-sortedBy_alphabet":
	print "\nCommon words, sorted by Ascii coding (alphabet):"
	print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	for key, value in dictTplCommonTokens_sortedByAscii:
		print key, value
else:
	print "\nCommon words, sorted by frequency of common matches:"
	print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	for key, value in dictTplCommonTokens_sortedByFrequency:
		print key, value
	print "\nCommon words, sorted by Ascii coding (alphabet):"
	print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	for key, value in dictTplCommonTokens_sortedByAscii:
		print key, value

#close files
infile1.close()
infile2.close()


print "\n########################################################################"
print "Bye Bye und bis bald! :-)"
print "########################################################################"



##Erste Datei: Tokenisieren
#lstWord1 = [] #Liste aller Tokens aus Datei 1
#for strLine in infile1:
	#lstWord = strLine.split()
	#for strWord in lstWord:
		#lstWord1.append(strWord)

##Zweite Datei: Tokenisieren
#dictTplCommonTokens = {} #Dictionnary mit gemeinsamen Wörtern
#for strLine in infile2:
	#lstWord = strLine.split()
	#for strWord in lstWord:
		##Vergleiche Token von Datei 2 mit Liste der Tokens in Datei 1
		#if strWord in lstWord1:
			##Prüfe ob gemeinsamer Token bereits früher gefunden wurde
			#if strWord not in dictTplCommonTokens:
				#dictTplCommonTokens[strWord] = 1 #neu
			#else:
				#dictTplCommonTokens[strWord] += 1 #bestehend


##dict in Tupeln sortiert nach Häufigkeit
#dictTplCommonTokens_sortedByFrequency = sorted(dictTplCommonTokens.items(), key = operator.itemgetter(1), reverse = True)
##dict in Tupeln sortiert nach Alphabet
#dictTplCommonTokens_sortedByAscii = sorted(dictTplCommonTokens.items(), key = operator.itemgetter(0))


#print "\nCommon words, sorted by frequency:"
#print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
#for key, value in dictTplCommonTokens_sortedByFrequency:
	#print key, value
#print "\nCommon words, sorted by Ascii coding (alphabet):"
#print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
#for key, value in dictTplCommonTokens_sortedByAscii:
	#print key, value
