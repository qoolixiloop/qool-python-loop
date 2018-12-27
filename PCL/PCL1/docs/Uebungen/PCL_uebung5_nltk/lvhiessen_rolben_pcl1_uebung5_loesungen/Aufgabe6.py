#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PCL I, Übung 5, HS15
# Aufgabe 6
# Autoren: 		'Roland Bend' AND 'Lennart von Thiessen'
# OLAT names: 	'rolben' AND 'lvthiessen' 
# Matrikel-Nr.: '97-923-163' AND '11-185-790'
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Aufruf des Programms: python Aufgabe6.py 
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Define functions and imports and global variables
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import nltk
from nltk.corpus import brown

# Define Wwrds and categories
words = [u'money', u'duty', u'love', u'fun']
categories = [u'science_fiction', u'romance', u'government', u'humor', u'religion']


def freq(categories, words):
	"""
		PRE: two not empty lists categories and words
		POST: returns the frequencies of the words (list) in the specified categories (list)
				and returns the result in a 2-Dim list (first dim: categories, second dim: words)
	"""
	counter = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
	
	for i in range(0, len(categories)):

		for word in brown.words(categories=categories[i]):
			for j in range(0, len(words)):
				if(word == words[j]):
					counter[i][j] += 1
	return counter
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# With NLTK
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#cfd = nltk.ConditionalFreqDist(
#	(genre, word)
#	for genre in brown.categories()
#	for word in brown.words(categories=genre))
#categories = [u'news', u'religion', u'hobbies', u'science_fiction', u'romance', u'humor']
#words = [u'money', u'duty', u'love', u'heart']
#cfd.tabulate(conditions=categories, samples=words)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Start Program
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print ""
print 'START-----------------------------------------------------------------------------------------'
print "Aufgabe 6 (no arguments)" 
print '----------------------------------------------------------------------------------------------'

# Calculate frequencies of the words in list 'words' for each category in list 'categories'
fq =  freq(categories, words)
print 'words are:', words
for i in range(0, len(fq)):
	print categories[i],"\n\t->", fq[i][:]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Calculate the relative frequencies with respect to each category
# and print the highest/lowest rel. freq. with the category name for all words.
for i in range(0, len(words)):
	max_val = 0.0
	max_idx = 0
	min_val = 0.0
	min_idx = 0
	for j in range(0, len(categories)):
		# Anteil des Wortes im zugehörigen Text. (Anz. Treffer in category_i / Anz. Worte in category_i)
		# REMARK: Gewisse Anteile sind extrem klein s.d. 0.0% herauskommt.
		tmp = float(fq[j][i])/float(len(brown.words(categories=categories[j])))
		if(tmp > max_val):
			max_val = tmp
			max_idx = j
		elif(tmp < min_val):
			min_val = tmp
			min_ids = j

	print "[ " + words[i] + " ]"
	print "\t Kategorie mit groesstem Anteil ist: ", categories[max_idx], "(", max_val*100, "% )."
	print "\t Kategorie mit kleinstem Anteil ist: ", categories[min_idx], "(", min_val*100, "% )."

print 'END----------------------------------------------------------------------- lvthiessen | rolben'
print ""



