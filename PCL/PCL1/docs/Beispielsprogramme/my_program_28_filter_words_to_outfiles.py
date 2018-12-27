#!/usr/bin/python

## program to write specific words to two output files.
## by Martin Volk

import sys  ## necessary for command line arguments

## get the filename
#filename = sys.argv[1]
filename="/media/benzro/OS/Users/benzro/Documents/LubuntuShared/\
8) PCL-1/Beispielsprogramme/SecondVariety.txt"
	
## open a file for reading
infile = open(filename, 'r')	
## create a name for the first output file
outfilename_1 = filename + '.a_words.txt'
## open the first file for writing
outfile_a = open(outfilename_1, 'w')
## create a name for the second output file
outfilename_2 = filename + '.b_words.txt'
## open the second file for writing
outfile_b = open(outfilename_2, 'w')
## for each line in the input file
cnt=0
for line in infile:
	cnt+=1
	# split the line into a list of strings
	line_list = line.split()
	# for each word in the line
	for word in line_list:		
		# remove a comma at the end of the word
		if word[-1] == ',' or word[-1] == '.':
			word = word[0:-1]
		# check if the word starts with 'a'
		if word[0] == 'a' and len(word)>10:	
			print cnt, word
			# write output to the first file
			outfile_a.write(word)
			outfile_a.write('\n')
		# check if the word starts with 'b'
		elif word[0] == 'b' and len(word)>10:
			print cnt, word
			# write output to the second file
			outfile_b.write(word)
			outfile_b.write('\n')				
## close the files
infile.close()
outfile_a.close()
outfile_b.close()
	
