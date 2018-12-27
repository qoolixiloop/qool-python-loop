#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PCL-I: Uebung 04 - Aufgabe 1, FS16

# Autoren:
# c(Student, Martikelnummer) -> {'Roland Benz'	: '97-923-163',
#								 'Linus Manser' : '13-791-132'}
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Cazim, Irene, Raffael:
# Wir geben beide Versionen ab. Es reicht eine anzuschauen.
# Linus Version benützt defaultdict(). Diese Datenstruktur kann
# wie eine Matrix in Matlab/R verwendet werden. Entsprechend sind
# seine Funktionsdefinitionen einiges eleganter codiert.
# Rolands Version ist sehr ausführlich dokumentiert. Alle Fragen
# der Aufgabestellung im Main beantwortet und auf Console geprintet.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Fuer die vollständig gelöste d.h. Übung inkl. beantworteten Fragen
# bitte Rolands Lösung anschauen.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Reflexion/Feedback
# a) Fasse deine Erkenntnisse und Lernfortschritte in zwei Sätzen
# zusammen.
# (Ich kann mich Roland nur anschliessen):
# Ich habe gelernt einen Trainingsalgorithmus für einen Classifier
# (Tagger) selber zu programmieren, damit einen Text zu taggen
# und die Ergebnisse mit Accuracy und Confusionsmatrix zu
# evaluieren. Zweite Erkenntnis: Die Verwendung von 'defaultdicts' 
# erleichtert einem das Leben.
# b) Wie viel Zeit hast du in diese Übungen investiert?
# Linus ~12 Stunden
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from __future__ import division #instead of casting to floats and potentially forgetting to do so
from nltk.corpus import brown
from collections import defaultdict
import operator


def dict_builder(sent_list):
	"""
	function to build a uni- and bigram-dictionary

	input: sentence as a list containing single words
		>>> [('Es','PRON'), ('ist','VERB'),...]
	output: dictionary containing all occured tag/word-combination 
		with the corresponding POS-tag-frequencies for 
		the word - for uni- and bigrams.
	"""
	# initiating dictionnaries (nested dictionnaries)
	unigram_dict = defaultdict(lambda: defaultdict(int))
	bigram_dict = defaultdict(lambda: defaultdict(int))

	for sent in sent_list:
		
		for i in range(0,len(sent)):
			current_word = sent[i][0]
			
			prev_tag = sent[i-1][1]
			
			current_word_tag = sent[i][1]
			tup = (prev_tag, current_word)

			# updating the dictionaries (uni and bigram)
			# bigram
			bigram_dict[tup][current_word_tag] += 1
			# unigram
			unigram_dict[current_word][current_word_tag] += 1
	
	# returns a tuple with the two dictionaries (uni- and bigram)
	return (bigram_dict, unigram_dict)


def the_glorious_zebra_butt():
	"""
	oh, glorious zebra butt, tell us your secret!
	"""
	pos_tag = "NOUN" # returns 'NOUN' pos-tag as a last resort ('NOUN' is the most common pos_tag)

	return pos_tag


def unigram_tagger(word, dictionary, backoff_tagger=the_glorious_zebra_butt):
	"""
	backoff-tagger in case the pos_tag-word-combination doesn't
	exist as key in the dictionary
	returns the most probable pos_tag for a given word
	if the unigram is oov, ask the_glorious_zebra_butt for guidance (backoff-"tagger")
	"""
	try:
		pos_tag = max(dictionary[word].iteritems(), \
			key=operator.itemgetter(1))[0]
	except ValueError:
		pos_tag = backoff_tagger()

	return pos_tag

def bigram_tagger(sent_list, dictionary, backoff_tagger=None, backoff_dictionary=None):
	"""
	actual POS-tagger-function
	input: sentence as list or string
	output: tagged sentence as list with tuples ('word','POS-tag')
	"""
	output_list = []

	for sent in sent_list:
		# prev_tag = None <- would be better... nltk fills in a '.' for no-context?! 
		prev_tag = '.'
		sub_list = []
		for i in range(0,len(sent)):
			current_word = sent[i]
			try:
				# save the most frequent tag for this postag/word-combination as 'pos_tag'
				pos_tag = max(dictionary[(prev_tag, current_word)].iteritems(), \
					key=operator.itemgetter(1))[0]

			# backoff	
			except ValueError:
				if backoff_tagger == None:
					pos_tag = "UNKNOWN"
				else:
					pos_tag = backoff_tagger(current_word, backoff_dictionary)

			sub_list.append((current_word, pos_tag))
			prev_tag = pos_tag

		output_list.append(sub_list)

	return output_list


def evaluate(tagged_sents, tagger, dictionary, backoff_tagger=None, backoff_dictionary=None):
	"""
	evaluation function:
	input: tagged sentences, tagger, dictionary, backoff_tagger, backoff_dictionary 
	output: tuple with tagger, eval_dict, #total_pos_tags, #correct_pos_tags, precision
		eval_dict:
		dictionary with each occuring POS-tag as key and the corresponding
		frequencies of proposed_tags for it
		>>>	{"NOUN": {"NOUN":100, "VERB":2,...}}
						v
					 correct
	"""
	eval_dict = defaultdict(lambda: defaultdict(int))

	# build sentence list without tags to let the tagger do its work
	# this newly tagged list will be compared to the gold standard, which is
	# the same list with the pre-annotated tags
	test_sents = []

	for sent in tagged_sents:
		test_sent = []
		for tup in sent:
			word = tup[0]
			test_sent.append(word)
		test_sents.append(test_sent)
	
	# depending on whether a backoff_tagger is given, call function differently
	if backoff_tagger == None and backoff_dictionary == None:
		result = tagger(test_sents, dictionary)
	else:
		result = tagger(test_sents, dictionary, backoff_tagger, backoff_dictionary)

	gold = tagged_sents

	total_pos_tags = 0

	for i in range(0,len(gold)):
		for x in range(0,len(gold[i])):

	 		proposed_tag = result[i][x][1]
	 		correct_tag = gold[i][x][1]
	 		if proposed_tag == correct_tag:
	 			eval_dict[correct_tag][correct_tag] += 1
	 		else:
	 			eval_dict[correct_tag][proposed_tag] += 1

	 		# increment total_pos_tags count by 1
	 		total_pos_tags += 1

	correct_pos_tags = 0
	# computing the total number of correct pos_tags
	for key in eval_dict:
		correct_pos_tags += eval_dict[key][key]

	precision = correct_pos_tags / total_pos_tags

	evaluation = (tagger, eval_dict, total_pos_tags, correct_pos_tags, precision)

	return evaluation


def display_evaluation(evaluation):
	"""
	input: evaluation-function (tuple)
	prints out the evaluation like so:

		total_pos_tags   : #
		correct_pos_tags : #
		precision        : %

	"""
	(tagger, eval_dict, total_pos_tags, correct_pos_tags, precision) = evaluation
	# displaying precision (printed)
	return "%s\n%-17s: %i\n%-17s: %i\n%-17s: %f" % (tagger, "total_pos_tags", total_pos_tags, "correct_pos_tags", correct_pos_tags,\
		"precision", precision)


def display_confusionmatrix(evaluation):
	"""
	input: evaluation
	prints out a confusionmatrix
	"""
	(tagger, eval_dict, total_pos_tags, correct_pos_tags, precision) = evaluation

	# key_list with keys for the first coloumn
	col_key_list = []

	for key in eval_dict:
		col_key_list.append(key)

	# sorting the list
	col_key_list.sort()

	# to integrate the "UNKNOWN" tag into the key_list, I created a new list, which takes in the 
	# additional pos_tag, which normally isn't in the universal tagset.
	row_key_list = []

	for key in col_key_list:
		row_key_list.append(key)

	row_key_list.append("UNKNOWN")

	##start of formatting the matrix
	# header (first row)
	print "\n","%-5s%s" % ("", "|"),
	for key in row_key_list:
		print '%-7s' % (key),


	# horizontal dividing line
	print "\n", (len(row_key_list)+1)*8* "-"
	
	# actual content rows
	for key in col_key_list:

		row = []
		for i in range(0, len(row_key_list)):

			row.append(eval_dict[key][row_key_list[i]])
		
		output_row = ['%-8i' % (x) for x in row]
		# each content line 
		print '%-5s%s' % (key, "|"), "".join(output_row)



def main():
	print "~~~~~~~~~~~~~beginning of script~~~~~~~~~~~~~~~~"
	# loading the corpus
	print "LOADING CORPUS:\n"
	tagged_sents = brown.tagged_sents(categories="belles_lettres", tagset="universal")
	print "splitting corpus in ratio 90(training)/10(test)...",

	slice_index = int(len(tagged_sents)*0.9)
	training_corpus = tagged_sents[:slice_index]
	test_corpus = tagged_sents[slice_index:]

	print "done"
	print "training corpus: %i sentences (%i words)" % \
		(len(training_corpus), sum([len(x) for x in training_corpus]))
	print "test corpus: %i sentences (%i words)" % \
		(len(test_corpus), sum([len(x) for x in test_corpus]))

	print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	print "TRAINING:\n"
	print "building bigram and unigram dictionaries...",
	(bigram_dict, unigram_dict) = dict_builder(training_corpus)
	print "done"

	print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	print "TAGGING:\n"
	print "Tag the sentence 'This is a sentence we want to tag' without backoff:"
	print bigram_tagger([["This", "is", "a", "sentence", "we", "want", "to", "tag"]\
			,[]], bigram_dict)
	print "\nTag the sentence 'This is a sentence we want to tag' with backoff:"
	print bigram_tagger([["This", "is", "a", "sentence", "we", "want", "to", "tag"],[]]\
			, bigram_dict, unigram_tagger, unigram_dict)
	print "\nAnswer to the question:"
	print "The problem here is, that once the 'UNKNOWN'-tag appeares, it 'corrupts' all"
	print "following (pos_tag,word)-checks. This has the consequence that every following"
	print "word is labelled as 'UNKNWON'."

	print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	print "EVALUATION with CONFUSIONMATRIX:\n"

	print "without backoff:"
	evaluation_without_backoff = evaluate(test_corpus, bigram_tagger, bigram_dict)
	print display_evaluation(evaluation_without_backoff)
	display_confusionmatrix(evaluation_without_backoff)

	print "\nwith backoff:"
	evaluation_with_backoff = evaluate(test_corpus, bigram_tagger, bigram_dict, unigram_tagger, unigram_dict)
	print display_evaluation(evaluation_with_backoff)
	display_confusionmatrix(evaluation_with_backoff)
	print "\n~~~~~~~~~~~~~~~~~end of script~~~~~~~~~~~~~~~~~~"


if __name__ == '__main__':
	main()