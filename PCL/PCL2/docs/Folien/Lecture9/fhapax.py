#!/usr/bin/python

import sys
import re
import codecs
from collections import defaultdict

sys.stdout = codecs.getwriter('UTF-8')(sys.stdout)

def loadData(filename, numOfLines):
	lines = codecs.open(filename, 'r', 'utf8').readlines()

	subset = lines[:numOfLines]

	tokens = re.split('\s+', u"".join(subset).strip())
	
	return tokens

def main():
	tokenList = loadData(sys.argv[1], int(sys.argv[2]))
	
	hapaxCount = 0
	
	frequencies = defaultdict(int)
	
	for token in tokenList:
		frequencies[token] += 1
	for token in frequencies:
		if frequencies[token] == 1:
			hapaxCount += 1
	
	print len(tokenList), hapaxCount

if __name__ == "__main__":
	main()
