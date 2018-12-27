#!/usr/bin/python

# program to count _German_ PoS tags in a Text+Berg file in 3-column format
# with a hash
# sort the result over the values via a list of tuples
# by Martin Volk

import sys  ## necessary for command line arguments
import re   ## necessary for regular expressions

def main():

	## define a hash
	my_pos_hash = {}
	
	## define a word counter
	word_counter = 0
	
	## initialize variable
	curr_lang = ''

	## get the filename
	filename = sys.argv[1]
	
	## open a file for reading
	infile = open(filename, 'r')
	
	## for each line in the file
	for line in infile:

		# check if the line contains a lang attribute
		match = re.search(' lang="([^"]+)', line)
		# store the current language
		if match:
			curr_lang = match.group(1)
		
		# check if the line contains a part-of-speech tag
		# alternative:
		# (word, pos_tag, lemma) = line.split('\t')
		match = re.search('\t([^\t]+)\t', line)
		
		# if the line contains a pos tag and the current language is German
		if match and (curr_lang == 'de'):
			# store the pos tag
			pos_tag = match.group()
			word_counter += 1
#			print match.group(1)
						
			## if pos is already in the hash
			## alternative:
			if pos_tag in my_pos_hash:
			# if my_pos_hash.has_key(pos_tag):
				## increment the counter
				my_pos_hash[pos_tag] += 1
			## if pos is not yet in the hash
			else:
				## instantiate the counter
				my_pos_hash[pos_tag] = 1				
				
	## close the file
	infile.close()
	
	pos_tuple_list = []
	
	## print the contents of the hash
	## frequency + pos_tag
	for pos_tag, freq in my_pos_hash.items():
		pos_tuple_list.append((freq,pos_tag))
	
	for tuple in sorted(pos_tuple_list):
		freq = tuple[0]
		pos_tag = tuple[1]
		print freq, '\t', pos_tag
	
	print "Found", word_counter, "PoS tags"

	
## This is the standard boilerplate to call the function main
if __name__ == '__main__':
	main()