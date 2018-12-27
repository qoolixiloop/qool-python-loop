#!/usr/bin/env python
# -*- coding: utf-8 -*-

#PCL I, Übung 3, HS15
#Aufgabe 2_1
#Autor: Roland Benz
#Matrikel-Nr.: 97-923-163 

'''
2.1 Filtern
Für diese Übung steht das angefangene Programm Aufgabe2_1.py bereit. numbers ist eine Liste,
welche 300 randomisierte Zahlen zwischen 1 und 600 enthält. (Den Rest musst du nicht verstehen,
kannst es aber gerne hier nachlesen.)
Erweitere das Programm nun so, dass es folgendes ausführt:
• die Anzahl der ungeraden sowie der geraden Zahlen ausgeben
• von den ungeraden sowie den geraden Zahlen die fünf grössten absteigend sortiert ausgeben
• die Summe der fünf grössten Zahlen von je den ungeraden und den geraden Zahlen berechnen
und die grössere ausgeben. Teile mit, ob es die Summe der ungeraden oder der geraden Zahlen
ist.
Tipp: Die hier verwendete Liste von Zahlen ist ziemlich gross, so auch die Zahlen. Die Richtigkeit
deines Codes zu kontrollieren ist also erschwert. Es macht hier Sinn, eine zusätzliche Liste mit weniger
und kleineren Zahlen (aber allen möglichen Fällen) zu kreieren, um dein Programm zu testen.
'''

#Debug flag=True and Execute
#or python -m pdb <fileName.py>
dBug=False
if dBug:                  
	import pdb
	pdb.set_trace() 


import random

#Your code
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
	#------------------------------------
	#get number of even entries in Array
	def nrOfEven(self):
		cnt=0
		for elem in self.lstNumbers:
			isEven=(elem % 2 == 0)
			if isEven:
				cnt+=1
		return cnt
	#get number of odd entries in Array
	def nrOfOdd(self):
		cnt=0
		for elem in self.lstNumbers:
			isOdd=(elem % 2 != 0)
			if isOdd:
				cnt+=1
		return cnt
	#------------------------------------
	#get top five even entries sorted and descending (+inf to -inf)
	def top5EvenSorted(self):
		lstTop5=[0,0,0,0,0]
		lstEven=[]
		#find even elements
		i=0
		for elem in self.lstNumbers:
			isEven=(elem % 2 == 0)
			if isEven:
				lstEven.append(elem)
		#find top five even elements
		lstEvenTmp=lstEven
		for i in range(0,len(lstTop5)):
			biggestNum=0
			#find biggest number
			#delete it from lstEvenTemp
			#store it in lstTop5
			for elem in lstEvenTmp:
				#update biggest number 
				if elem > biggestNum:
					biggestNum=elem
			lstEvenTmp.remove(biggestNum) 
			lstTop5[i]=biggestNum	
		return lstTop5
	#get top five odd entries sorted and descending (+inf to -inf)
	def top5OddSorted(self):
		lstTop5=[0,0,0,0,0]
		lstOdd=[]
		#find odd elements
		i=0
		for elem in self.lstNumbers:
			isOdd=(elem % 2 != 0)
			if isOdd:
				lstOdd.append(elem)
		#find top five odd elements
		lstOddTmp=lstOdd
		for i in range(0,len(lstTop5)):
			biggestNum=0
			#find biggest number
			#delete it from lstOddTemp
			#store it in lstTop5
			for elem in lstOddTmp:
				#update biggest number 
				if elem > biggestNum:
					biggestNum=elem
			lstOddTmp.remove(biggestNum) 
			lstTop5[i]=biggestNum	
		return lstTop5
	#------------------------------------
	#calculate sum enties
	def sumOfArrayElements(self,arr):
		sum=0
		for elem in arr:
			sum+=elem
		return sum
	#check which number is larger
	def evenIsLarger(self,even, odd):
		if even>odd:
			return True
		else:
			return False
	#------------------------------------
	def listToString(self):
		return "[" + ", ".join( str(x) for x in self.lstNumbers) + "]"
	def sortedListToString(self):
		lstNumbersSorted= sorted(self.lstNumbers)
		return "[" + ", ".join( str(x) for x in lstNumbersSorted) + "]"


#a)
#die Anzahl der ungeraden sowie der geraden Zahlen ausgeben
randNrTest=RandomNrTesting(301,1,600)
print "\nThe list of random numbers: \n"\
		+ randNrTest.listToString()
print "\nThe sorted list of random numbers: \n"\
		+ randNrTest.sortedListToString()
nrOfEven=randNrTest.nrOfEven()
nrOfOdd=randNrTest.nrOfOdd()
print "\nQuantity of even elements: %d \n" % (nrOfEven)\
	+ "Quantity of even elements: %d \n" % (nrOfOdd)


#b)
#von den ungeraden sowie den geraden Zahlen die fünf 
#grössten absteigend sortiert ausgeben
print "Top five even elements:"
top5EvenSrtd=randNrTest.top5EvenSorted()
i=1
for elem in top5EvenSrtd:
	print "%d : %d \n" % (i, elem)
	i+=1
	
print "Top five odd elements:"
top5OddSrtd=randNrTest.top5OddSorted()
i=1
for elem in top5OddSrtd:
	print "%d : %d \n" % (i, elem)
	i+=1
		

#c)die Summe der fünf grössten Zahlen von je den ungeraden 
#und den geraden Zahlen berechnen und die grössere ausgeben. 
#Teile mit, ob es die Summe der ungeraden oder der geraden Zahlen
#ist
sumTop5Even=randNrTest.sumOfArrayElements(top5EvenSrtd)
sumTop5Odd=randNrTest.sumOfArrayElements(top5OddSrtd)
print "Sum top 5 even: %d; sum top 5 odd: %d \n" % (sumTop5Even, sumTop5Odd)
if randNrTest.evenIsLarger(sumTop5Even,sumTop5Odd):
	print "Sum top 5 even: %d is larger. \n" % (sumTop5Even)
else:
	print "Sum top 5 odd: %d is larger. \n" % (sumTop5Odd)
	
