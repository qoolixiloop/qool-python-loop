#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections
import operator
import StringIO
import sys

from collections import defaultdict
from operator import itemgetter

class IntDict(dict):

    def __missing__(self, key):
        self[key] = int()
        return self[key]


class BigramTagger(object):

    def __init__(self):
        self.freqs = defaultdict(IntDict)

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
                return (word, None)

    def tag_sentence(self, sent):
        tagged = []
        last_tag = None
        for word in sent:
            tagged_word = self.tag(word, last_tag)
            tagged.append(tagged_word)
            last_tag = tagged_word[1]
        return tagged


def evaluate(tagger, corpus):
    total = 0
    correct = 0
    count = 0
    for sent in corpus:
        words = [t[0] for t in sent]
        tagged_words = tagger.tag_sentence(words)
        count += 1
        for my_tag, gold_tag in zip([t[1] for t in sent], 
                [t[1] for t in tagged_words]):
            total += 1
            if my_tag == gold_tag:
                correct += 1
    return float(correct) / float(total)


def generate_confusion_matrix(tagger, corpus, tagset):
    cmatrix = defaultdict(IntDict)
    cmtable = StringIO.StringIO()
    tag_rows = u''.join([u'{:>8}' for t in tagset])
    for sent in corpus:
        words = [t[0] for t in sent]
        tagged_words = tagger.tag_sentence(words)
        for my_tag, gold_tag in zip([t[1] for t in sent], 
                [t[1] for t in tagged_words]):
            cmatrix[gold_tag][my_tag] += 1
    cmtable.write(u'        ')
    cmtable.write(tag_rows.format(*tagset))
    cmtable.write(u'\n')
    for tag in tagset:
        cmtable.write(u'{:>8}'.format(tag))
        cmtable.write(tag_rows.format(*[cmatrix[tag][tag2] for tag2 in tagset]))
        cmtable.write(u'\n')
    cmt_str = cmtable.getvalue()
    cmtable.close()
    return cmt_str

