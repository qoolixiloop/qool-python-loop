# Python program to split compound nouns
# by Martin Volk

# initialize the list variables with lists of words
lexicon = ['computer', 'linguistik', 'fleisch', 'fleischer', \
			'erzeugnis', 'zeugnis']

testwords = ['computerlinguistik', 'computerexperte', \
			'fleischerzeugnis']

# for each word in the list  testwords
for word in testwords:
	# split the word in all possible ways
	# the first element is at least 3 characters long
	for position in range(3, len(word)):
		## assign the split parts to two variables
		part1 = word[0:position]
		part2 = word[position:]
		## print the current split for inspection
		print part1, part2
		
		## solution with two nested if conditions
#		if part1 in lexicon:
#			if part2 in lexicon:
#				print 'Found compound ', part1, part2, ':-)'

		## solution with a complex condition connected with 'and'
		if (part1 in lexicon) and (part2 in lexicon):
				print 'Found compound ', part1, part2, ':-)'
