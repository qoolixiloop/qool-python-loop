#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#used corpora as data input
from nltk.corpus import brown

#used functionality for ML
import operator
import random
import nltk

#feature extractor functions
def punct_features(tokens, i):
    """
        i is the position of each period '.' in the list of tokens
        we need to specify the features of the data that will be used in order
        to decide whether punctuation indicates a sentence boundary
        """
    return {'next-word-capitalized': tokens[i+1][0].isupper(),
            'prevword': tokens[i-1].lower(),
            'punct': tokens[i],
            'prev-word-is-one-char': len(tokens[i-1]) == 1}

def segment_sentences(words):
    """
        Classification-based sentence segmenter.
        """
    start = 0
    sents = []
    for i, word in words:
        print i, word
        if word in '.?!' and classifier.classify(words, i) == True:
            sents.append(words[start:i+1])
            start = i+1
    if start < len(words):
        sents.append(words[start:])
    print "from segment sentences", sents

def dialogue_act_features(post):
    features = {}
    for word in nltk.word_tokenize(post):
        features['contains({})'.format(word.lower())] = True
    return features

def rte_features(rtepair):
    extractor = nltk.RTEFeatureExtractor(rtepair)
    features = {}
    features['word_overlap'] = len(extractor.overlap('word'))
    features['word_hyp_extra'] = len(extractor.hyp_extra('word'))
    features['ne_overlap'] = len(extractor.overlap('ne'))
    features['ne_hyp_extra'] = len(extractor.hyp_extra('ne'))
    return features

def tag_list(tagged_sents):
    return [tag for sent in tagged_sents for (word, tag) in sent]

def apply_tagger(tagger, corpus):
    return [tagger.tag(nltk.tag.untag(sent)) for sent in corpus]

# Main
if __name__ == "__main__":
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "E X A M P L E 1: Sentence Segmentation"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "Sentence Segmentation. " \
          "Sentence segmentation can be viewed as a classification " \
          "task for punctuation: whenever we encounter a symbol that " \
          "could possibly end a sentence, such as a period or a " \
          "question mark, we have to decide whether it terminates " \
          "the preceding sentence." \
          "The first step is to obtain some data that has already " \
          "been segmented into sentences and convert it into a form " \
          "that is suitable for extracting features:"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    sents = nltk.corpus.treebank_raw.sents()[:500]
    print "length of treebank_raw.sents() : ", len(sents)
    tokens = []
    boundaries = set()
    offset = 0
    for sent in sents:
        # concatentation (+): The method extend(seq)
        # appends the contents of seq to list.
        tokens.extend(sent)
        offset += len(sent)
        boundaries.add(offset - 1)
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "Here, tokens is a merged list of tokens from the " \
          "individual sentences, and boundaries is a set " \
          "containing the indexes of all sentence-boundary tokens."
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print tokens[:10]
    print sorted(list(boundaries))[:10]
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "Based on this feature extractor, we can create a list " \
          "of labeled featuresets by selecting all the punctuation " \
          "tokens and tagging whether they are boundary tokens or not" \
          "(end of sentence tokens '.' or '?' or '!')"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "data structure of featureset:" \
          "[({punct_features},True/False)," \
          " ({punct_features},True/False),...]" \
          "- Start bei for Schleife: jeder index i wird durchlaufen" \
          "- für jedes i wird geprüft, ob tokens[i] ein 'i?!' ist" \
          "- falls nicht, wird i erhöht ohne Eintrag in Liste" \
          "- falls ja:" \
          "    -wird die Funktion punct_features(tokens, i)" \
          "     aufgerufen und ein dictionary Eintrag erzeugt" \
          "    -wird geprüft ob i im set boundaries enthalten ist" \
          "     und entsprechend ein boolean Eintrag True/False erzeugt"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    featuresets = [(punct_features(tokens, i), (i in boundaries))
                   for i in range(1, len(tokens) - 1)
                   if tokens[i] in '.?!']
    print featuresets[:10]
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "Using these featuresets, we can train and evaluate a " \
          "punctuation classifier"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    size = int(len(featuresets) * 0.1)
    train_set, test_set = featuresets[size:], featuresets[:size]
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "accuracy"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print nltk.classify.accuracy(classifier, test_set)
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "To use this classifier to perform sentence segmentation, " \
          "we simply check each punctuation mark to see whether it’s " \
          "labeled as a boundary, and divide the list of words at " \
          "the boundary marks"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    new_sents = nltk.corpus.treebank_raw.sents()[501:503]
    print "new sentences: ", new_sents
    new_tokens = []
    for sent in new_sents:
        new_tokens.extend(sent)
    print "new tokens: ", new_tokens
    new_featureset = [(i,new_token)
                   for i, new_token in enumerate(new_tokens)]
    print "new feature: ", new_featureset
    # segment_sentences(new_featureset)
    # print "new classification: ", classifier.classify(new_featureset)
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "E X A M P L E 2: Identifying Dialogue Act Types"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    posts = nltk.corpus.nps_chat.xml_posts()[:100]
    featuresets = [(dialogue_act_features(post.text), post.get('class'))
                   for post in posts]
    print featuresets[:10]
    size = int(len(featuresets) * 0.1)
    train_set, test_set = featuresets[size:], featuresets[:size]
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    print(nltk.classify.accuracy(classifier, test_set))
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "let’s test it out on some names that did not appear in" \
          " its training data"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    new_p=nltk.corpus.nps_chat.xml_posts()[103]
    print "new post: ",new_p.text, "class: " ,new_p.get('class')
    new_f = dialogue_act_features(new_p.text)
    print "new feature: ",new_f
    print "new classification: ",classifier.classify(new_f)

    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "E X A M P L E: Confusion Matrix"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    brown_tagged_sents = brown.tagged_sents(categories='news')
    size = int(len(brown_tagged_sents) * 0.9)
    train_sents = brown_tagged_sents[:size]
    t2 = nltk.BigramTagger(train_sents)
    gold = tag_list(brown.tagged_sents(categories='editorial'))
    test = tag_list(apply_tagger(t2, brown.tagged_sents(categories='editorial')))
    cm = nltk.ConfusionMatrix(gold, test)
    print(
    cm.pretty_format(sort_by_count=True, show_percents=True, truncate=9))
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print ""
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print ""
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"








