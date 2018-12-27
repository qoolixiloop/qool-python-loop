#!/usr/bin/python

# program to do word-by-word translation based on a bilingual dictionary
# by Martin Volk

# define a hash (= dictionary)
my_lexicon = {'Tante':'aunt', 
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
test_sentence = 'Tante Polly sah den Mann mit dem Fernglas'
test_sentence = 'der Mann sah die Tante Polly mit dem Fernglas'
# test_sentence = 'Tante Polly sah den Mann im Garten'
test_sentence = 'Tante Polly sah den Mann im Garten mit dem Fernglas'
print 'Input sentence:', test_sentence
# convert the sentence into a list
test_list = test_sentence.split()
print 'Output sentence:',
# work through the list and translate each word
for word in test_list:
	## if the word is in the lexicon as key
	if word in my_lexicon:
		print my_lexicon[word],	
	else:
		print '\n >>>', word, ' is unknown!!! :-('
print		
print '---------------------'	
	
