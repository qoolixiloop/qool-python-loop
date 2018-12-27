#!/usr/bin/env python
# -*- coding: utf-8 -*-

# simon.clematide@uzh.ch
# PCL I

from nltk.corpus import brown

# Korpus als Liste von 2-Tupeln (Wort, POS-Tag)
brown_tagged_words = brown.tagged_words()

# Das balancierte Korpus umfasst Texte aus 15 Kategorien
print "brown.categories ", brown.categories(),"\n"

# Es werden alle 500 Einzeldateien verarbeitet!
cnt=0
for f in brown.fileids()[1:10]:
    cnt+=1
    print cnt, ": ", f
    print brown.abspath(f)

# brown
print 60*'*',\
    '\nKorpus als Liste von Paaren von Woertern und POS-Tags:'
print brown_tagged_words,"\n", \
        len(brown_tagged_words), "\n" #1'161'192 Zeichen
print brown_tagged_words[0:20],"\n"

# Wo liegen die Dateien dieses Korpus?
#Python
print "brown.root path: ", brown.root

#Unix
#$ locate -i --regex nltk\.\+corpora\.+brown
#$ ls -l "/home/benzro/nltk_data/corpora/brown/README"
# -rw-rw-r-- 1 benzro benzro 387 Nov 13 14:46
#$ ls -l "/home/benzro/nltk_data/corpora/brown/CONTENTS"
# -rw-rw-r-- 1 benzro benzro 145896 Nov 13 14:46
#$ less "/home/benzro/nltk_data/corpora/brown/CONTENTS"
#$ less "/home/benzro/nltk_data/corpora/brown/README"

