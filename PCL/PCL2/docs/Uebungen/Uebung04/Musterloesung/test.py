#!/usr/bin/env python
# -*- coding:utf-8 -*-

import aufgabe1 as a1
import aufgabe2 as a2
import nltk
from nltk.corpus import brown
from nltk.corpus import conll2000
from nltk.tag import mapping


def test_tagging(tagger):
   
    test_bg = tagger.tag_sentence([u'this', u'is', u'a', u'sentence', 
        u'that', u'we', u'want', u'to', u'tag', u'.'])

    print u' '.join((u'{}/{}'.format(word, tag) for word, tag in test_bg))
    print u'\n'


def print_accuracy(tagger, test):

    score = a1.evaluate(tagger, test)
    print u'Tagger accuracy: {}'.format(score)
    print u'\n'


def print_confusion_matrix(tagger, test, tagset):

    cmatr = a1.generate_confusion_matrix(tagger, test, tagset)
    print u'Tagger Confusion Matrix (Rows: Target, Columns: Actual)'
    print cmatr
    print u'\n'


def main():

    # 1. a)
    bts = brown.tagged_sents(categories=u'news', tagset=u'universal')
    brown_size = int(len(bts) * 0.9)
    brown_training = bts[:brown_size]
    brown_test = bts[brown_size:]
    tagset = list(mapping._UNIVERSAL_TAGS)

    simple_tagger = a1.BigramTagger()
    simple_tagger.train(brown_training)

    #1. b)
    test_tagging(simple_tagger)

    #1. c)
    print u'Simple bigram tagger'
    print_accuracy(simple_tagger, brown_test)

    #1. d)
    print_confusion_matrix(simple_tagger, brown_test, tagset)

    #2. a)
    default_tagger = a2.DefaultTagger(u'NN')

    unigram_tagger = a2.UnigramTagger(backoff_tagger=default_tagger)
    unigram_tagger.train(brown_training)

    bigram_tagger = a2.BigramTagger(backoff_tagger=unigram_tagger)
    bigram_tagger.train(brown_training)

    print u'Bigram tagger with backoffs'
    print_accuracy(bigram_tagger, brown_test)

    #2. b)
    other_cat = brown.tagged_sents(categories='romance', tagset='universal')
    print u'Simple bigram tagger, other genre'
    print_accuracy(simple_tagger, other_cat)
    print u'Backoff tagger, other genre'
    print_accuracy(bigram_tagger, other_cat)

    conll_sents = conll2000.tagged_sents(tagset=u'universal')

    print u'Simple bigram tagger, other corpus'
    print_accuracy(simple_tagger, conll_sents)
    print u'Backoff tagger, other corpus'
    print_accuracy(bigram_tagger, conll_sents)


if __name__ == '__main__':
    main()
