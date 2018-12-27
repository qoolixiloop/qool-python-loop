#!/usr/bin/env python
# -*- coding: utf-8 -*-

# simon.clematide@uzh.ch
# PCL I

from __future__ import division
import nltk

#Brown words
brown_words=nltk.corpus.brown.words()
print "\nfrom 0.0: ", len(brown_words), type(brown_words)
print brown_words[:20]

#List: Inffizienterer Lookup für die Stoppwörter mit Listen
stopwords_en = nltk.corpus.stopwords.words('english')
print "\nfrom 0.1: ", len(stopwords_en), type(stopwords_en)
print stopwords_en[::20]

# # Was berechnet foo()?
# def foo(text):
#     """ Hier fehlt Dokumentation... """
#     bar = [w for w in text
#            if w.lower() not in stopwords_en]
#     print "\nfrom 1.1: ", len(bar), len(text)
#     return len(bar)/len(text)*100.
#
# print "\nfrom 1.2: ", foo(brown_words)

# Set: Effizienterer Lookup für die Stoppwörter mit Mengen
stopwords_en_set = {w for w in stopwords_en}
print "\nfrom 2: ", len(stopwords_en_set), stopwords_en_set

# # Optimierte Funktion
# def non_stopwords_percentage(text):
#     """ Return the percentage of non-stopwords
#     in a list of English tokens. """
#     non_stopwords = [w for w in text
#                      if w.lower() not in stopwords_en_set]
#     print "\nfrom 3.1: ", len(non_stopwords), len(text)
#     return len(non_stopwords)/len(text)*100.
#
# print "\nfrom 3.2: ", non_stopwords_percentage\
#                             (brown_words)
#
# print "\nfrom 3.3: "
# help(non_stopwords_percentage)

# Wie misst man die Effizienz?
#=============================
import cProfile

#Vorberechnen der Liste mit 1 Mio. Token
brown_words_list = list(nltk.corpus.brown.words())
print "\nfrom 4: ", len(brown_words_list), type(brown_words_list)
print brown_words_list[:20]

# # Ineffizientere Verarbeitung mit Stoppwortlisten
# print "\nfrom 5.1: "
# cProfile.run("foo(brown_words)")
# print "\nfrom 5.2: "
# cProfile.run("foo(brown_words_list)")
#
# # Effizientere Verarbeitung mit Stoppwortmenge
# # (oder Dictionary mit Dummy-Werten)
# print "\nfrom 6.1: "
# cProfile.run("non_stopwords_percentage(brown_words)")
# print "\nfrom 6.2: "
# cProfile.run("non_stopwords_percentage(brown_words_list)")

# Wie kann man die Interpunktionstoken ausfiltern?
#=================================================
import re

def delete_punctuation(s):
    """ Return string with all punctuation symbols
    of iso-latin 1 deleted. """
    p = r'[!"#%&\x27`()*,-./:;?@[\]_{}\xa1\xab\xb7\xbb\xbf]'
    s_ = re.sub(p,'',s)
    #if s != s_:
    #    print s, s_
    return s_

def content_word_percentage(text):
    """ Return the percentage of content words in
    a list of English tokens. """
    content_words = [w for w in text
                     if delete_punctuation(w) != ''
                     and w.lower() not in stopwords_en_set]
    print "\nfrom 7.1: ", len(content_words), len(text)
    return len(content_words)/len(text)*100.

print "\nfrom 7.2: ", \
    content_word_percentage(brown_words_list)

print "\nfrom 8: "
cProfile.run("content_word_percentage(brown_words_list)")