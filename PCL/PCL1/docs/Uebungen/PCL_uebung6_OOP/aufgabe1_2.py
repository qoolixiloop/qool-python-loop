#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PCL-I: Uebung 6 - Aufgabe 1_2, HS15

# Autoren:
# c(Student, Martikelnummer) -> 	{'Roland Benz'			: '97-923-163', 
#									 'Lennart von Thiessen' : '11-185-790'}

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Aufruf des Programms:
# Version 1: python aufgabe1_2.py 
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


'''
a) __init__: Initialisierung der Klasse.
b) __eq__: Implementiert den Operator ==
c) __getitem__: Implementiert den Operator []
d) __contains__: Implementiert den Operator in
e) __str__: Wird von print aufgerufen
f) index: Gibt die erste Position zurück, an der ein Substring 
gefunden wurde.

>>> ns1 = Normalstring(u'môr')
>>> ns2 = Normalstring(u'mor')
>>> ns3 = Normalstring(u'Mor')
>>> ns1 == ns2
True
>>> ns2 == ns3
False
>>> u'ô' in ns2
True
>>> ns1[1] == ns2[1]
True
>>> print ns1
mor
>>> ns2.index(u'ô')
1
>>> ns1.unnormal
u'môr'

'''

import unicodedata

#Klassendefiniton
class Normalstring(object):
	
	'''a) __init__: Initialisierung der Klasse.'''
	def __init__(self, str_):
		#instance variable of unnormalized input
		self.unnormal = str_
		#processed instance variable (input normalized)
		self.normal = self.normalize(self.unnormal)
		
	'''b) __eq__: Implementiert den Operator ==	
				auf der normalisierten Instanzvariablen!'''
	def __eq__(self, other):
		isEqual=False
		#print self, other, isEqual
		'''ginge vermutlich auch einfacher mit == Operator für Strings'''
		for iter_ in range(0, len(self.normal)):
			isEqual=(self.normal[iter_]==other.normal[iter_])
			#print self.normal, other.normal, isEqual
			if isEqual==False:
				break
		return isEqual
	
	'''c) __getitem__: Implementiert den Operator []
			auf der normalisierten Instanzvariablen!'''
	def __getitem__(self, item_):
		#returns character of string at item_
		#return self.unnormal[item_]
		return self.normal[item_]

	'''d) __contains__: Implementiert den Operator in
			auf dem normalisierten Inputstring str_ und 
			der normalisierten Instanzvariablen!'''
	def __contains__(self, str_):
		#checks if instance variable contains str_
		str_normalized=self.normalize(str_)
		selfContainsStr_=(str_normalized in self.normal)
		'''selfContainsStr_=(str_ in self.unnormal) #returns False!!'''
		return selfContainsStr_
	
	'''e) __str__: Wird von print aufgerufen'''	
	def __str__(self):
		#returns instance variable
		'''return "Unnormalized: " + self.unnormal #throws UnicodeEncodeError'''
		return self.normal
	
	'''f) index: Gibt die erste Position zurück, an der 
				ein Substring gefunden wurde, 
				auf dem normalisierten Inputstring str_ und 
				der normalisierten Instanzvariablen!'''	
	def index(self, str_):
		#returns first index of str_ in instance variable
		try:
			str_normalized=self.normalize(str_)
			strFound=self.normal.index(str_normalized, 0, len(self.normal))
			#print str_normalized, self.normal
		except:
			strFound=0
		finally:
			return strFound
				
	'''Beim Normalisieren hilft das Modul unicodedata. 
	   Verwende dazu diese Funktion'''		
	def normalize(self, str_):
		nfkd_form = unicodedata.normalize('NFKD', str_)
		return u"".join(c for c in nfkd_form if not unicodedata.combining(c))

					
#Main		
ns1 = Normalstring(u'môr')
print "\n ns1: ", ns1.unnormal, ns1.normal
ns2 = Normalstring(u'mor')
print " ns2: ", ns2.unnormal, ns2.normal
ns3 = Normalstring(u'Mor')
print " ns3: ", ns3.unnormal, ns3.normal, "\n"

iseq=(ns1 == ns2)
print "\n ns1==ns2 should return True"
print " ns1==ns2: ", iseq

iseq=(ns2 == ns3)
print "\n ns2==ns3 should return False"
print " ns2==ns3: ", iseq

contains=(u'ô' in ns2)
print "\n u'ô' in ns2 should return True"
print " u'ô' in ns2: " , contains

'''Bemerkung: hier wird nicht 
	Normalstring.__eq__(self, other) aufgerufen!!'''
iseq=(ns1[1] == ns2[1])
print "\n ns1[1]==ns2[1] should return True"
print " ns1[1]==ns2[1]: ",iseq

print "\n print ns1 should return mor"
print " ns1: ", ns1

var=ns2.index(u'ô')
print "\n ns2.index(u'ô') should return 1"
print " ns2.index(u'ô') " , var

var=ns1.unnormal
print "\n ns1.unnormal should return u'môr'"
print " ns1.unnormal " , var



'''
Übersicht über die magischen Methoden

Binäre Operatoren
Operator 	Methode
+ 	object.__add__(self, other)
- 	object.__sub__(self, other)
* 	object.__mul__(self, other)
// 	object.__floordiv__(self, other)
/ 	object.__div__(self, other)
% 	object.__mod__(self, other)
** 	object.__pow__(self, other[, modulo])
<< 	object.__lshift__(self, other)
>> 	object.__rshift__(self, other)
& 	object.__and__(self, other)
^ 	object.__xor__(self, other)
| 	object.__or__(self, other)

Erweiterte Zuweisungen
Operator 	Methode
+= 	object.__iadd__(self, other)
-= 	object.__isub__(self, other)
*= 	object.__imul__(self, other)
/= 	object.__idiv__(self, other)
//= 	object.__ifloordiv__(self, other)
%= 	object.__imod__(self, other)
**= 	object.__ipow__(self, other[, modulo])
<<= 	object.__ilshift__(self, other)
>>= 	object.__irshift__(self, other)
&= 	object.__iand__(self, other)
^= 	object.__ixor__(self, other)
|= 	object.__ior__(self, other)

Unäre Operatoren
Operator 	Methode
- 	object.__neg__(self)
+ 	object.__pos__(self)
abs() 	object.__abs__(self)
~ 	object.__invert__(self)
complex() 	object.__complex__(self)
int() 	object.__int__(self)
long() 	object.__long__(self)
float() 	object.__float__(self)
oct() 	object.__oct__(self)
hex() 	object.__hex__(self)

Vergleichsoperatoren
Operator 	Methode
< 	object.__lt__(self, other)
<= 	object.__le__(self, other)
== 	object.__eq__(self, other)
!= 	object.__ne__(self, other)
>= 	object.__ge__(self, other)
> 	object.__gt__(self, other)
'''
