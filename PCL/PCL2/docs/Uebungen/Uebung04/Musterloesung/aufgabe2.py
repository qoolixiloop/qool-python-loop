#!/usr/bin/env python
# -*- coding: utf-8 -*-

import aufgabe1
import collections
import operator
import StringIO
import sys

from aufgabe1 import IntDict
from collections import defaultdict
from operator import itemgetter

class DefaultTagger(object):

    def __init__(self, dtag):
        self._tag = dtag

    def tag(self, word):
        return (word, self._tag)


class UnigramTagger(object):

    def __init__(self, backoff_tagger=None):
        self.freqs = defaultdict(IntDict)
        self.backoff = backoff_tagger

    def train(self, training_data):
        for sent in training_data:
            for word,tag in sent:
                self.freqs[word][tag] += 1

    def tag(self, word):
        try:
            best_tag = max(self.freqs[word].items(), key=itemgetter(1))[0]
            return (word, best_tag)
        except Exception:
            if self.backoff is not None:
                return self.backoff.tag(word)
            else:
                return (word, None)

    def tag_sentence(self, sentence):
        return list(map(self.tag, sentence))


class BigramTagger(object):

    def __init__(self, backoff_tagger=None):
        self.freqs = defaultdict(IntDict)
        self.backoff = backoff_tagger

    def train(self, training_data):
        for sent in training_data:
            last_tag = None
            for token, tag in sent:
                context = (last_tag, token)
                self.freqs[context][tag] += 1
                last_tag = tag

    def tag(self, word, last_tag):
        context = (last_tag, word)
        try:
            best_tag = max(self.freqs[context].items(), key=itemgetter(1))[0]
            return (word, best_tag)
        except Exception:
            if self.backoff is not None:
                return self.backoff.tag(word)
            else:
                return (word, None)

    def tag_sentence(self, sent):
        tagged = []
        last_tag = None
        for word in sent:
            tagged_word = self.tag(word, last_tag)
            tagged.append(tagged_word)
            last_tag = tagged_word[1]
        return tagged
