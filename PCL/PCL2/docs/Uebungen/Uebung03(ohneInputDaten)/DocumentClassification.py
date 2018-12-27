#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#used corpora as data input
from nltk.corpus import movie_reviews

#used functionality for ML
import operator
import random
import nltk

#feature extractor functions

def document_features(document, word_features):
    """
        A feature extractor for document classification, whose features indicate whether or not
        individual words are present in a given document.
        """
    document_words = set(document)
    features = {}
    for word in word_features:
        #features[key]=value, key=word, value=True/False
        features['contains(%s)' % word] = (word in document_words)
    return features


# Main
if __name__ == "__main__":
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "6.1 Supervised Classification" \
          "Classification is the task of choosing the correct class " \
          "label for a given input. In basic classification tasks, " \
          "each input is considered in isolation from all other inputs, " \
          "and the set of labels is defined in advance. A classifier is " \
          "called supervised if it is built based on training corpora " \
          "containing the correct label for each input."
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "E X A M P L E 3: Document Classification"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "Document Classification. " \
          "corpora where documents have been labeled with categories." \
          " Using these corpora, we can build classifiers that will " \
          "automatically tag new documents with appropriate category " \
          "labels. First, we construct a list of documents, labeled " \
          "with the appropriate categories (here: category=pos/neg )"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "length: ",len(movie_reviews.fileids())
    documents = [(list(movie_reviews.words(fileid)), category)
        for category in movie_reviews.categories()
        for fileid in movie_reviews.fileids(category)]
    random.shuffle(documents)
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "print two documents in data structure" \
          "[([text-tokens],category=pos/neg)," \
          "([text-tokens],category=pos/neg),...]"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print documents[0:2]
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "access elements (and part of it) in a list of tuples"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    for text, cat in documents[0:10]:
        if cat == u'pos':
            print cat, text[1:10]
    for text, cat in documents[0:10]:
        if cat == u'neg':
            print cat, text[1:10]
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "To limit the number of features that the classifier needs " \
          "to process, we begin by constructing a list of the 2,000 " \
          "most frequent words in the OVERALL corpus"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
    print (all_words.items())[1:10]
    print (all_words.keys())[1:10]
    print (all_words.values())[1:10]
    word_features = all_words.keys()[:2000]
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print " We can then define a feature extractor that simply checks " \
          "whether each of these words is present in a given document."
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    features = document_features(movie_reviews.words('pos/cv957_8737.txt'),
                            word_features)
    print features.items()[1:10]
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "...whether each of these words is present in EACH of the " \
          "given documents. "
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    featuresets = [(document_features(d,word_features), c)
                   for (d, c) in documents]
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "print elements in data structure" \
          "[({text-tokens of document 1:True/False},category=pos/neg)," \
          "({text-tokens of document 2:True/False},category=pos/neg),...]"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "length: ", len(featuresets)
    print featuresets[0:2]
    for text_dict, cat in featuresets[0:10]:
        if cat == u'pos':
            print cat, text_dict.items()[1:5]
    for text, cat in documents[0:10]:
        if cat == u'neg':
            print cat, text_dict.items()[1:5]
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "Now that we’ve defined our feature extractor, we can use " \
          "it to train a classifier to label new movie reviews"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    train_set, test_set = featuresets[100:], featuresets[:100]
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "At that point, we can use the test set to evaluate how well" \
          " our model will perform on new input values"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print nltk.classify.accuracy(classifier, test_set)
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "Apparently in this corpus, a review that mentions triple " \
          "is almost 8 times more likely to be negative than positive, " \
          "while a review that mentions fabric is about 6 times more " \
          "likely to be positive. " \
          "(for each run something else; because of random shuffle" \
          "of documents at the beginning, the documents in the " \
          "training set differ for ech run)"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    classifier.show_most_informative_features(5)

    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "End of Script"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"


