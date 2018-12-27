#!/usr/bin/python

## program to read a list of person names with gender information
## and to find these names in a text file
##
## call: python <this_program> <person_name_file> <text_file>
##
## assumes the person names to be in the format: name\tgender
##
## by Martin Volk

import sys  ## necessary for command line arguments
## define a hash as a global variable
my_person_hash = {}
## define a function that reads the person names from file <person_name_file>
## and stores them in the global hash
def read_and_store_person_names():	
	## get the filename of the person name file
	#filename = sys.argv[1]
	filename="/media/benzro/OS/Users/benzro/Documents/LubuntuShared/"\
			+"8) PCL-1/Beispielsprogramme/person_name_and_gender.txt"	
	## open the person name file for reading
	infile = open(filename, 'r')	
	## for each line in the file
	for line in infile:	
		# strip away the \n symbol
		clean_line = line.rstrip()		
		# split the line into a list of strings
		line_list = clean_line.split('\t')
		name = line_list[0]
		gender = line_list[1]
		# save the name --> gender pair in a hash
		my_person_hash[name] = gender
		# add the genitive form of the name
		# example: Tom --> Toms
		name = name + 's'
		# save the genitive name --> gender pair in the hash
		my_person_hash[name] = gender		
###########################################
def main():
	# initialize the counters
	person_counter = 0
	gender_counter = {}
	# read the person names into a hash
	read_and_store_person_names()			
	## get the filename of the text file
	#filename = sys.argv[2]
	filename="/media/benzro/OS/Users/benzro/Documents/LubuntuShared/"\
			+"8) PCL-1/Beispielsprogramme/SecondVariety.txt"		
	## open the file for reading
	infile = open(filename, 'r')
	## for each line in the file
	cnt=0
	for line in infile:
		cnt+=1
		# split the line into a list of strings
		line_list = line.split()
		# for each word in the line
		for word in line_list:		
			# if the word is in the person name hash
			if word in my_person_hash:
				gender = my_person_hash[word]
				# print a line of success and joy :-)
				print cnt,'Found name ', word, ' gender ', gender
				# count the number of found name occurrences
				person_counter += 1
				# count the gender occurrences; get(key[, default])
				gender_counter[gender] = gender_counter.get(gender, 0) + 1							
	## close the file
	infile.close()	
	print
	print 'I found', person_counter, 'person names. :-)'	
	## print the gender frequencies
	for gender in gender_counter:
		print gender, 'names with freq', gender_counter[gender]
	
## This is the standard boilerplate to call the function main
if __name__ == '__main__':
	main()
