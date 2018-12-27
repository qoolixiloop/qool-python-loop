#!/usr/bin/env python
# -*- coding: utf-8 -*-


from __future__ import division

import nltk
from nltk.book import *
from nltk.corpus import wordnet as wn
import re, pprint


#A concordance permits us to see words in context
print "from 1: ", text1.concordance("monstrous")

# What other words appear in a similar range of contexts?
print "from 2: ",text1.similar("monstrous")
print "from 3: ",text2.similar("monstrous")

#the contexts that are shared by two or more words
print "from 4: ",text2.common_contexts(["monstrous", "very"])

#determine the locations of a word in the text
text4.dispersion_plot(["citizens", "democracy",
                        "freedom", "duties", "America"])

#generating some random text
# reuses common words and phrases from the source text
# and gives us a sense of its style and content
#print "from 5: ",text3.generate()

#get the length of something
# So Genesis has 44,764 words and punctuation symbols,
# or “tokens.” A token is the technical name for a sequence
# of characters—such as hairy, his, or :)—that we want
# to treat as a group.
print "from 6: ",len(text3)

#The vocabulary of a text is just the set of tokens that it uses
print "from 7: ",set(text3) #set, vocabulary used
print "from 8: ",sorted(set(text3)) #list, sorted list of vocabulary items

#nr of different tokens used
# this book has only 2,789 distinct words, or “word types.”
# A word type is the form or spelling of the word independently
# of its specific occurrences in a text
print "from 9: ",len(set(text3))

#a measure of the lexical richness of the text.
# each word is used 16 times on average
print "from 10: ",len(text3) / len(set(text3))

#count how often a word occurs in a text,
print "from 11: ",text3.count("smote")

#compute what percentage of the text is taken up by
# a specific word
print "from 12: ",100 * text4.count('a') / len(text4)

#we can use Python’s addition operator on lists
print "from 13: ", ['Monty', 'Python'] + ['and', 'the', 'Holy', 'Grail']

#append
print "from 14: ",sent1.append("Some")

#find the index of when it first occurs
print "from 15: ",text4.index('awaken')

#find the word of an index
print "from 16: ",text4[173]

# replace an entire slice with new material
sent = ['word1', 'word2', 'word3', 'word4', 'word5',
        'word6', 'word7', 'word8', 'word9', 'word10']
sent[0] = 'First'
sent[9] = 'Last'
print "from 17: ",len(sent),"  ",sent  #10
sent[1:9] = ['Second', 'Third']
print "from 18: ",len(sent),"  ",sent #4

#perform multiplication and addition with strings
name = 'Monty'
print "from 19: ",name * 2
print "from 20: ",name + '!'

#join the words of a list to make a single string
print "from 21: ", ' '.join(['Monty', 'Python'])

#split a string into a list
print "from 22: ",'Monty Python'.split()

#use a FreqDist to find the 50 most frequent words
# total number of words (“outcomes”) that have been counted up
fdist1 = FreqDist(text1)
print "from 23: ",fdist1, len(set(text1))
# list of all the distinct types in the text
vocabulary1 = fdist1.keys()
print "from 24: ",vocabulary1[:50]

#These 50 words account for nearly half the book
# Only one word, whale, is slightly informative!
# It occurs over 900 times. The rest of the
# words tell us nothing about the text;
# they’re just English “plumbing.
print "from 25: ",fdist1.plot(50, cumulative=True)

#words that occur once only, the so-called hapaxes
print "from 26: ",fdist1.hapaxes()

#We would like to find the words from the vocabulary of the
# text that are more than 15 characters long. Let’s call this
# property P, so that P(w) is true if and only if w is more
# than 15 characters long. “the set of all w such that w is an
# element of V (the vocabulary) and w has property P
# {w | w ∈ V & P(w)}
# [w for w in V if p(w)]
V = set(text1)
long_words = [w for w in V if len(w) > 15]
print "from 27: ",sorted(long_words)

#automatically identify the frequently occurring con-
# tent-bearing words of the text
# all words from the chat corpus that are longer than
# seven characters, that occur more than seven times
fdist5 = FreqDist(text5)
print "from 28: ", sorted([w for w in set(text5)
                            if len(w) > 7 and fdist5[w] > 7])

#A collocation is a sequence of words that occur together
# unusually often... they are resistant to substitution with
# words that have similar senses
# list of word pairs, also known as bigrams
#print "from 29: ", bigrams(['more', 'is', 'said', 'than', 'done'])

#collocations are essentially just frequent bigrams, except that
# we want to pay more attention to the cases that involve rare
# words. In particular, we want to find bigrams that occur more
# often than we would expect based on the frequency of individual
# words. The collocations that emerge are very specific
# to the genre of the texts
print "from 30: ",text4.collocations()

#distribution of word lengths in a text
print "from 31: ",[len(w) for w in text1]
fdist = FreqDist([len(w) for w in text1])
# a quarter of a million items
print "from 32: ",fdist
# there are only 20 different word lengths
print "from 33: ",fdist.keys()
# how frequent the different lengths of words are
print "from 34: ",fdist.items()

#Increment the count for this sample
#print "from 35: ",fdist1.inc('monstrous')

#Count of the number of times a given sample occurred
# from 36:  10
print "from 36: ",fdist1['monstrous']

#Frequency of a given sample
# from 37:  3.83407650516e-05
print "from 37: ",fdist1.freq('monstrous')


