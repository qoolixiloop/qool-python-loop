#!/usr/bin/env python
# -*- coding: utf-8 -*-

# simon.clematide@uzh.ch
# PCL I

#Demo von Mengen- und Dictionarykomprehension
#Alphanumeric is a combination of alphabetic and numeric
# characters, and is used to describe the collection of
# Latin letters and Arabic digits or a text constructed
# from this collection.

#Sets
mc = {x.lower() for x in "Das Alphabet. 12" if x.isalnum()}
print mc #set(['a', 'b', 'e', 'd', 'h', 'l', '1', 'p',
             # 's', '2', 't']) der Punkt fällt weg

ms = set()
for x in "Das Alphabet. 12":
    if x.isalnum():
        ms.add(x.lower())
print ms #set(['a', 'b', 'e', 'd', 'h', 'l', '1', 'p',
            #  's', '2', 't']) Der Punkt fällt weg
#Dictionary
text = "abrakadabra. 12"
dc = {c:text.count(c) for c in set(text)}
print dc #{'a': 5, ' ': 1, 'b': 2, 'd': 1, 'k': 1, '.': 1,
        #  '1': 1, 'r': 2, '2': 1}

# Wie würde man das als For-Schleife implementieren?
ds = dict()
for c in set(text):
    ds.update({c:text.count(c)})
print ds #{'a': 5, ' ': 1, 'b': 2, '1': 1, 'd': 1, '2': 1,
        #  'k': 1, 'r': 2, '.': 1}

#List
lc = [x.lower() for x in "Das Alphabet. 12" if x.isalnum()]
print lc

lc = list(x.lower() for x in "Das Alphabet. 12" if x.isalnum())
print lc

#Sets
mc = {x.lower() for x in "Das Alphabet. 12" if x.isalnum()}
print mc

mc = set(x.lower() for x in "Das Alphabet. 12" if x.isalnum())
print mc

#Dictionary
text = "abrakadabra. 12"
dc = {c:text.count(c) for c in set(text)}
print dc

dc = dict((c,text.count(c)) for c in set(text))
print dc