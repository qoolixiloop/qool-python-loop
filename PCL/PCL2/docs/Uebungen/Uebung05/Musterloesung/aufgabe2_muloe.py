#!/usr/bin/python
#-*- coding: utf-8 -*- 
#PCL 2, Uebung 05
#Aufgabe 2
#Irene Ma


from nltk.corpus import brown
import re, string, nltk
from collections import defaultdict

rePunct = re.compile("^[" + string.punctuation + "]*$")
reNum = re.compile("^[0-9]*$")
matrix = defaultdict(lambda: defaultdict(float))

def single_cost(token):
	"""
		Helper function to calculate the cost of deletion/insertion
		Args: 
			token: a token
	"""
	global rePunct
	return 0.1 if rePunct.match(token) else 3.0

def compare_cost(x,y):
	"""
		Helper function to calculate the cost of replacement
		Args:
			x,y: tokens to compare
	"""
	global rePunct,reNum
	if x == y:
		return 0.0

	#if x and y are not the same, determine their type and calculate cost
	xClass = "punct" if rePunct.match(x) else "num" if reNum.match(x) else "else"
	yClass = "punct" if rePunct.match(y) else "num" if reNum.match(y) else "else"
	
	if xClass == "punct" and yClass == "punct":
		return 0.1
	elif xClass == "num" and yClass == "num":
		return 4.0
	elif xClass == "else" and yClass == "else":
		return 1.3
	elif xClass != yClass:
		return 16.0
	else:
		raise Exception("Hmm " + x + ", " + y)

def gen_edit_dist(a,b):
	"""
		Function that calculates the general edit distance of two sentences 
		via dynamic programming, top-down (recursive + memoization)

		Args:
			a,b: list of tokens (originally sentences)
	"""
	global matrix

	#if a and b are not empty sentences, continue
	if(len(a) != 0 or len(b) != 0):
		A = " ".join(a)
		B = " ".join(b)

		#if the costs for matrix[A][B] haven't been calculated yet, calculate the minimum cost
		if(not matrix[A][B]):
			ops = []
			if(len(a) != 0 and len(b) != 0):
				#insertion cost
				ops.append(gen_edit_dist(a,b[:-1]) + single_cost(b[-1]))
				#deletion cost
				ops.append(gen_edit_dist(a[:-1],b) + single_cost(a[-1]))
				#replacement cost
				ops.append(gen_edit_dist(a[:-1],b[:-1]) + compare_cost(a[-1],b[-1]))
				#transposing cost
				if(len(a)>1 and len(b)>1 and a[-2] == b[-1] and a[-1] == b[-2]):
					ops.append(gen_edit_dist(a[:-2],b[:-2])+0.4)
				matrix[A][B] = min(ops)

			elif(not len(a)): #B is longer than A
				insCost = gen_edit_dist(a,b[:-1]) + single_cost(b[-1])
				matrix[A][B] = insCost
			elif(not len(b)): #B is shorter than A
				delCost = gen_edit_dist(a[:-1],b) + single_cost(a[-1])
				matrix[A][B] = delCost

	else:
		#if both are empty we are at the start
		A=""
		B=""
		matrix[A][B] = 0.0

	return matrix[A][B]

def main():
	global matrix

	A = raw_input("Sentence A: ")
	B = raw_input("Sentence B (enter brown for d)): ")

	if B != "brown":
		a = nltk.wordpunct_tokenize(A);
		b = nltk.wordpunct_tokenize(B);

		res = gen_edit_dist(a,b)
		
		print "The General Edit Distance of",A,"and",B, "is",res
	else:
		a = nltk.wordpunct_tokenize(A);
		sents = brown.sents()
		
		listofres = [(gen_edit_dist(a,s),s) for s in sents]

		res = min(listofres, key=lambda x: x[0])

		print "The brown sentence closest to '",A,"' is '"," ".join(res[1]),"' with general edit distance",res[0]


if __name__ == "__main__":
	main()



