##Useful Python Code Snippets

#start of each programm
'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-

#PCL I, Übung 3, HS15
#Aufgabe 5
#Autor: Roland Benz
#Matrikel-Nr.: 97-923-163 
'''

#imports
'''
import sys
import os.path #file system
from random import choice #choice method from random numbers
import string #string object
from string import lowercase #lowercase method from string
'''

#start pdb debugger
'''
#1. Method: 
#bash command: python -m pdb <fileName.py>

#2. Method: 
#add in fileName.py following code and execute 
dBug=False
if dBug:                  
	import pdb
	pdb.set_trace() 
'''

#command line arguments
'''
import sys
strPathAndFilename=""
try:
	strPathAndFilename=sys.argv[1] #Throws an IndexError Exception
except:
	strPath="/media/benzro/OS/Users/benzro/Documents/"\
			+"LubuntuShared/8) PCL-1/Übungen/PCL_uebung3_python/"
	strFilename="moby_dick.txt" 
	strPathAndFilename=strPath+strFilename
'''

#bject oriented, define class, static variables, instance variables, methods
'''
class RandomNrTesting:
	#class variable shared by all instances
	randomNrTest=0 #to index test runs (not needed here)
	#init
	def __init__(self, howMany, randLow, randHigh):
		# instance variable unique to each instance
		self.howMany=howMany
		self.randLow=randLow
		self.randHigh=randHigh
		self.lstNumbers = [] 
		self.randomNrTest+=1
		self.getRandomList()
	#creates a list of random numbers
	def getRandomList(self):
		for i in range(self.howMany):
			self.lstNumbers.append(random.randint(self.randLow,self.randHigh))
		return self.lstNumbers
'''

#Open (and read) book
'''
import os.path
fileExists=os.path.isfile(strPathAndFilename)
if not fileExists:
	print "The file\n %s" % (strPathAndFilename)\
			+	"does not exist. Exit process.\n"
	sys.exit() #kills the phyton interpreter process
else:
	try:
		bookIn=open(strPathAndFilename, "r") #Throws an Exception
		#Comment next two lines, otherwise bookIn is in EOF state 
		#when trying to iterate with: for line in bookIn.readlines():
		strBookIn=bookIn.read()
		lstBookIn=strBookIn.split() #"\n" does not remove blank and \r
	except:
		print "Could not open the file %s\n" % (strPathAndFilename)\
				+ "\nExit process.\n"
'''

#Read book and make list of tokens
'''
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
'''

#declare data structures
'''
#Variables and containers
strIn="" #string of user input
lstIn=[] #list of user inputs
strLstIn="" #string of list of user inputs
lstFndWrdsTotal=[] #list of found words in total
setFndWrdsTotal=set() #unique list or set of found words in total
cntFndWrdsTotal=0 #counter of found words in total
'''

#command line dialog with user
'''
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
'''

#search list and convert list to string
'''
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
'''

#set data structure
'''
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
'''

#dictionary data structure: iterate through dictionnary
'''
lstOfTplKeyValuePairsOfDictSAC=dictSAC.items()
#unsorted
print "\nUnsorted list of tuples\n"
for elem in lstOfTplKeyValuePairsOfDictSAC:
	if len(elem[1])>5:
		print "Name: %s \t Long mountain name: %s" %(elem[0], elem[1])
#sorted
print "\nSorted list of tuples, sorted on first tuple element x[0]\n"
lstsortedOfTplKeyValuePairsOfDictSAC = sorted(lstOfTplKeyValuePairsOfDictSAC,key=lambda x: x[0])
for elem in lstsortedOfTplKeyValuePairsOfDictSAC:
	if len(elem[1])>5:
		print "Name: %s \t Long mountain name: %s" %(elem[0], elem[1])
'''

#dictionary data structure: access and print dictionnary items
'''
#extract and print selected key-value pairs as dictionnary
dictSomePairs = {key: dictLongTokens[key] for key in dictLongTokens.keys()[10:60]}
print "\nb) Print some pairs as dictionary:\n %s \n" %(dictSomePairs)

#extract and print selected key-value pairs as separate key value strings
print "\nb) Print some pairs as key and value variables:"
for key,value in dictLongTokens.items()[10:30]:
		print "Key: %s \t value: %s" %(key,value)

#sort, extract and print chosen key-value pairs as separate key value strings
print "\nc) Dictionary sorted by key:\n"\
	+ "   (print only the first 20)" 
for key, value in sorted(dictLongTokens.items())[:20]:
  print "Key: %s \t value: %s" %(key,value)

#
print "\nc) Dictionary sorted by value:\n"\
	+ "   (print only the largest 20)" 
lstOfTplDictLongTokens = list(dictLongTokens.items())
lstOfTplTop20 = sorted(lstOfTplDictLongTokens, key=lambda tup: tup[1])[-20:]
for elem in lstOfTplTop20:
  print "Key: %s \t value: %s" %(elem[0],elem[1])
'''

#dictionary data structure: update and print dictionnary
'''
#store new key value pair in newdictionnary
newKeyValuePair={"Benz":"Uetliberg"}
strNewKeyValuePair=str(newKeyValuePair)
print "New key-value pair:\n %s\n" % (strNewKeyValuePair)

#update dictionary with new key value pair
dictSAC.update(newKeyValuePair)
strSAC=str(dictSAC)
print "SAC Dictionary:\n %s\n" % (strSAC)
'''

#string data structure
'''
#Solution 1
i=0			
for char in strLongWrd:
	i+=1
	charPosABC = string.lowercase.index(char) + 1
	strToPrint = "".join(char for i in range(charPosABC))
	print " %d : <%d> \t %s \n" % (i,charPosABC,strToPrint)
	#print "%d:   " + strToPrint + "\n"	% (i)
	
#Solution 2
i=0
for char in strLongWrd:
	i+=1
	charPosABC = string.lowercase.index(char) + 1
	strToPrint = char * charPosABC	
	print " %d : <%d> \t %s \n" % (i,charPosABC,strToPrint)
		
#With randomized strings
i=0
for char in strLongWrd:
	i+=1
	charPosABC = string.lowercase.index(char) + 1
	strToPrint = "".join(choice(lowercase) for i in range(charPosABC))	
	print " %d : <%d> \t %s \n" % (i,charPosABC,strToPrint)
'''

#list data structure
'''
#a) am Ende der Liste ein Ausrufezeichen anhängt
lstText_a = lstText + ["!"]

#b)der Liste die Wörter des Satzes ’Dies ist mein Satz’ hinzufügt
strText_b = "Dies ist mein Satz"
lstText_b = strText_b.split(" ")
lstText_b = lstText + lstText_b

#c)die Anzahl der Vorkommen des Tokens ’ist’ ermittelt und mitteilt
intCntIst_c=0
for word in lstText_b:
	if word == "ist":
		intCntIst_c +=1
print "Das Wort \"ist\" kommt " + str(intCntIst_c) + " Mal vor."

#d)das erste Vorkommen von ’&’ aus der Liste entfernt 
iter=0
lstText_d=[]
for word in lstText_b:	
	if word == "%":
		lstText_d = lstText_b
		del lstText_d[iter]
		break
	iter+=1	
print lstText_d

#e)'%' vor dem dritten Element (achte auf Index!) das Wort ’so’ einfügt
lstText_e = lstText_d
lstText_e.insert(2,"so")	
print lstText_e	

#f)das erste Element mit dem Wort ’Computerlinguistik’ ersetzt (d.h. Anzahl Elemente bleibt gleich)
lstText_f = lstText_e
lstText_f[0] = "Computerlinguistik"
print lstText_f

#g)das erste Vorkommen von ’sehr’ mit ’unglaublich’ ersetzt (schwieriger)
iter=0
lstText_g=[]
for word in lstText_f:	
	if word == "sehr":
		lstText_g = lstText_f
		lstText_g[iter] =  "unglaublich"
		break
	iter+=1	
print lstText_g
'''
