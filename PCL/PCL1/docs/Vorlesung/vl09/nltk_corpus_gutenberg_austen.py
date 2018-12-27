#!/usr/bin/env python
# -*- coding: utf-8 -*-

# simon.clematide@uzh.ch
# PCL I

from nltk.corpus import gutenberg

# oder absoluter Pfad einer Textdatei
filename = 'austen-emma.txt'

# Korpus als eine lange Zeichenkette
emma_chars = gutenberg.raw(filename)
print 60*'*', '\nKorpus als eine lange Zeichenkette:'
print emma_chars[-324:] #die letzten 324 Zeichen

# Korpus als Liste von Wörtern
# (Wort ist Zeichenkette)
emma_words = gutenberg.words(filename)
print 60*'*', '\nKorpus als Liste von Woertern:'
print emma_words[-30:] #die letzten 30 Wörter

# Korpus als Liste von Sätzen
# (Satz ist Liste von Wörten)
emma_sents = gutenberg.sents(filename)
print 60*'*', '\nKorpus als Liste von Saetzen:'
print emma_sents[-5:] #die letzten 5 Sätze

# Korpus als Liste von Paragraphen
# (Paragraph ist Liste von Sätzen)
emma_paras = gutenberg.paras(filename)
print 60*'*', '\nKorpus als Liste von Paragraphen:'
print emma_paras[-2:] #die letzten 2 Paragraphen

# Wieviele Paragraphen?
number_of_paras=len(gutenberg.paras(filename))
print "\n number of paras: ",number_of_paras,"\n"

# Wieviele Sätze?
number_of_sents=len(gutenberg.sents(filename))
print "\n number of sents: ",number_of_sents,"\n"

# Wieviele Sätze pro Paragraph im Schnitt?
emma_paras_sents_mean=number_of_sents/number_of_paras
print "\n number sents per para: ",emma_paras_sents_mean,"\n"

# Wieviele Wörter pro Satz im Schnitt?
number_of_words=len(gutenberg.words(filename))
emma_sents_words_mean=number_of_words/number_of_sents
print "\n number of words per sent: ",emma_sents_words_mean,"\n"

# Wie kann man die durchschnittliche Wortlänge berechnen?
number_of_chars=len(gutenberg.raw(filename))
emma_words_chars_mean=number_of_chars/number_of_words
print "\n number of chars per word: ",emma_words_chars_mean,"\n"

# Wo liegen die Dateien dieses Korpus?
print "\n gutenberg.root directory: ", gutenberg.root,"\n"
