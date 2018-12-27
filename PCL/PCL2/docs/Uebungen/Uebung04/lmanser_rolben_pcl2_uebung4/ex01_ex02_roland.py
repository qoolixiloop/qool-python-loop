#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PCL-I: Uebung 04 - Aufgabe 1, FS16

# Autoren:
# c(Student, Martikelnummer) -> {'Roland Benz'	: '97-923-163',
#								 'Linus Manser' : '13-791-132'}
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Hinweis für Cazim, Irene, Raffael:
# Wir geben beide Versionen ab. Es reicht eine anzuschauen.
# Linus Version benützt defaultdict(). Diese Datenstruktur kann
# wie eine Matrix in Matlab/R verwendet werden. Entsprechend sind
# seine Funktionsdefinitionen einiges eleganter codiert.
# Rolands Version ist sehr ausführlich dokumentiert. Alle Fragen
# der Aufgabestellung im Main beantwortet und auf Console geprintet.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Reflexion/Feedback
# a) Fasse deine Erkenntnisse und Lernfortschritte in zwei Sätzen
# zusammen.
# Ich habe gelernt einen Trainingsalgorithmus für einen Classifier
# (Tagger) selber zu programmieren, damit einen Text zu taggen
# und die Ergebnisse mit Accuracy und Confusionsmatrix zu
# evaluieren. Zweite Erkenntnis: defaultdict() verwenden.
# b) Wie viel Zeit hast du in diese Übungen investiert?
# Roland 15 Stunden
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


from __future__ import division

#used corpora as data input
from nltk.corpus import brown

#used functionality for ML
import nltk
import random
import operator
import math


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Main
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# set the flags for debug info
debug_train = 0
debug_test = 0
debug_eval = 0


def main():
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    print "1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "load corpus ... \n split it into" \
          " 90 % training set & 10 % test set\n"
    # 1a) Teile dein Korpus in zwei Teile zu je 90 und 10%
    # ----------------------------------------------------

    # load list of sents with tuples of word and tag
    list_of_tagged_sents = brown.tagged_sents(
        categories = "news", tagset = "universal")
    print "list of tagged sents: \n" \
          "(only a subset printed)\n", list_of_tagged_sents[:2]

    # cast ConcatenatedCorpusView object into a list
    list_of_tagged_sents = list(list_of_tagged_sents)

    # load list of tokens (not needed)
    list_of_tokens = brown.words(
        categories = "news")
    print "\nlist of tagged tokens: \n", \
        "(not nedded & only a subset printed)\n", list_of_tokens[:5]

    # info about loaded corpus size
    nr_of_sents_loaded = len(list_of_tagged_sents)
    print "\nnr of sents loaded: ", nr_of_sents_loaded

    nr_of_tokens_loaded = sum(
        [len(x) for x in list_of_tagged_sents])
    print "nr of tokens loaded (from sents): ", nr_of_tokens_loaded

    nr_of_tokens_loaded = len(list_of_tokens)
    print "nr of tokens loaded (from words): ", nr_of_tokens_loaded

    # partition the loaded list of tagged sents
    cut = (int)(nr_of_sents_loaded * 0.9)
    training_set = list_of_tagged_sents[:cut]
    test_set = list_of_tagged_sents[cut:]

    # random shuffle the training_set (not needed)
    # (only works on list not on ConcatenatedCorpusView)
    random.shuffle(training_set)

    print "split loaded list of tagged sents into: \n" \
          " nr of training sents: %s \n nr or test sents: %s" \
          % (cut, nr_of_sents_loaded - cut)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    print "2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "train classifier (tagger) with training set\n"
    # 1b) Implementiere deinen Tagger.
    # Du darfst externen Code benutzen, aber du solltest zeigen,
    # dass du verstanden hast, wie der Tagger genau funktioniert.
    # Wenn der Tagger ein Bigramm noch nicht gesehen hat,
    # sollte er es als unbekannt taggen.
    #
    # Datenstruktur 1: bigrams_with_all_tags_and_cnt
    # {(tag_N-1, token_N):{tag_N_1:cnt_1, tag_N_2:cnt_2, ...},
    #  (tag_N, token_N+1):{tag_N+1_1:cnt_1, tag_N+1_2:cnt_2, ...},
    #  ...}
    # Datenstruktur 2: bigrams_with_most_likely_tag
    # {(tag_N-1, token_N):tag_N_most_likely,
    #  (tag_N, token_N+1):tag_N_most_likely,
    #  ...}
    # ---------------------------------------------------
    bigrams_with_all_tags_and_cnt, bigrams_with_most_likely_tag = \
        train_bigram_tagger(training_set)

    print "tagger_bigram ((tag_N-1, token_N),(most likely tag N)):\n" \
          "(only a subset printed)\n", \
        bigrams_with_most_likely_tag.items()[:20]

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    print "3~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "pos-tag the test set with the bigram tagger\n"
    # 1b) Teste deinen Tagger auf
    # dem Satz “This is a sentence that we want to tag.”
    # Welches Problem tritt auf?
    # Anwort 1b): ..... (siehe console output)
    #
    # data structure: test_set_untagged
    # list of sents containing list of tokens
    # [[token_0, token_1, ...]_sent1,
    #  [token_0, token_1, ...]_sent2, ...]
    #
    # data structure: bigrams_with_most_likey_tag:
    # {(tag_N-1, token_N):tag_N_most_likely,
    #  (tag_N, token_N+1):tag_N_most_likely,
    #  ...}
    #
    # data structure: test_set_tagged
    # [(token_N, tag_N_most_likely),(token_N+1, tag_N+1_most_likely),...],
    # [(token_N, tag_N_most_likely),(token_N+1, tag_N+1_most_likely),...],
    #  ...}
    # ---------------------------------------------------

    # untag the test set
    test_set_untagged = untag_sents_tagged(test_set)

    # tag the test set with tagger
    test_set_tagged = bigram_tagger(
        test_set_untagged, bigrams_with_most_likely_tag)

    print "test set untagged:\n" \
          "(only a subset printed)\n", test_set_untagged[:2]
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "test set tagged with bigram tagger:\n" \
          "(only a subset printed)\n", test_set_tagged[:2]
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "test set tagged with brown.tagged_sents:\n" \
          "(only a subset printed)\n", test_set[:2]

    # tag the sentence "This is a sentence that we want to tag."
    test_sentence = [[(u'This',u'DET'), (u'is',u'VERB'),
        (u'a',u'DET'), (u'sentence',u'NOUN'),
        (u'that', u'ADP'), (u'we', u'PRON'),
        (u'want', u'VERB'), (u'to',u'PRT'),
        (u'tag',u'NOUN'), (u'.',u'.')]]
    test_sentence_untagged = [[u'This', u'is', u'a', u'sentence',
                u'that', u'we', u'want', u'to', u'tag', u'.']]
    test_sentence_tagged = bigram_tagger(
        test_sentence_untagged, bigrams_with_most_likely_tag)

    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "test sentence untagged:\n " \
          "(only a subset printed)\n",\
                test_sentence_untagged[:2]
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "test sentence tagged with bigram tagger:\n " \
          "(only a subset printed)\n",\
                test_sentence_tagged[:2]
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "Antwort 1b)\n Problem:\n The tagger has no key containing " \
          "UNKNOWN as pos-tag. Therefore the first time " \
          "a specific bigram is not found in the tagger " \
          "dictionary, the pos-tag UNKNOWN propagates " \
          "through the sentence."

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    print "4~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "evaluate test set (pre-labels vs. own-labels)\n"
    # 1c) Schreibe eine Funktion evaluate(tagger, tagged_sents),
    # die die Genauigkeit eines Taggers berechnet.
    # Evaluiere deinen Tagger auf deinem Testkorpus.
    # Wie genau ist er?
    # Anwort 1c): ..... (siehe console output)
    # ---------------------------------------------------

    # evaluate accuracy of tagger
    accuracy = evaluate(
        test_set, bigrams_with_most_likely_tag)

    print "Antwort 1c)\n accuracy of tagger: ", accuracy

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    print "5~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "print the confusion matrices\n " \
          " on the brown corpus 10% test sentences\n " \
          " on the 1 test sentence"
    # 1d) Erstelle eine Konfusionsmatrix für deinen Tagger.
    # Bei welchen Tags macht er besonders viele Fehler?
    # Anwort 1d): ..... (siehe console output)
    # ---------------------------------------------------

    confusion_matrix(test_set, test_set_tagged)

    confusion_matrix(test_sentence, test_sentence_tagged)

    print "Antwort 1d)\n Interpretation of the confusion matrix:\n" \
          " The optimal solution has a diagonal matrix." \
          " Not diagonal entries show the number of wrongly" \
          " tagged tokens.\"" \
          " The ratio unknown:known bigrams is about 6:1" \
          " for most english tokens, 9:1 for nouns, and inf:1 " \
          " for foreign tokens with pos-tax X, since none has been" \
          " tagged correctly."

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    print "6~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "bigram-unigram-default-backoff\n"
    # 2) Schreibe zwei weitere Tagger:
    # einen Unigramm-Tagger und einen Default-Tagger.
    # Ändere deinen Tagger so, dass er Wörter in unbekannten
    # Kontexten mit dem Unigramm-Tagger taggt.
    # Der Unigramm-Tagger sollte wiederum bei unbekannten Wörtern
    # auf den Default-Tagger zurückgreifen.
    # ---------------------------------------------------

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    print "7~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "train classifier (tagger) with training set\n"
    # 2a) Trainiere den neuen Tagger auf den
    # gleichen Korpora wie in der letzten Aufgabe.
    # ---------------------------------------------------

    # train unigram tagger
    unigrams_with_all_tags_and_cnt, unigrams_with_most_likely_tag = \
        train_unigram_tagger(training_set)

    # train default tagger
    default_with_most_likely_tag = \
        train_default_tagger(training_set)

    print "tagger_unigram ((token_N),(most likely tag N)):\n " \
          "(only a subset printed)\n",\
            unigrams_with_most_likely_tag.items()[:20]

    print "\ntagger_default ((most likely tag N)):\n", \
            default_with_most_likely_tag

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    print "8~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "pos-tag the test set with the bigram tagger\n"
    # 2) Teste deinen Tagger auf
    # dem Satz “This is a sentence that we want to tag.”
    # ---------------------------------------------------

    # tag the test set with tagger
    test_set_tagged = bigram_tagger_with_backoff(
        test_set_untagged, bigrams_with_most_likely_tag,
        unigrams_with_most_likely_tag, default_with_most_likely_tag)

    print "test set untagged:\n" \
          "(only a subset printed)\n", test_set_untagged[:2]
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "test set tagged with bigram tagger with backoff:\n" \
          "(only a subset printed)\n", test_set_tagged[:2]
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "test set tagged with brown.tagged_sents:\n" \
          "(only a subset printed)\n", test_set[:2]

    # tag the sentence "This is a sentence that we want to tag."
    test_sentence_untagged = [[u'This', u'is', u'a', u'sentence',
                               u'that', u'we', u'want', u'to',
                               u'tag', u'.']]
    test_sentence_tagged = bigram_tagger_with_backoff(
        test_sentence_untagged, bigrams_with_most_likely_tag,
        unigrams_with_most_likely_tag,
        default_with_most_likely_tag)

    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "test sentence untagged:\n" \
          "(only a subset printed)\n",\
            test_sentence_untagged[:2]
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "test sentence tagged with bigram tagger:\n" \
          "(only a subset printed)\n",\
            test_sentence_tagged[:2]
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "Problem from 1b):\n -> Solved.\n" \
          "The backoff functionality, checks the bigrams first,\n" \
          "if unknown, it checks the unigrams,\n" \
          "if unknown, it takes the pre calculated default post tag"

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    print "9~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "evaluate test set (pre-labels vs. own-labels)\n"
    # a) Evaluiere den neuen Tagger auf den
    # gleichen Korpora wie in der letzten Aufgabe.
    # Gibt es einen Unterschied in der Genauigkeit?
    # Anwort 2a): ..... (siehe console output)
    # ---------------------------------------------------

    # evaluate accuracy of tagger
    accuracy = evaluate_with_backoff(
        test_set, bigrams_with_most_likely_tag,
        unigrams_with_most_likely_tag,
        default_with_most_likely_tag)

    print "Antwort 2a) accuracy of tagger: ", accuracy
    print " Without vs. with backoff functionality:\n" \
          " From under 20% to over 90% accuracy."

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    print "10~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "confusion matrix\n"
    # 2a) Erstelle eine Konfusionsmatrix für deinen Tagger.
    # Bei welchen Tags macht er besonders viele Fehler?
    # Anwort 2a): ..... (siehe console output)
    # ---------------------------------------------------

    #print confusion matrix
    confusion_matrix(test_set, test_set_tagged)

    # print confusion matrix
    confusion_matrix(test_sentence, test_sentence_tagged)

    print "Antwort 2a)\n Interpretation of the confusion matrix:\n" \
          " The optimal solution has a diagonal matrix." \
          " Not diagonal entries show the number of wrongly" \
          " tagged tokens.\"" \
          " ADJ, VERB, NUM, make use of the default tagger in " \
          " about 0 to 30 % of cases. X in nearly all of the cases." \
          " ADV-ADJ, ADV-ADP, ADP-PRT show a high error ratio."

 # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    print "11~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "evaluation of bigram tagger with backoff on other " \
          "corpora and categories\n"
    # 2b) Evaluiere deine Tagger auf einer anderen Kategorie des
    # Brown-Korpus.
    #
    # Wie verändert sich ihre Genauigkeit?
    # Wie sieht es aus, wenn du sie über dem conll2000-Korpus evaluierst?"
    # Anwort 2b): ..... (siehe console output)
    # ---------------------------------------------------


    #Brown corpus categories
    print "brown corpus categories\n", brown.categories()

    print "\n1~~~load tagged sents of lore category"
    # load list of sents with tuples of word and tag
    list_of_tagged_sents = brown.tagged_sents(
        categories="lore", tagset="universal")

    # cast ConcatenatedCorpusView object into a list
    list_of_tagged_sents = list(list_of_tagged_sents)

    print "3~~~untag tagged sents"
    # untag the test set
    test_set = list_of_tagged_sents
    test_set_untagged = untag_sents_tagged(test_set)

    print "8~~~load tagged sents"
    # tag the test set with tagger
    test_set_tagged = bigram_tagger_with_backoff(
        test_set_untagged, bigrams_with_most_likely_tag,
        unigrams_with_most_likely_tag,
        default_with_most_likely_tag)

    print "10~~~print confusion matrix"
    # print confusion matrix
    confusion_matrix(test_set, test_set_tagged)

    print "9~~~evaluate accuracy of tagger trained with" \
          " category news and tagged with category lore"
    # evaluate accuracy of tagger
    accuracy = evaluate_with_backoff(
        test_set, bigrams_with_most_likely_tag,
        unigrams_with_most_likely_tag,
        default_with_most_likely_tag)

    print "\nAntwort 2b)\n accuracy of tagger: ", accuracy

    print "The question can be answered hypothetically without" \
        " testing the hypothesis for the conll2000-Korpus:\n" \
        " The accuracy decreases for one simple reason." \
        " Machine learning is about generalization from seen" \
        " examples. Unseen dimensions which exist in new text " \
        " categories or corpora in the form of frequent new" \
        " bigrams/unigrams/default are not part of the trained " \
        " classifier (tagger). The worst that can happen, is that" \
        " the default pos-tag is no longer true for the new texts."

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Function definitions
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def train_bigram_tagger(training_set):
    """
        return a dictionary with:
            key = bigram consisting of  tuple (last tag, this token)
            value = most likely tag
        most likely tag = max ({tag1:cnt1, tag2:cnt2, ...}, cnt_i)
        """
    # Input data structure
    # list of sents containing list of tuples (token, tag)
    # [[(token_0,tag_0), (token_1,tag_1), ...]_sent1,
    #  [(token_0,tag_0), (token_1,tag_1), ...]_sent2, ...]

    # Output data structure 1:
    # {(tag_N-1, token_N):{tag_N_1:cnt_1, tag_N_2:cnt_2, ...},
    #  (tag_N, token_N+1):{tag_N+1_1:cnt_1, tag_N+1_2:cnt_2, ...},
    #  ...}

    # Output data structure 2:
    # {(tag_N-1, token_N):tag_N_most_likely,
    #  (tag_N, token_N+1):tag_N_most_likely,
    #  ...}

    # Intermediate data structure: dict_new_tag_cnt
    # {tag_N-1:cnt, tag_N:cnt, tag_N+1:cnt, ...}

    # output data structure 1
    dict_last_tag_new_token__dict_new_tag__cnt = {}

    # output data structure 2
    dict_last_tag_new_token__most_likey_new_tag = {}

    # nested dictionary
    dict_new_tag__cnt = {}

    if (debug_train): training_set = training_set[:2]
    # iterate through sentences in training set
    for list_sent in training_set:

        # first tag in sentence
        tag_0 = "NONE"

        #iterate through words in sentence
        for i, tuple_token_tag in enumerate(list_sent):

            # extract last tag i-1
            if not i == 0:
                tag_i_minus_1 = list_sent[i - 1][1]
            else:
                tag_i_minus_1 = tag_0

            # extract token i
            token_i = tuple_token_tag[0]

            # extract tag i
            tag_i = tuple_token_tag[1]

            # extract counter
            dict_new_tag__cnt = \
                dict_last_tag_new_token__dict_new_tag__cnt.\
                    get((tag_i_minus_1, token_i),{})

            cnt_i = dict_new_tag__cnt.get(tag_i,0)

            # increment counter
            cnt_i = cnt_i+1

            # update nested dictionary
            dict_new_tag__cnt.update(
                {tag_i:cnt_i})

            # update data structure 1
            dict_last_tag_new_token__dict_new_tag__cnt.update(
                {(tag_i_minus_1, token_i):dict_new_tag__cnt})

            if (debug_train): print "%s: (%s,%s), %s "\
                              %(i, tag_i_minus_1, token_i, tag_i)

    # generate output data structure 2
    for last_tag_new_token, dict_new_tag__cnt \
            in dict_last_tag_new_token__dict_new_tag__cnt.items():

        # extract most likely tag
        most_likey_new_tag = max(
            dict_new_tag__cnt.iteritems(),
            key=operator.itemgetter(1))[0]

        # update data structure 2
        dict_last_tag_new_token__most_likey_new_tag.update(
                {last_tag_new_token:most_likey_new_tag})

    if (debug_train):
        print dict_last_tag_new_token__dict_new_tag__cnt, "\n-----\n", \
            dict_last_tag_new_token__most_likey_new_tag

    # return the data structure
    return dict_last_tag_new_token__dict_new_tag__cnt, \
           dict_last_tag_new_token__most_likey_new_tag


def train_unigram_tagger(training_set):
    """
        unigram tagger
        """
    # Input data structure
    # list of sents containing list of tuples (token, tag)
    # [[(token_0,tag_0), (token_1,tag_1), ...]_sent1,
    #  [(token_0,tag_0), (token_1,tag_1), ...]_sent2, ...]

    # Output data structure 1:
    # {(token_N):{tag_N_1:cnt_1, tag_N_2:cnt_2, ...},
    #  (token_N+1):{tag_N+1_1:cnt_1, tag_N+1_2:cnt_2, ...},
    #  ...}

    # Output data structure 2:
    # {(token_N):tag_N_most_likely,
    #  (token_N+1):tag_N_most_likely,
    #  ...}

    # Intermediate data structure: dict_new_tag__cnt
    #{tag_N_1: cnt_1, tag_N_2: cnt_2, ...}

    # output data structure 1
    dict_new_token__dict_new_tag__cnt = {}

    # output data structure 2
    dict_new_token__most_likey_new_tag = {}

    # nested dictionary
    dict_new_tag__cnt = {}

    if (debug_train): training_set = training_set[:2]
    # iterate through sentences in training set
    for list_sent in training_set:

        #iterate through words in sentence
        for i, tuple_token_tag in enumerate(list_sent):

            # extract token i
            token_i = tuple_token_tag[0]

            # extract tag i
            tag_i = tuple_token_tag[1]

            # extract counter
            dict_new_tag__cnt = \
                dict_new_token__dict_new_tag__cnt.\
                    get((token_i),{})

            cnt_i = dict_new_tag__cnt.get(tag_i,0)

            # increment counter
            cnt_i = cnt_i + 1

            # update nested dictionary
            dict_new_tag__cnt.update(
                {tag_i:cnt_i})

            # update data structure 1
            dict_new_token__dict_new_tag__cnt.update(
                {(token_i):dict_new_tag__cnt})

            if (debug_train): print "%s: (%s,%s) "\
                              %(i, token_i, tag_i)

    # generate output data structure 2
    for new_token, dict_new_tag__cnt \
            in dict_new_token__dict_new_tag__cnt.items():

        # extract most likely tag
        most_likey_new_tag = max(
            dict_new_tag__cnt.iteritems(),
            key=operator.itemgetter(1))[0]

        # update data structure 2
        dict_new_token__most_likey_new_tag.update(
                {new_token:most_likey_new_tag})

    if (debug_train):
        print dict_new_token__dict_new_tag__cnt, "\n-----\n", \
            dict_new_token__most_likey_new_tag, "\n-----\n"

    # return the data structure
    return dict_new_token__dict_new_tag__cnt, \
           dict_new_token__most_likey_new_tag


def train_default_tagger(training_set):
    """
        default tagger
        """
    # Input data structure
    # list of sents containing list of tuples (token, tag)
    # [[(token_0,tag_0), (token_1,tag_1), ...]_sent1,
    #  [(token_0,tag_0), (token_1,tag_1), ...]_sent2, ...]

    # Intermediate data structure: dict_tag_cnt
    # {tag_N-1:cnt, tag_N:cnt, tag_N+1:cnt, ...}

    # intermediate data structure
    dict_tag_cnt = {}

    if (debug_train): training_set = training_set[:2]
    # count true and false tagger tagged tags
    for j, sent_j in enumerate(training_set):

        # iterate through tokens in sentence
        for i, (token_i, tag_i) in enumerate(sent_j):

            # extract and increment counter of tag i
            cnt_i = dict_tag_cnt.get(tag_i, 0)
            cnt_i = cnt_i + 1

            # uptdate dictionary
            dict_tag_cnt.update({tag_i:cnt_i})

    if (debug_train):print dict_tag_cnt
    # determine most frequent tag
    most_likely_tag = max(
        dict_tag_cnt.iteritems(),
        key=operator.itemgetter(1))[0]

    if (debug_train): print most_likely_tag
    #return most frequent tag
    return most_likely_tag


def untag_sents_tagged(test_set):
    """
        returns list of tokens:
        """

    # Input data structure
    # list of sents containing list of tuples (token, tag)
    # [[(token_0,tag_0), (token_1,tag_1), ...]_sent1,
    #  [(token_0,tag_0), (token_1,tag_1), ...]_sent2, ...]

    # Output data structure
    # list of sents containing list of tokens
    # [[token_0, token_1, ...]_sent1,
    #  [token_0, token_1, ...]_sent2, ...]

    # output list
    list_of_untagged_tokens = []

    if (debug_test): test_set = test_set[:2]
    # extract the token from the input data structure
    for j, sent_j in enumerate(test_set):

        # append a new empty list to the output list
        list_of_untagged_tokens.append([])

        # iterate through tokens in sentence
        for token_i, tag_i in sent_j:

            if (debug_test): print "%s: (%s,%s)" \
                              % (j, token_i, tag_i)

            # apppend new token to output list
            list_of_untagged_tokens[j].append(token_i)

    if (debug_test): print list_of_untagged_tokens

    # return list of untagged tokens
    return list_of_untagged_tokens


def bigram_tagger(
        list_of_sents_with_tokens, bigrams_with_most_likey_tag):
    """
        tags the input list of sents containing list of tokens
        with bigram data structure:
        """
    # Input data structure list_of_sents_with_tokens
    # list of sents containing list of tokens
    # [[token_0, token_1, ...]_sent1,
    #  [token_0, token_1, ...]_sent2, ...]

    # Input data structure bigrams_with_most_likey_tag:
    # {(tag_N-1, token_N):tag_N_most_likely,
    #  (tag_N, token_N+1):tag_N_most_likely,
    #  ...}

    # Output data structure
    # [(token_N, tag_N_most_likely),(token_N+1, tag_N+1_most_likely),...],
    # [(token_N, tag_N_most_likely),(token_N+1, tag_N+1_most_likely),...],
    #  ...}

    # output list
    list_tokens_tags=[]

    # first tag in sentence
    tag_0 = "NONE"

    if (debug_test):
        list_of_sents_with_tokens = list_of_sents_with_tokens[:2]
    # extract the token from the input data structure
    for j, sents_j in enumerate(list_of_sents_with_tokens):

        # append a new empty list to the output list
        list_tokens_tags.append([])

        # iterate through tokens in sentence
        for i, token_i in enumerate(sents_j):

            # last tag i-1
            if i == 0:
                tag_i_minus_1 = tag_0
            else:
                tag_i_minus_1 = tag_i

            # build bigram
            bigram_i = (tag_i_minus_1, token_i)

            # extract new tag or
            # return unknown if bigram unknown
            tag_i = bigrams_with_most_likey_tag.get(
                bigram_i, "UNKNOWN")

            # update output data structure
            list_tokens_tags[j].append(
                (token_i, tag_i))

    if (debug_test): print list_tokens_tags

    # return list of tagged tokens
    return list_tokens_tags


def bigram_tagger_with_backoff(list_of_sents_with_tokens,
            bigrams_with_most_likely_tag,
            unigrams_with_most_likely_tag,
            default_with_most_likely_tag):
    """
        tags the input list of sents containing list of tokens
        with a backoff algorithm staring with a bigram data structure:
        """

    # Input data structure: list_of_sents_with_tokens
    # list of sents containing list of tokens
    # [[token_0, token_1, ...]_sent1,
    #  [token_0, token_1, ...]_sent2, ...]

    # Input data structure: bigrams_with_most_likey_tag:
    # {(tag_N-1, token_N):tag_N_most_likely,
    #  (tag_N, token_N+1):tag_N_most_likely,
    #  ...}

    # Input data structure: unigrams_with_most_likey_tag
    # {(token_N):tag_N_most_likely,
    #  (token_N+1):tag_N_most_likely,
    #  ...}

    # Input data structure:default_with_most_likey_tag
    # (tag_most_likely)

    # Output data structure:
    # [(token_N, tag_N_most_likely),(token_N+1, tag_N+1_most_likely),...],
    # [(token_N, tag_N_most_likely),(token_N+1, tag_N+1_most_likely),...],
    #  ...}

    # output list
    list_tokens_tags = []

    # first tag in sentence
    tag_0 = "NONE"

    if (debug_test):
        list_of_sents_with_tokens = list_of_sents_with_tokens[:2]
    # extract the token from the input data structure
    for j, sents_j in enumerate(list_of_sents_with_tokens):

        # append a new empty list to the output list
        list_tokens_tags.append([])

        # iterate through tokens in sentence
        for i, token_i in enumerate(sents_j):

            # last tag i-1
            if i == 0:
                tag_i_minus_1 = tag_0
            else:
                tag_i_minus_1 = tag_i

            # build bigram
            bigram_i = (tag_i_minus_1, token_i)

            # extract new tag or
            # return unknown if bigram unknown
            tag_i = bigrams_with_most_likely_tag.get(
                bigram_i, "UNKNOWN")

            # backoff to unigram
            # extract new tag or
            # return unknown if unigram unknown
            if tag_i == "UNKNOWN":
                tag_i = unigrams_with_most_likely_tag.get(
                    token_i, "UNKNOWN")

            # backoff to default
            if tag_i == "UNKNOWN":
                tag_i = default_with_most_likely_tag

            # update output data structure
            list_tokens_tags[j].append(
                (token_i, tag_i))

    if (debug_test): print list_tokens_tags

    # return list of tagged tokens
    return list_tokens_tags


def evaluate(pretagged_sents, bigrams_with_most_likey_tag):
    """
        evaluates the tagger
        returns proportion of true tagger tagged tags
        """
    # Input data structure: pretagged_sents
    # list of sents containing list of tuples (token, tag)
    # [[(token_0,tag_0), (token_1,tag_1), ...]_sent1,
    #  [(token_0,tag_0), (token_1,tag_1), ...]_sent2, ...]

    # Input data structure: bigrams_with_most_likey_tag
    # {(tag_N-1, token_N):tag_N_most_likely,
    #  (tag_N, token_N+1):tag_N_most_likely,
    #  ...}

    # Intermediate data structure: sents_tagger_tagged
    # [[(token_N, tag_N_most_likely),(token_N+1, tag_N+1_most_likely),...],
    #  [(token_N, tag_N_most_likely),(token_N+1, tag_N+1_most_likely),...],
    #  ...]

    # untag the test set
    sents_untagged = untag_sents_tagged(pretagged_sents)

    # tag the test set with tagger
    sents_tagger_tagged = bigram_tagger(
        sents_untagged, bigrams_with_most_likey_tag)

    # counters
    cnt_true_tags = 0
    cnt_false_tags = 0
    cnt_tokens = 0

    if (debug_eval):pretagged_sents = pretagged_sents[:2]
    # count true and false tagger tagged tags
    for j, sent_j in enumerate(pretagged_sents):

        # iterate through tokens in sentence
        for i, (token_i, pretagged_tag_i) in enumerate(sent_j):

            # increment token counter
            cnt_tokens = cnt_tokens + 1

            #extract tagger_tagged_tag_i of tagger tagged tags
            tagger_token_i = sents_tagger_tagged[j][i][0]
            tagger_tagged_tag_i = sents_tagger_tagged[j][i][1]

            # compare tags and increment tags counter
            if pretagged_tag_i == tagger_tagged_tag_i:
                cnt_true_tags = cnt_true_tags + 1
            else:
                cnt_false_tags = cnt_false_tags + 1

            if (debug_eval):
                print "%s: (%s,%s), (%s,%s)" % (j,
                    token_i, pretagged_tag_i,
                    tagger_token_i, tagger_tagged_tag_i)

    # calculate accuracy
    proportion_of_correctly_tagged_tags = (
        cnt_true_tags/cnt_tokens)

    # return accuracy
    return proportion_of_correctly_tagged_tags

def evaluate_with_backoff(pretagged_sents,
                          bigrams_with_most_likey_tag,
                          unigram_with_most_likey_tag,
                          default_with_most_likey_tag):
    """
        evaluates the tagger
        returns proportion of true tagger tagged tags
        """
    # Input data structure: pretagged_sents
    # list of sents containing list of tuples (token, tag)
    # [[(token_0,tag_0), (token_1,tag_1), ...]_sent1,
    #  [(token_0,tag_0), (token_1,tag_1), ...]_sent2, ...]

    # Input data structure: bigrams_with_most_likey_tag:
    # {(tag_N-1, token_N):tag_N_most_likely,
    #  (tag_N, token_N+1):tag_N_most_likely,
    #  ...}

    # Input data structure: unigrams_with_most_likey_tag
    # {(token_N):tag_N_most_likely,
    #  (token_N+1):tag_N_most_likely,
    #  ...}

    # Input data structure:default_with_most_likey_tag
    # (tag_most_likely)

    # Intermediate data structure: sents_tagger_tagged
    # [[(token_N, tag_N_most_likely),(token_N+1, tag_N+1_most_likely),...],
    #  [(token_N, tag_N_most_likely),(token_N+1, tag_N+1_most_likely),...],
    #  ...]

    # untag the test set
    sents_untagged = untag_sents_tagged(pretagged_sents)

    # tag the test set with tagger
    sents_tagger_tagged = bigram_tagger_with_backoff(
        sents_untagged, bigrams_with_most_likey_tag,
        unigram_with_most_likey_tag, default_with_most_likey_tag)

    # counters
    cnt_true_tags = 0
    cnt_false_tags = 0
    cnt_tokens = 0

    if (debug_eval):pretagged_sents = pretagged_sents[:2]
    # count true and false tagger tagged tags
    for j, sent_j in enumerate(pretagged_sents):

        # iterate through tokens in sentence
        for i, (token_i, pretagged_tag_i) in enumerate(sent_j):

            # increment token counter
            cnt_tokens = cnt_tokens + 1

            #extract tagger_tagged_tag_i of tagger tagged tags
            tagger_token_i = sents_tagger_tagged[j][i][0]
            tagger_tagged_tag_i = sents_tagger_tagged[j][i][1]

            # compare tags and increment tags counter
            if pretagged_tag_i == tagger_tagged_tag_i:
                cnt_true_tags = cnt_true_tags + 1
            else:
                cnt_false_tags = cnt_false_tags + 1

            if (debug_eval):
                print "%s: (%s,%s), (%s,%s)" % (j,
                    token_i, pretagged_tag_i,
                    tagger_token_i, tagger_tagged_tag_i)

    # calculate accuracy
    proportion_of_correctly_tagged_tags = (
        cnt_true_tags/cnt_tokens)

    # return accuracy
    return proportion_of_correctly_tagged_tags

def confusion_matrix(pretagged_sents, sents_tagger_tagged):
    """
        prints confusion matrix out to console
        all numbers in the matrix sum up to number of tokens in text
        optimal result: only diagonal filled with numbers
        """
    # Input data structure: pretagged_sents AND tagger_tagged_sents
    # list of sents containing list of tuples (token, tag)
    # [[(token_0,tag_0), (token_1,tag_1), ...]_sent1,
    #  [(token_0,tag_0), (token_1,tag_1), ...]_sent2, ...]

    # Output data structure: confusion_matrix
    # {(pretagged_tag, tagger_tagged_tag):cnt,
    #  (pretagged_tag, tagger_tagged_tag):cnt,
    #  ... }

    # counters
    confusion_matrix = {}
    cnt_tokens = 0

    if (debug_eval): pretagged_sents = pretagged_sents[:2]
    # count true and false tagger tagged tags
    for j, sent_j in enumerate(pretagged_sents):

        # iterate through tokens in sentence
        for i, (token_i, pretagged_tag_i) in enumerate(sent_j):

            # extract tagger_tagged_tag_i of tagger tagged tags
            tagger_token_i = sents_tagger_tagged[j][i][0]
            tagger_tagged_tag_i = sents_tagger_tagged[j][i][1]

            # increment token counter
            cnt_tokens = cnt_tokens + 1

            # extract and increment counter of tag i
            cnt_i = confusion_matrix.get(
                (pretagged_tag_i, tagger_tagged_tag_i), 0)
            cnt_i = cnt_i + 1

            # compare tags and increment tags counter
            confusion_matrix.update(
                {(pretagged_tag_i, tagger_tagged_tag_i):cnt_i})

            if (debug_eval):
                print "%s: (%s,%s), (%s,%s), (%s)" % (j,
                        token_i, pretagged_tag_i,
                        tagger_token_i, tagger_tagged_tag_i,
                        cnt_i)

    # cast confusion matrix into a list of tuples
    # [(('a', 'a'), 1), (('a', 'b'), 1), ...]
    confusion_matrix_sorted = sorted(
        confusion_matrix.iteritems(), key=operator.itemgetter(0))

    # extract axes
    set_down=set()
    set_right=set()
    for (down, right), c in confusion_matrix_sorted:
        set_down.add(down)
        set_right.add(right)

    # sort axes
    list_down = sorted(set_down)
    delta = list(set_right - set_down)
    list_right = list_down + delta

    #print title
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "confusion matrix"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

    # iterate through right axis
    print "%-6s" % (""),
    for right in list_right:

        #print column names
        print "%-6s" % (right[0:5]),
    print

    # iterate through down axis
    for down in list_down:

        #print line names
        print "\n"
        print "%-6s" % (down[0:5]),

        # iterate through right axis
        for right in list_right:

            #print counter
            cnt = confusion_matrix.get((down,right),0)
            print "%-6s" %(cnt),

    print "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"

    #return confusion matrix
    return confusion_matrix


if __name__ == "__main__":
	main()