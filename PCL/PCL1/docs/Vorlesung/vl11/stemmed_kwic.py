#!/usr/bin/env python
# -*- coding: utf-8 -*-

# simon.clematide@uzh.ch
# PCL I
# Example from NLTK book p. 107-108

import nltk, re

class RegexStemmer(object):
    #ObjektInitialisierung
    def __init__(self, r=
            r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)?$'):
        #Eigener Regex zur Wortstammbildung
        self._r = r
        print "\nfrom 0.0: ", type(self._r), self._r
    #Hier wird der WortStamm bestimmt
    def stem(self,word):
        m = re.match(self._r, word)
        #Stamm ^(.*?)
        try:
            return m.group(1)
        except:
            return "" #falls keine Gruppe 1 besteht

class IndexedText(object):
    #ObjektInitialisierung
    def __init__(self, stemmer, text):
        #Text ist Wortliste
        self._text = text
        print "\nfrom 0.1: ", type(self._text),self._text[:10]
        #Stemmer zur Stammbildung
        self._stemmer = stemmer
        print "\nfrom 0.2: ", type(self._stemmer),self._stemmer
        #Textindex mit WortStamm, dict, {WortStamm, AlleIndices}
        self._index = nltk.Index((self._stem(word), i)
                                 for (i, word) in enumerate(text))
        print "\nfrom 0.3: ", type(self._index)
        print "\nfrom 0.3: is dict? ",issubclass(nltk.Index, dict)
    #Stamm in Kleinbuchstaben
    def _stem(self, word):
        return self._stemmer.stem(word).lower()
    #Konkordanzprint
    def concordance(self, word, width=40):
        #Aufruf der Methode stem
        key = self._stem(word)      # stemmed keyword
        #width: chars vor und nach word
        wc = width/4                # words of context
        #Iteriere über AlleIndices des key=Wortstamm
        for i in self._index[key]:
            #linker Kontext ohne word
            lcontext = ' '.join(self._text[i-wc:i])
            #word (index i) und rechter Kontext
            rcontext = ' '.join(self._text[i:i+wc])
            ldisplay = '%*s'  % (width, lcontext[-width:])
            rdisplay = '%-*s' % (width, rcontext[:width])
            print ldisplay, rdisplay

#Text laden
text = nltk.corpus.webtext.words('grail.txt')

#Neues nltk stemmer objekt
#=========================
print "\nfrom 1.1:"
porter_stemmer = nltk.PorterStemmer()

#Neues Text Objekt, mit nltk Stemmer und Index
print "\nfrom 1.2:"
porter_index = IndexedText(porter_stemmer, text)

#Konkordanz von gestemmtem Wort seem
print "\nfrom 1.3: ","\nKWIC mit Porter-Stemmer\n"
porter_index.concordance('seem')
print "\n",40*"=" ,"\n"

#Neues Stemmer Objekt mit eigener Regex
#======================================
print "\nfrom 2.1:"
regex_stemmer = RegexStemmer()

#Test: Stemmer anwenden auf seeming
print "\nfrom 2.test: ", regex_stemmer.stem('seeming')

#Neues Text Objekt mit eigenem Stemmer und Index
print "\nfrom 2.2:"
regex_index = IndexedText(regex_stemmer, text)

#Konkordanz von gestemmten Wort seem
print "\nfrom 2.3: ","\nKWIC mit simplem Regex-Stemmer\n"
regex_index.concordance('seem')
print "\n",40*"=" ,"\n"

## Wie gut ist unser simpler Stemmer?
#====================================
print "\nfrom 3.0:"
porter_index.concordance('dies')
print "\nfrom 3.1:"
regex_index.concordance('dies')
print "\n",40*"=" ,"\n"

print "\nfrom 3.test: ",regex_stemmer.stem('dies')
print "\nfrom 3.test: ",regex_stemmer.stem('dying')
print "\nfrom 3.test: ",regex_stemmer.stem('is')
print "\n",40*"=" ,"\n"

## Wie gut ist unser better Stemmer?
#====================================
regex = r'^(.{2,}?)(ing|ly|ed|ious|ies|ive|es|s|ment)?$'
print "\nfrom 3.2: ", regex
better_regex_index = IndexedText(RegexStemmer(r=regex), text)

print "\nfrom 3.3: ","\nKWIC mit better Regex-Stemmer\n"
better_regex_index.concordance('dies')
print "\n",40*"=" ,"\n"



