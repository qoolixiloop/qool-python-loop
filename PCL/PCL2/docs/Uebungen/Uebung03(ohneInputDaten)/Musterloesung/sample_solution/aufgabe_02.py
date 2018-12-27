#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# PCL2-Ü3-Aufgabe 2
# Musterlösung von Raphael Balimann (raphael.balimann@uzh.ch) - HS 2015
#
import nltk
import aufgabe_01

# Main function to showcase functionality
def main():

    ham_corpus = aufgabe_01.buildCorpus('enron_data/enron1/ham/')
    spam_corpus = aufgabe_01.buildCorpus('enron_data/enron1/spam/')

    # creating a list from generators to feed to n-gram builder
    ham = [i for i in ham_corpus.words()]
    spam = [i for i in spam_corpus.words()]

    ham2 = build_ngrams(ham,2)
    spam2 = build_ngrams(spam,2)

    print "The bigram 'you may' is ",
    print('IN THE CORPUS' if check_members(ham2,["you","may"]) else 'NOT IN THE CORPUS')
    print "and it is ",
    print('A COLLOCATION' if is_collocation(ham2,["you","may"]) else 'NOT A COLLOCATION')

    variety = get_finals(spam2,["viagra"])
    print "Here are some n-grams with 'viagra' in them, lean back and enjoy!"
    print variety

    viagra_click = uncondprobability(spam2,["viagra","click"])
    print """The bigram 'viagra click' occupies\
        %f percent of the spam messages.""" %(viagra_click*100)

    viagra_works = condprobability(spam2,["viagra","works"])
    print """If the word 'viagra' appears in a spam message,\
        the word 'works' will appear with a probability of\
        %f percent afterwards.""" %(viagra_works*100)

    return

# Wrapper function to build n-grams from a list provided
# Using zip to merge multiple instances of the same list into n-tuples
# Requires modifications to work as a generator
def build_ngrams(raw_token,n):

    return zip(*[raw_token[i:] for i in range(n)])

# Function to check if a list of tokens is present as an n-gram
# Returns True if found, False otherwise
# Checks if sizes of n-gram match, returns False if mismatching
def check_members(ngram_list, token_list):

    if len(token_list) != len(ngram_list[0]):
        return False

    if tuple(token_list) in ngram_list:
        return True

    return False

# Wrapper function to count n-rgams in a list of n-grams
def count_ngram(ngram_list,ngram):

    ngram = tuple(ngram)
    return ngram_list.count(ngram)

# Function to get all n-grams that start with the token found in backgram
# Returns a list of all n-grams found, so it is possible to use further
def get_finals(ngram_list,backgram):

    results = []
    backgram = tuple(backgram)

    if len(ngram_list[0]) != (len(backgram)+1):
        # returning false to signal a problem
        return False

    for ngram in ngram_list:
        if (ngram[0:len(backgram)] == backgram):
            results.append(ngram)

    return results

# Function to see if a n-gram is a collocation
# Based on an arbitrary treshold
# Returns a boolean value for further processing
def is_collocation(ngram_list,ngram):

    # arbitrary value, set low for testing values
    # 1% of all n-grams is a good value though
    treshold = 0.001

    # getting all n-1-grams
    backoffs = get_finals(ngram_list,ngram[:-1])

    if (count_ngram(ngram_list,ngram) / float(len(backoffs)) > treshold):
        return True
    else:
        return False

# Function to get the probability of a n-gram within a corpus
def uncondprobability(ngram_list, ngram):

    if len(ngram) != len(ngram_list[0]):
        # returning false to signal a problem
        return False

    probability = count_ngram(ngram_list,ngram)/float(len(ngram_list))

    return probability

# Function to get the conditional probability of a n-gram within a corpus
# n representing the level
def condprobability(ngram_list, ngram):

    if len(ngram) != len(ngram_list[0]):
        # returning false to signal a problem
        return False

    backoffs = get_finals(ngram_list,ngram[:-1])

    probability = count_ngram(ngram_list,ngram) / float(len(backoffs))

    return probability


# Standard boilerplate to call the main() function to begin the program.
if __name__ == '__main__':
    main()
