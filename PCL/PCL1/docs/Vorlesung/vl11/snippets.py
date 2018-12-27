#!/usr/bin/env python
# -*- coding: utf-8 -*-

l1 = [('der',1200),('die',1000)]
l2=[]
for i,e in enumerate(l1):
    print "\nfrom 1: ", i #iterator
    print "\nfrom 2: ",e #element
    #l2[i]=(i,e) #funktioniert nicht, index out of range
    l2.append((i,e))
    print "\nfrom 3: ",l1[i]
    print "\nfrom 4: ",e is l1[i]
print "\nfrom 5: ",enumerate(l1)
print "\nfrom 6: ",l2

help(enumerate)
# class enumerate(object)
#  |  enumerate(iterable[, start]) ->
#         iterator for index, value of iterable|
#  |  enumerate is useful for obtaining an indexed list:
#  |      (0, seq[0]), (1, seq[1]), (2, seq[2]), ...
print "\n",40*"=","\n"

global_list = [('der',1200),('die',1000),('das',900)]
print "from 1: ", global_list
def del_first(l):
    print "from 2: ",
    print 'global_list is parameter l:', global_list is l
    del l[0]
del_first(global_list)
print "from 3: ",global_list
print "\n",40*"=","\n"

l1 = [('der',1200),('die',1000)]
print "from 1: ", l1
l2 = l1
print "from 2: ", l2
# Kopieren via Slicing
l3 = l1[:]
print "from 3: ", l3
# Kopieren via copy modul
import copy
l4 = copy.copy(l1)
print "from 4: ", l4
# Welche Listen werden modifiziert?
l1[0] = ('der',999999999)
print "from 5.1: ", l1
print "from 5.2: ", l2
print "from 5.3: ", l3
print "from 5.4: ", l4
print "\n",40*"=","\n"

