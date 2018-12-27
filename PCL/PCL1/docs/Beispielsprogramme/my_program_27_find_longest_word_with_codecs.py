#!/usr/bin/python
# *-* coding: UTF-8 *-*

# program to demonstrate opening a file for reading
# and searching the longest word in this file
# by Martin Volk

import sys  ## necessary for command line arguments
import codecs
## define a variable for the length of the longest word  
max_len = 0
## ... and for the word itself
max_word = ''
## get the filename (to be searched) from the command line
#filename = sys.argv[1]
filename="/media/benzro/OS/Users/benzro/Documents/LubuntuShared/\
8) PCL-1/Beispielsprogramme/person_name_and_gender.txt"	
## open the file for 'reading'
infile = codecs.open(filename, 'r', 'utf-8')	
## for each line in this file do
for line in infile:
	my_line_list = line.split(' ')
	print "Space delimiter", my_line_list
	my_line_list = line.split()
	print "Default delimiter set", my_line_list
	for word in my_line_list:
		## if the current word is longer than max_len
		if len(word) > max_len:
			## set max_len to the length of the current word
			max_len = len(word)
			## store the current word in max_word
			max_word = word
			print max_len, max_word			
## close the file
infile.close()		
## print the length of the longest word and the word itself
print max_len, max_word
	
