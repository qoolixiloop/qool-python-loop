#!/usr/bin/python

# program to find compound words in a given text
# - assumes the words from the text itself to be the lexicon
# by Martin Volk

import sys  ## necessary for command line arguments
def main():
	## define a list for the lexicon
	lexicon = []
	## define a type counter
	type_counter = 0
	## get the filename
	#filename = sys.argv[1]
	filename="/media/benzro/OS/Users/benzro/Documents/LubuntuShared/"\
			+"8) PCL-1/Beispielsprogramme/SecondVariety.txt"
	## open the input file for reading
	infile = open(filename, 'r')	
	## for each line in the input file
	for line in infile:
		# split the line into a list of strings
		line_list = line.split()
		# for each word in the line
		for word in line_list:
			# if the word is not in the lexicon, then add it
			if word not in lexicon:
				lexicon.append(word)
				# count the words in the lexicon
				type_counter += 1				
	## close the file
	infile.close()		
	##########################################################
	## define a compound counter
	compound_counter = 0
	## check for each word in the lexicon
	## if it is composed of two other words from the lexicon
	for word in lexicon:
		# split the word in all possible ways
		# the first element must be at least 3 characters long
		# and the last element must be at least 3 characters long
		for position in range(3, len(word)-2):		
			## check if both parts are in the lexicon
			if word[0:position] in lexicon and word[position:] in lexicon:
				print 'Found compound ', word[0:position], word[position:]
				compound_counter += 1
	print
	print 'I collected', type_counter, 'different words for the lexicon.'
	print 'I found', compound_counter, 'compounds ;-)'
		
## This is the standard boilerplate to call the function main
if __name__ == '__main__':
	main()
