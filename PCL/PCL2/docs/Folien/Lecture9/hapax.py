#!/usr/bin/python

import sys
import re
import codecs
from collections import defaultdict
import cProfile

sys.stdout = codecs.getwriter('UTF-8')(sys.stdout)

def loadData(filename, numOfLines):
	lines = codecs.open(filename, 'r', 'utf8').readlines()

	subset = lines[:numOfLines]

	tokens = re.split('\s+', u"".join(subset).strip())
	
	return tokens

def countToken(tok, lst):
	#return lst.count(tok)
	result = 0
	
	for tkn in lst:
		if tok == tkn:
			result += 1
	
	return result

def main():
	tokenList = loadData(sys.argv[1], int(sys.argv[2]))
	
	hapaxCount = 0
	
	for token in tokenList:
		tokenCount = countToken(token, tokenList)
		
		if tokenCount == 1:
			hapaxCount += 1
	
	print len(tokenList), hapaxCount

if __name__ == "__main__":
	cProfile.run('main()', 'hapax.profile')
