#!/usr/bin/python

# program to count _German_ ADJA-NN sequences (= simple NPs) in file with 3-column format
# with a hash
# by Martin Volk

import sys  ## necessary for command line arguments
import re   ## necessary for regular expressions

def main():

	## define a hash
	my_np_hash = {}
	
	## define a counter
	np_counter = 0
	
	## initialize variables
	curr_word = ''
	last_word = ''
	curr_pos_tag = ''
	last_pos_tag = ''
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
		
		# check if the line contains a word
#		match = re.search('^([^\t]+)', line)
		# check if the line contains a lemma
		match = re.search('\t[^\t]+\t([^\n]+)', line)
		
		# if the line contains a word and the current language is German
		if match and (curr_lang == 'de'):
			# store the word
			curr_word = match.group(1)
#			print curr_word

			# check if the line contains a part-of-speech tag
			match = re.search('\t([^\t]+)\t', line)		
			# if the line contains a pos tag
			if match:
				# store the pos tag
				curr_pos_tag = match.group(1)

			if (last_pos_tag == 'ADJA') and (curr_pos_tag == 'NN'):
#				print last_word, curr_word
				np = last_word + ' ' + curr_word
				np_counter += 1
						
				## if np is already in the hash
				if my_np_hash.has_key(np):
					## increment the counter
					my_np_hash[np] += 1
				## if np is not yet in the hash
				else:
					## instantiate the counter
					my_np_hash[np] = 1
		
		## store the current word and current pos tag for the next iteration
		last_word = curr_word
		last_pos_tag = curr_pos_tag			
				
	## close the file
	infile.close()
	
	## print the contents of the hash
	## frequency + np
	for np in my_np_hash.keys():
		print my_np_hash[np], '\t', np
	
	print "Found", np_counter, "NPs"

	
## This is the standard boilerplate to call the function main
if __name__ == '__main__':
	main()