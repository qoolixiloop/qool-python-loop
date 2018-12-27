#!/usr/bin/env python
# -*- coding: utf-8 -*-

#PCL I, Übung 3, HS15
#Aufgabe 5
#Autor: Roland Benz
#Matrikel-Nr.: 97-923-163 

#Debug:  python -m pdb <fileName.py>


'''
###import packages
import sys ## necessary for command line arguments
import re  ## necessary for regular expressions
import codecs ##necessary to read file as UTF-8

###OOP define main function (beginn)
def fkt(arg, arg):
	#Your code
def main():
	#Your code
	#fkt(arg,arg)
#call the function main (end)
if __name__ == '__main__':
	main()

###Command line arguments
inFilename = sys.argv[1] #get the filename	
outFilename = sys.argv[2] #get the filename	

###open file buffer
infile = codecs.open(inFilename, 'r', encoding='utf-8')
outfile = codecs.open(outFilename, 'w', encoding='utf-8')

###for each line in the input file buffer
for strLine in infile:
	
	# strip away the \n symbol
	strLineCleaned = strLine.rstrip()
	
	# split the line into a list of strings
	lstWord = strLineCleaned.split()
	
	# for each word in the line		
	for strWord in lstWord:
	
		# write output to the file
		outfile.write(strWord)
		
	# for each word in the line
	for strWord in lstWord:
		# if the word is not in the lexicon list, then add it
		if strWord not in lstLexicon:
			lstLexicon.append(strWord)

###for each element in the list	
for strWord in lstLexicon:

	# split the word in all possible ways
	# the first element must be at least 3 characters long
	# and the last element must be at least 3 characters long
	for position in range(3, len(strWord)-2):
	
		#check if both parts are in the lexicon
		if strWord[0:position] in lstLexicon and\
			strWord[position:] in lstLexicon:
			print 'Found compound ', strWord[0:position], strWord[position:]
			compound_counter += 1

### define a hash as a global variable
my_person_hash = {}

# define a function 
def read_and_store_person_names():
		
# for each line in the file
for strLine in infile:

	# strip away the \n symbol
	strLineCleaned = strLine.rstrip()
	
	# split the line into a list of strings
	lstWord = strLineCleaned.split('\t')
	
	name = lstWord[0]
	gender = lstWord[1]
	
	# save the name --> gender pair in a hash
	dictPerson[name] = gender
	
	# add the genitive form of the name
	# example: Tom --> Toms
	name = name + 's'
	
	# save the genitive name --> gender pair in the hash
	dictPerson[name] = gender


### define a hash (= dictionary)
dictLexicon = {'Tante':'aunt', 
	'Polly':'Polly', 
	'sah':'saw', 
	'Mann':'man', 
	'mit':'with', 
	'Fernglas':'telescope', 
	'im':'in the', 
	'Garten':'garden', 
	'dem':'the', 
	'der':'the', 
	'den':'the' }
	
# convert the sentence into a list
strTestSentence = 'Tante Polly sah den Mann im Garten mit dem Fernglas'
lstTestSentence = test_sentence.split()
	
# work through the list and translate each word
for strWord in lstTestSentence:
	# if the word is in the lexicon as key
	if strWord in dictLexicon:
		print dictLexicon[strWord],	
	else:
		print '\n >>>', strWord, ' is unknown!!! :-('


###test sentences with Part-of-Speech tags
strTestSentence = 'Tante#NN Polly#NE hat#VAFIN den#ART Mann#NN mit#APPR dem#ART Fernglas#NN gesehen#VVPP'
lstTestSentence = strTestSentence.split()

#initialize a list to hold tuples of word + PoS tag
lstTplWordPOSTag= []

#create a new list where each pair of word + PoS tag is a tuple
for strWordPosPair in lstTestSentence:
	(word, pos) = strWordPosPair.split('#')
	lstTplWordPOSTag.append((word,pos))

#for each word + pos-tag pair do
i = 0
vvpp_position = 0
for tplWordPOSTag in lstTplWordPOSTag:
	# if the current PoS tag is a finite auxiliary verb
	if (tplWordPOSTag[1] == 'VAFIN'):
		vafin_position = i
	# else if the current PoS tag is a full verb in past participle 
	elif (tplWordPOSTag[1] == 'VVPP'):
		vvpp_position = i
		tplVVPP = tplWordPOSTag
	# index for the position in the list
	i += 1

# if we found a full verb in past participle
if (vvpp_position > 0):
	# remove the VVPP tuple from its original position
	lstTplWordPOSTag.pop(vvpp_position)
	# insert the VVPP tuple after the VAFIN
	lstTplWordPOSTag.insert(vafin_position+1, tplVVPP)
	
# work through the list and translate each word
for tplWordPOSTag in lstTplWordPOSTagt:
	word = tplWordPOSTag[0]
	# if the word is in the lexicon as key
	if word in dictLexicon:
		print dictLexicon[word],	
	else:
		print '\n >>>', word, ' is unknown!!! :-('


###program to count _German_ PoS tags in a Text+Berg file in 3-column format
dictPOSTag = {}
for strLine in infile:

	# check if the line contains a language attribute
	regexMatch = re.search(' lang="([^"]+)', strLine)
	# store the current language
	if regexMatch:
		curr_lang = regexMatch.group(1)
	
	# check if the line contains a part-of-speech tag
	regexMatch = re.search('\t([^\t]+)\t', strLine)
	# alternative:
	# (word, pos_tag, lemma) = strLine.split('\t')
	
	# if the line contains a pos tag and the current language is German
	if regexMatch and (curr_lang == 'de'):
		# store the pos tag
		posTag = regexMatch.group()
		word_counter += 1
					
		#if Pos-tag is already in the hash add counter
		if posTag in dictPOSTag:
		#alternative:
		#if dictPOSTag.has_key(pos_tag):
			#increment the counter
			dictPOSTag[posTag] += 1
		#if Pos-tag is not yet in the hash add Pos-Tag
		else:
			#instantiate the counter
			dictPOSTag[posTag] = 1				
			
lstTplPOSTag = []
#frequency + POS-Tag
for posTag, freq in dictPOSTag.items():
	lstTplPOSTag.append((freq,posTag))

for tpl in sorted(lsttplPOSTag):
	freq = tpl[0]
	posTag = tpl[1]
	print freq, '\t', posTag
print "Found", word_counter, "PoS tags"


###program to count _German_ ADJA-NN sequences (= simple NPs) in file with 3-column format
dictNP = {}
for strLine in infile:

	#check if the line contains a lang attribute
	regexMatch = re.search(' lang="([^"]+)', strLine)
	
	# store the current language
	if regexMatch:
		curr_lang = regexMatch.group(1)
	
	#check if the line contains a word
	#regexMatch = re.search('^([^\t]+)', strLine)
	
	#check if the line contains a lemma
	regexMatch = re.search('\t[^\t]+\t([^\n]+)', line)
	
	#if the line contains a word and the current language is German
	if regexMatch and (curr_lang == 'de'):
		curr_word = regexMatch.group(1)
	
		#check if the line contains a part-of-speech tag
		regexMatch = re.search('\t([^\t]+)\t', line)		
		#if the line contains a pos tag
		if regexMatch:
			#store the pos tag
			curr_pos_tag = regexMatch.group(1)
	
		if (last_pos_tag == 'ADJA') and (curr_pos_tag == 'NN'):
			np = last_word + ' ' + curr_word
			np_counter += 1
					
			#if np is already in the hash
			if dictNP.has_key(np):
				#increment the counter
				dictNP[np] += 1
			#if np is not yet in the hash
			else:
				#instantiate the counter
				dictNP[np] = 1
	
	#store the current word and current pos tag for the next iteration
	last_word = curr_word
	last_pos_tag = curr_pos_tag			

#close file
infile.close()
outfile.close()	
'''
