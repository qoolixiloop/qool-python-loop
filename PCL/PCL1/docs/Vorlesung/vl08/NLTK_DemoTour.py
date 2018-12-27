#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nltk.book import *
print "from 0 :"
texts()
#Texte sind Sequenzen von Tokens
# (Textanzeige)
print "from 1 :"
print text1[0:10]
print "from 2 :"
print text2[0:10]
#Konkordanzen erstellen
#KWIC (Keyword in Context)
# (Stichwort mit etwas Text davor -B6 oder danach -A6 )
print "from 3 :"
text1.concordance("man") #Keyword=man
print "from 4 :"
text2.concordance("man")
print "from 5 :"
text1.concordance("woman") #Keyword=woman
print "from 6 :"
text2.concordance("woman")
#Ähnlichkeit Similarity
# (andere Wörter, welche in ähnlichen Kontexten auftauchen)
print "from 7 :"
text1.similar("woman")
print "from 8 :"
text2.similar("woman")
print "from 9 :"
text1.similar("love")
print "from 10 :"
text2.similar("love")
# Häufigkeit in einem Korpus
# (word count $wc oder grep -c)
print "from 11 :"
print text1.count('love')
print "from 12 :"
print text2.count('love')
# Häufigkeitsdistributionen
# Alle Häufigkeiten aller verschiedenen Tokens berechnen
# (grep "\b.*\b" "filename" | )
print "from 13_1:"
fdist1 = FreqDist(text1)
print type(fdist1)
vocabulary1= sorted(fdist1, key=fdist1.get,reverse=True)
for w in vocabulary1[:50]:
    print w, "\t\t", fdist1[w]
print "from 13_1:"
fdist2 = FreqDist(text2)
print type(fdist2)
vocabulary2= sorted(fdist2, key=fdist2.get,reverse=True)
for w in vocabulary2[:20]:
    print w, "\t\t", fdist2[w]
print "from 14_1 :"
fdist1.plot(50,cumulative=False)
print "from 14_2 :"
fdist2.plot(20,cumulative=False)
# Statistische Kollokationen
# Welche Wörter kommen unerwartet häufig nebeneinander vor?
print "from 15 :"
text1.collocations()
print "from 16 :"
text2.collocations()
# Dispersions Plots
# Wo tauchen auf einer Zeitachse Wörter wie oft auf?
# Amerikanische Ansprachen
print "from 17 :"
text4.dispersion_plot(["freedom","war"])
print "from 18 :"
text4.dispersion_plot(["economy","war"])
# Textgenerierung
# Statistische Generierung von Texten aus Trigramm-Statistiken von Wörtern.
# Typischer Wortverbindungen aus einem Korpus.
# (In NLTK 3 momentan kaputt.) Politische Rede?
# Sich inspirieren lassen von präsidialen
# Ansprachen der vergangenen Präsidenten der USA.
print "from 19 :"
#text4.generate()
"""Fellow - Countrymen : At this second gathering , our commerce and
share them . Instead of undertaking particular recommendations on this
occasion , feeling the emotions which the Executive , in seeking
practical plans for mediation , conciliation , and evil is real , and
defense ; if a preference , upon a party , and we have piled deficit
upon deficit , mortgaging our future is this which gives inestimable
value to those who came here believed they could to merit it can
deliver ; from inflated rhetoric that postures instead of others , and
by our own"""
# Listenkomprehension
print "from 20 :"
V = set(text1)
long_words = [w for w in V if len(w)>15]
print long_words