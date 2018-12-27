#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PCL-I: Uebung 6 - Aufgabe 1_1, HS15

# Autoren:
# c(Student, Martikelnummer) -> 	{'Roland Benz'			: '97-923-163', 
#									 'Lennart von Thiessen' : '11-185-790'}

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Aufruf des Programms:
# Version 1: python aufgabe1_1.py 
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import codecs

class SACTriple(object):
	"""
	Class representing a triple of token, POS, lemma from the Text+Berg corpus.
	
	Attributes:
		word: A unicode string containing the token
		pos: A unicode string containing the part of speech tag
		lemma: A unicode string containing the lemma of the token
		upos: A unicode string containing the universal POS tag for the token.
	"""

	def __init__(self, line, pos_dict):
		"""
		SACTriple initializer.

		Splits the string passed in and assigns the first part to word, the 
		second to pos, and the third to lemma. Calls _look_up_upos to
		calculate upos.

		Args:
			line: A string in the form "word POS lemma", 
					separated by any whitespace
			pos_dict: A dictionary of POS:UPOS values.
		Returns:
			An SACTriple instance.

		Examples:
		>>> pos_dict = {}
		>>> with codecs.open('pos2upos.tsv') as pos_tbl:
		...     for line in pos_tbl:
		...         l = line.split()
		...         pos_dict[l[0]] = l[1]
		>>> st = SACTriple(u"hat VAFIN haben", pos_dict)
		>>> st.pos
		u'VAFIN'
		>>> st.lemma
		u'haben'
		>>> st.upos, pos_dict
		u'VERB'
		"""
		#helper instance variables
		self.strLine=line
		self.lstLineSplit=self.strLine.split()
		self.pos_dict=pos_dict
		#instance variables
		self.word=self._getToken()
		self.pos=self._getPosTag()
		self.lemma=self._getLemma()
		self.upos=self._look_up_upos()
		print "\nfrom __init__: ", self.word, self.pos, self.lemma, self.upos
    
    #Split the input string
	def _getToken(self):
		return self.lstLineSplit[0]	
	def _getPosTag(self):
		return self.lstLineSplit[1]	
	def _getLemma(self):
		return self.lstLineSplit[2]

	def __eq__(self, other):
		"""
		Two SACTriples are equal when their word, POS and lemma are equal.

		Args:
			other: SACTriple to compare.

		Returns:
			True if all fields of self and other are equal, False if there are
			field mismatches, NotImplemented if other is not an SACTriple.

		Examples:
			>>> triple1 = SACTriple(u"machen VVINF machen", pos_dict)
			>>> triple2 = SACTriple(u"hat VAFIN haben", pos_dict)
			>>> triple3 = SACTriple(u"machen VVINF machen", pos_dict)
			>>> not_a_triple = u"hat VAFIN haben"
			>>> triple1 == triple3 
			True
			>>> triple2 == triple3
			False
			>>> triple2 == not_a_triple
			False
		"""
		#Python ==: compare string characters
		#Java ==: compare string object reference
		#print "\nfrom __eq__: "
		isEqual=False
		try:
			isEqual_w=(self.word==other.word)
			isEqual_p=(self.pos==other.pos)
			isEqual_l=(self.lemma==other.lemma)
			isEqual_u=(self.upos==other.upos)
			if (isEqual_w and isEqual_p and isEqual_l and isEqual_u):
				isEqual=True
		except:
			isEqual=False
		finally:
			return isEqual

	def __repr__(self):
		"""
		Simple string representation function.

		Returns:
			A unicode string of the form 
			SACTriple(u"word POS lemma UPOS", dict)

			The dict is represented as {pos: upos}.

		Examples:
			>>> triple = SACTriple(u"hat VAFIN haben")
			>>> triple
			SACTriple(u"hat VAFIN haben", {u'VAFIN': u'VERB'})
		"""
		#print "\nfrom __repr__: "
		strTmp= "SACTriple(u'" + self.word +" "+ self.pos +" "+ self.lemma +\
					"', {u'" + self.pos + "' : u'" + self.upos + "'})"
		return strTmp
		
	def __str__(self):
		"""
		Pretty string representation.

		Returns:
			A string of the form 
			'Word: word, POS: pos, Lemma: lemma, UPOS: upos'

		Examples:
			>>> triple = SACTriple("hat VAFIN haben", pos_dict)
			>>> print triple
			Word: "hat", POS: "VAFIN", Lemma: "haben", UPOS: "VERB"
		"""
		#print "\nfrom __str__: "
		strTmp="Word: '" + self.word + "' , POS: '" + self.pos + \
				"' , Lemma: '" + self.lemma + "' , UPOS: '"+ self.upos
		return strTmp

	def _look_up_upos(self):
		"""
		Looks up POS in self.pos_dict to find the right unified equivalent of
		the POS tag.

		Args:
			pos_dict: a dictionary with german POS tags as keys and unified POS
						tags as values.

		Returns:
			the UPOS correspondence of the POS tag.
		"""
		#print "\nfrom _look_up_upos: "
		#pos_dict{pos:upos}
		upos=self.pos_dict.get(self.pos, "None")
		return upos

#Main
def main():
	'''tests self.__init__(self, line, pos_dict)'''
	pos_dict = {}
	with codecs.open('pos2upos.tsv') as pos_tbl:
		for line in pos_tbl:
			l = line.split()
			pos_dict[l[0]] = l[1]
	st = SACTriple(u"hat VAFIN haben", pos_dict)
	print "\n should print u'VAFIN': ", st.pos
	print "\n should print u'haben': ",st.lemma
	print "\n should print u'VERB': ", st.upos 
	print "\n should print pos2upos.tsv", pos_dict

	'''tests self.__eq__'''
	triple1 = SACTriple(u"machen VVINF machen", pos_dict)
	triple2 = SACTriple(u"hat VAFIN haben", pos_dict)
	triple3 = SACTriple(u"machen VVINF machen", pos_dict)
	not_a_triple = u"hat VAFIN haben"
	
	iseq=(triple1 == triple3)
	print "\n triple1 == triple3 should return True"
	print " triple1 == triple3: ",iseq
	
	iseq=(triple2 == triple3)
	print "\n triple2 == triple3 should return False"
	print " triple2 == triple3: ",iseq
	
	iseq=(triple2 == not_a_triple)
	print "\n triple2 == not_a_triple should return False"
	print " triple2 == not_a_triple: ",iseq
	
	'''tests self.__repr__'''
	triple = SACTriple(u"hat VAFIN haben", pos_dict)
	print "\n triple should return: "\
			"SACTriple(u'hat VAFIN haben', {u'VAFIN': u'VERB'})"
	print " triple: ", repr(triple)
	

	'''tests self.__str__'''
	triple = SACTriple("hat VAFIN haben", pos_dict)
	print "\n triple should return Word: 'hat', POS: 'VAFIN', Lemma: 'haben', UPOS: 'VERB'"
	print " triple: ", triple
	
			
## This is the standard boilerplate to call the function main
if __name__ == '__main__':
	main()

