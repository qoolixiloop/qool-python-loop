#!/usr/bin/env python
# -*- coding: utf-8 -*-

import nltk
text = """At eight o'clock on Thursday morning
Arthur didn't feel very good."""
print "\nRaw Text\n",text
text_ = 'He believes in stemming.'
print "\nRaw Text_\n",text_

#Tokenizer
tokens = nltk.word_tokenize(text)
print "\nTokenizer\n",tokens
itokens=text_.split()
print "\niSimpleSplitTokenizer\n",itokens

#Text
itext=nltk.Text(itokens)
print "\niText\n ", itext #to print the first line
for i in itext:
    print type(i), i
print "  Text Länge und Typ\n ", len(itext), type(itext)

#Tagger
tagged = nltk.pos_tag(tokens)
print "\nTagger\n",tagged
itagged = nltk.pos_tag(itokens)
print "\niTagger\n",itagged

#Chunker
entities = nltk.chunk.ne_chunk(tagged)
print "\nChunker\n",entities
ientities = nltk.chunk.ne_chunk(itagged)
print "\niChunker\n",ientities

#Stemmer
stemmer = nltk.stem.PorterStemmer()
print "\nStemmer"
for tok in nltk.word_tokenize('He believes in stemming.'):
    print tok,"\t", stemmer.stem(tok)
print "\niStemmer"
for tok in itext:
    print tok,"\t", stemmer.stem(tok)

#Lemmatizer
print "\nLemmatizer"
lemmatizer = nltk.stem.WordNetLemmatizer()
for tok in nltk.word_tokenize('He believes in stemming.'):
    print tok,"\t", lemmatizer.lemmatize(tok)
print "\niLemmatizer"
for tok in itext:
    print tok,"\t", lemmatizer.lemmatize(tok)
