#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Author
#------
#Roland Benz, 97-923-163

#Dieses Programm ausführen mit: 
#------------------------------
#python uebung02_aufgabe05.py


#5 Wortendungen erkennen
#Wir wollen ein Programm erstellen, das den Nutzer wiederholt nach einem deutschen Wort fragt, die
#Wortendungen untersucht und dann passenden Wortarten zuordnet.
print "\nDear user, this script determines\n word classes."
quitNow = False
while not quitNow:
	strIn=raw_input("\nPlease enter one German word:\n")
	print "\nYou entered:\n" + strIn + "\n"
	listStrIn=strIn.split(" ")
	quitNow=(strIn=="q")
	oneWord=(len(listStrIn)==1)
	emptyWord=(len(strIn)==0)
	inputIsOK = (oneWord and not emptyWord and not quitNow)
	if inputIsOK:
		#Rules for word classes
		#----------------------
		last2=strIn[-2:]
		last3=strIn[-3:]
		last4=strIn[-4:]
		first2=strIn[:2]
		first3=strIn[:3]
		first4=strIn[:4]
		#Those which are countable
		#-------------------------
		#Pronouns are countable, a not complete list of personal/possessive/reflexive... pronouns
		isAPronoun = (strIn=="ich" or strIn=="du" or strIn=="er" or strIn=="sie" 
										or strIn=="wir" or strIn=="dir" or strIn=="ihr" or strIn=="euch" 
										or strIn=="mein" or strIn=="dein" or strIn=="mir" 
										or strIn=="dir" or strIn=="uns")
		#Conjunctions are countable, a not complete list
		isAConjunction= (strIn=="und" or strIn=="sowie" or strIn=="als")
		#Prepositons are countable, a not complete list
		isAPreposition=(strIn=="nach" or strIn=="über" or strIn=="zu" or strIn=="bei" 
										or strIn=="unter" or strIn=="neben" or strIn=="vor")
		#Articles are countable, a not complete list of definite and indefinite pronouns
		isAnArticle=(strIn=="der" or strIn=="die" or strIn=="das" or strIn=="dem" or strIn=="den" 
									or strIn=="ein" or strIn=="eine" or strIn=="einen" or strIn=="einem")
		#Those which are neighter countable nor have a morphological pattern
		#-------------------------------------------------------------------
		#Adverbs have no morphological patterns
		isAnAdverb=()
		#Particles have no morphological patterns
		isAParticle= ()
		#Adjectives Positive have no morphological pattern but 
		#syntactic patterns e.g. (lie between article and noun)
		isAnAdjPos=()
		#Those with morphological patterns
		#---------------------------------
		#Nouns are not countable and have tons of different patterns
		isANomen = (last4 == "heit" or last3 =="ant" or last3 =="net" or last4=="ment")
		#Adjectives Comparative are not countable but have some strong patterns 
		isAnAdjComp = (last3=="ser" or last3=="her" or last3=="ter" or last3=="ner")
		#Adjectives Superlative are not countable but have a strong pattern
		isAnAdjSup = (last4 == "sten")
		#Verbs are not countable and have tons of different patterns
		isAVerb = ((last2 == "te") or (first2=="ge" and last2=="en") or (last3=="end"))
		#Output
		if isAConjunction:
			print "<"+ strIn + "> is very likely a conjunction\n"
		elif isAPreposition:
			print "<"+ strIn + "> is very likely a preposition\n"
		elif isAnArticle:
			print "<"+ strIn + "> is very likely a article\n"
		elif isAPronoun:
			print "<"+ strIn + "> is very likely a pronoun\n"
		elif isAParticle:
			print "<"+ strIn + "> is very likely a particle\n"
		elif isAnAdverb:
			print "<"+ strIn + "> is very likely an adverb\n"
		elif isAnAdjPos:
			print "<"+ strIn + "> is very likely an adjective positive\n"
		elif isAnAdjSup:
			print "<"+ strIn + "> is very likely an adjective superlative\n"
		elif isAnAdjComp:
			print "<"+ strIn + "> is very likely an adjective comparative\n"
		elif isAVerb:
			print "<"+ strIn + "> is very likely a verb\n"
		elif isANomen:
			print "<"+ strIn + "> is very likely a nomen\n"
		else:
			print "sorry, no rule or pattern yet for the word <"+ strIn + ">!\n" 
	else:
		if (not oneWord or emptyWord):
			print "Oops, something went wrong!"
		if quitNow:
			print "Good bye!\n"
		continue


#Der Programmablauf sollte ungefähr so aussehen:
#B i t t e gebe e i n d e u t s c h e s Wort e i n , Abbruch mit ’ q ’ :
#fährt
#Das e i n g e g e b e n e Wort i s t s e h r w a h r s c h e i n l i c h e i n Verb .
#B i t t e gebe e i n d e u t s c h e s Wort e i n , Abbruch mit ’ q ’ :
#q
#Auf Wiedersehen !
#Es ist euch freigestellt, welche Kriterien zur Unterscheidung einsetzt, teilweise ist es sicher nützlich,
#mehrere Bedingungen zu verschachteln.
#Folgende Beispiele sind gute Ansätze zur Wortartenerkennung:
#• ”-heit” für Nomen
#• ”-sten” für Adjektive im Superlativ
#• ”-te” für Verben
#Abzugeben ist das komplette, ausführbare Programm.
