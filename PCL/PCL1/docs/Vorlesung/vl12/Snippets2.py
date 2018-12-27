#!/usr/bin/env python
# -*- coding: utf-8 -*-

word="01234567"
file=open("/home/benzro/Documents/"
          "UnixCommandTestOrdner/PythonTestOutFile.txt","a")
if len(word)<10:
    istr="1: "+ str(len(word))+" "+ word + "\n"
    file.write(istr)
elif len(word)<20:
    print "2:", len(word),word
elif len(word)>20:
    print "3:",len(word), word

file.close()

import re
file=open("/home/benzro/Documents/"
          "UnixCommandTestOrdner/PythonTestInFile.txt","r")
#Schreibe ein Programm,
# das zählt, welche Wortart wie häufig vorkommt.
dict={}
for line in file:
    print "0", line
    list_line=line.split("\t")
    print "1", list_line
    list_tag=list_line[1]
    #list_tag=list_line[1].rstrip()
    #list_tag=re.sub("\n","",list_line[1])
    print "2",list_tag
    #if list_tag[0]=="C":
    word=list_line[0]
    imatch=re.search("on",word)
    if imatch:
        print "3", imatch
        if list_tag in dict:
            dict.update({list_tag: dict[list_tag] + 1})
        else:
            dict.update({list_tag: 1})
    print dict
    print 30*"-"
file.close()