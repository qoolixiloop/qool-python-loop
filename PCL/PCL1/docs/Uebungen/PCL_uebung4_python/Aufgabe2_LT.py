#!/usr/bin/env python
# -*- coding: utf-8 -*-
#PCL I, Übung 4, HS15
#Aufgabe 2
#Autor: 'Lennart von Thiessen'
#Matrikel-Nr.: '11-185-790'

import sys
import re

filename = sys.argv[1]
infile = open(filename,'r')
i_lines = 0

print '## START ######################################################'

for word in infile:
	i_lines += 1
	word = word.rstrip('\n')
	tmp_list = re.findall('(ing$|s$|ed$)', word)
	if(len(tmp_list) != 0):
		sol = word + ' -> ' + word[:-len(tmp_list[0])] + ' ' + tmp_list[0]
		print sol
	else:
		sol = word + ' -> ' + word
		print sol
print i_lines, ' Verben wurden überprüft'

print '## END ########################################################'



# WAS GEMEINT MIT WIE FILTER FUNKTIONIERT



