#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PCL I, Übung 5, HS15
# Aufgabe 5
# Autoren: 		'Roland Bend' AND 'Lennart von Thiessen'
# OLAT names: 	'rolben' AND 'lvthiessen' 
# Matrikel-Nr.: '97-923-163' AND '11-185-790'
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Aufruf des Programms: python Aufgabe5.py wordlength startingCharacter
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Define functions and imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import sys
import nltk, operator
from nltk.corpus import webtext

def printresult(dict):
	"""
		PRE: 'dict' is a not empty dictionary
		POST: Sorts the dictionary and prints the (key,value)-pair with the highest value
				(if there are more pairs with the same value, both are printed).
	"""
	dict_sorted = sorted(dict.items(), key = operator.itemgetter(1), reverse=True) #sortiert dict nach Wert

	res = [dict_sorted[0]]
	freq = res[0][1]
	for i in range(1, len(dict_sorted)):
		if(dict_sorted[i][1] == freq):
			res.append(dict_sorted[i])
		else:
			break

	for tupel in res:
		print str(tupel[0]) + ' : ' + str(tupel[1])

def dictLen(text, length):
	"""
		PRE: 	'text' is a text in list format that is not empty (each word is an item)
				'length' is the length of the words you are looking for
		POST: returns a dictionary. Each entry is (key, value) = (word_(with 'length' letters), frequency)
	"""
	dict_tmp = {}
	for ele in text:
		if(len(ele) == int(length)):
			if(ele in dict_tmp):
				dict_tmp[ele] += 1
			else:
				dict_tmp[ele] = 1
	return dict_tmp

def dictChar(text, char):
	"""
		PRE: 	'text' is a text in list format that is not empty (each word is an item)
				'char' is the first character of the words you are looking for
		POST: returns a dictionary. Each entry is (key, value) = (word_(starts with 'char'), frequency)
	"""
	dict_tmp = {}
	for ele in text:
		if(ele[0] ==  char):
			if(ele in dict_tmp):
				dict_tmp[ele] += 1
			else:
				dict_tmp[ele] = 1
	return dict_tmp

def dictLenChar(dictLen, char):
	"""
		PRE: 	'dictLen' is a dictionary with (key, values) = (word, freq) where all words have the same length 
				'char' is the first character of the words you are looking for
		POST: returns a dictionary. Each entry is (key, value) = (word_(starts with 'char'), frequency)
				and all words have the same amount of letters
	"""
	dict_tmp = {}
	for ele in dictLen:
		if(ele[0] == char):
			dict_tmp[ele] = dictLen[ele]
	return dict_tmp

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Start Program
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# import the arguments
length = sys.argv[1]
char = sys.argv[2]

print ""
print 'START------------------------------------------------------'
print "Aufgabe 5 (length=" + length + ", character='" + char + ")" 
print '-----------------------------------------------------------'

text = webtext.words('grail.txt')

print "Häufigstes Wort mit " + str(length) + " Buchstaben:"
printresult(dictLen(text, length))

print "Häufigstes Wort mit Anfangsbuchstabe '" + char + "':"
printresult(dictChar(text, char))

print "Häufigstes Wort mit " + str(length) + " Buchstaben und Anfangsbuchstabe '" + char + "':"
printresult(dictLenChar(dictLen(text, length), char))
print 'END------------------------------------ lvthiessen | rolben'
print ""





