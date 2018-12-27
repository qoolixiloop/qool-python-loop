#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PCL-I: Uebung 03 - Aufgabe 1, FS16

# Autoren:
# c(Student, Martikelnummer) -> 	{'Roland Benz'			: '97-923-163',
#									 'Linus Manser' 		: '13-791-132'}
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Aufruf des Programms:
# Version 1: python ex01.py
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

'''
1 Ein Korpus erstellen

Abzugeben ist ein Skript, welches ein oder mehrere Korpora erstellt und sich in den folgenden
Aufgaben einfach als Modul aufrufen lässt.
'''

# generate corpora with nltk PlaintextCorpusReader
#=================================================
import codecs
import os
from nltk.corpus.reader.plaintext import PlaintextCorpusReader as PCR

def new_corpus():
    # path of downloaded text files enron1
    corpusdir_ham ="/media/benzro/OS/Users/benzro/Desktop/Studium Uni/2)" \
               "ZweitesSemester/27)PCL-2/Uebungen/Uebung03/Enron/enron1/ham/"
    corpusdir_spam ="/media/benzro/OS/Users/benzro/Desktop/Studium Uni/2)" \
                "ZweitesSemester/27)PCL-2/Uebungen/Uebung03/Enron/enron1/ham/"

    # generate corpora
    newcorpus_ham = PCR(corpusdir_ham, '.*')
    newcorpus_spam = PCR(corpusdir_spam, '.*')


# try out some functionalities of nltk on new corpora
#====================================================

def try_out_some_functionalities():

    corpusdir ="/media/benzro/OS/Users/benzro/Desktop/Studium Uni/2)" \
           "ZweitesSemester/27)PCL-2/Uebungen/Uebung03/Enron/test/"
    newcorpus = PCR(corpusdir, '.*')

    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "access one file in the corpus"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    infile = corpusdir + "0001.1999-12-10.farmer.ham.txt"
    infile = "0004.1999-12-14.farmer.ham.txt"
    fin = newcorpus.open(infile)
    print fin.read().strip()
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "all file ids"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print newcorpus.fileids()
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "access each file in the corpus"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    # (reduced output: [0:2])
    for infile in sorted(newcorpus.fileids()):
        # the fileids of each file
        print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        print infile
        # opens the file
        fin = newcorpus.open(infile)
        # prints the content of the file
        print fin.read().strip()
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "access the plaintext; outputs pure string of all files"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print newcorpus.raw().strip()
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "Access paragraphs in the corpus. (list of list of list of strings)"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    # NOTE: NLTK automatically calls nltk.tokenize.sent_tokenize and
    #       nltk.tokenize.word_tokenize.
    #
    # Each element in the outermost list is a paragraph, and
    # Each paragraph contains sentence(s), and
    # Each sentence contains token(s)
    print newcorpus.paras()
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "To access pargraphs of a specific fileid."
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print newcorpus.paras(newcorpus.fileids()[0])
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "Access sentences in the corpus. (list of list of strings)"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    # NOTE: That the texts are flattened into sentences that contains tokens.
    print newcorpus.sents()
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "To access sentences of a specific fileid."
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print newcorpus.sents(newcorpus.fileids()[0])
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "Access just tokens/words in the corpus. (list of strings)"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print newcorpus.words()
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "To access tokens of a specific fileid."
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print newcorpus.words(newcorpus.fileids()[0])
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

if __name__ == "__main__":
    new_corpus()
    try_out_some_functionalities()


