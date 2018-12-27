#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PCL I, Uebung 6, Aufgabe 2, HS15
# Aufgabe 6
# Autoren: 		'Roland Bend' AND 'Lennart von Thiessen'
# OLAT names: 	'rolben' AND 'lvthiessen' 
# Matrikel-Nr.: '97-923-163' AND '11-185-790'
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Aufruf des Programms: python aufgabe2.py filename.tsv
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import codecs
import regex
import sys

nameList = []

filename = sys.argv[1]

with codecs.open(filename,'r',encoding='utf8') as f:
    for line in f:
    	line = line.strip()
    	mod =  regex.sub(ur'\p{Lu}','*',line)

    	counter =  0
    	tmp = ''
    	length = len(line)

    	while(counter < length):
    		char = mod[counter]
    		char_next = mod[counter+1]
    		if((char == '*' or char == '-' or char == ' ') and (char_next == '*' or char_next == '-' or char_next == ' ')):
    			tmp = tmp + line[counter]
    			counter = counter + 1
    		else:
    			nameList.append((tmp.rstrip(' '),line[counter:]))
    			tmp =  ''
    			break


with codecs.open("out.tsv",'w',encoding='utf8') as f:
	for ele in nameList:
		res = ele[1].lower() + '\t' + ele[0].lower() + '\t' + ele[0] + ' ' + ele[1] + '\r\n'
		f.write(res)



# VERGLEICHEN MIT GOLD.tsv
#
# python aufgabe2.py NAME.tsv
# diff --suppress-common-lines -y GOLD.tsv out.tsv | wc
#
# OUTPUT:
#      21     264    2214
#
# 21 Fehler