#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# PCL2-Ü3-Aufgabe 3
# Musterlösung von Raphael Balimann (raphael.balimann@uzh.ch) - HS 2015
#
import nltk
import aufgabe_01
import random


# Main function to showcase functionality
def main():

    documents, spam_corpus, ham_corpus = data_builder()

    spam_words = word_builder(spam_corpus)
    ham_words = word_builder(ham_corpus)
    wordlist = spam_words + ham_words
    words = top_words(wordlist)

    featuresets = [(document_features(document,words), classification) for (document,classification) in documents]
    train_set, test_set = featuresets[100:], featuresets[:100]
    classifier = nltk.NaiveBayesClassifier.train(train_set)

    print "Classifier accuracy: ",
    print(nltk.classify.accuracy(classifier, test_set))
    classifier.show_most_informative_features(5)

    return

# Function to build a collection of classifiable data
# Returns the corpus objects as well to save precious computing (and user) time
# Could be much nicer, maybe a good exercise for the final exam?
def data_builder():

    data = []

    spam_path = 'enron_data/full/spam/'   #full data set
    ham_path = 'enron_data/full/ham/'    #full data set

    # spam_path = 'enron_data/enron1/spam/' #testing
    # ham_path = 'enron_data/enron1/ham/' #testing

    spam = aufgabe_01.buildCorpus(spam_path)
    ham = aufgabe_01.buildCorpus(ham_path)

    spam_docs = [(list(spam.words(fileid)), 'spam') for fileid in spam.fileids()]
    ham_docs = [(list(ham.words(fileid)), 'ham') for fileid in ham.fileids()]

    data = spam_docs + ham_docs
    random.shuffle(data)

    return (data,spam,ham)

# Helper function to transform corpus obejcts into a list of words
def word_builder(corpus):

    words = []

    for word in corpus.words():
        words.append(word)

    return words

# Helper function to get the top most frequently used words
def top_words(wordlist):

    max_range = 2000

    all_words = nltk.FreqDist(w.lower() for w in wordlist)
    word_features = list(all_words)[:max_range]

    return word_features

# The infamous document features with a basic example of a feature
# Feel free to play around with the features, the sky's the limit and the accuracy may be your guide
def document_features(document, words):

    document_words = set(document)
    features = {}

    for word in words:

        # a gain of 18% compared to the pure baseline, if there's anything to top that!
        features[u'contains({})'.format(word)] = (word in document_words)

    return features

# # Baseline empty feature to check if classifier runs as expected
# def document_features(document,words):
#
#     return {}

# Standard boilerplate to call the main() function to begin the program.
if __name__ == '__main__':
    main()
