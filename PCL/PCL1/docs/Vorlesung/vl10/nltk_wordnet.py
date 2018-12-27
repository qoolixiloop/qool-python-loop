#!/usr/bin/env python
# -*- coding: utf-8 -*-

# simon.clematide@uzh.ch
# PCL I

import nltk

# Mit "as" kann man Kurznamen einführen.
from nltk.corpus import wordnet as wn


# <h2>Synsets (unterschiedliche Bedeutungen) eines
# Lemmas berechnen</h2>
# Welche Bedeutungen hat das Wort "car"?
print "\nfrom 1: ", wn.synsets('car')
print "\nfrom 2", wn.synsets('motorcar')

# Definition einer Bedeutung
print "\nfrom 3: ", wn.synset('car.n.01').definition()

# <h2>Alle synonymen Lemmas eines Synsets berechnen</h2>
print "\nfrom 4: ", wn.synset('car.n.01').lemma_names()
print "\nfrom 5: ", wn.synset('car.n.01').lemmas()

# Was ist eine Lemma-Datenstruktur?
print "\nfrom 6: ", type(wn.synset('car.n.01').lemmas()[0])
print "\nfrom 7: "
help(nltk.corpus.reader.wordnet.Lemma)

# Alle hyponymen Bedeutungen eines Lemmas berechnen
print "\nfrom 8: ", wn.synset('car.n.01').hyponyms()


