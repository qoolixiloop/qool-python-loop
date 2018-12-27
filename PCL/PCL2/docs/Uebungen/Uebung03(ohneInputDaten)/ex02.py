#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PCL-I: Uebung 03 - Aufgabe 2, FS16

# Autoren:
# c(Student, Martikelnummer) -> 	{'Roland Benz'			: '97-923-163',
#									 'Linus Manser' 		: '13-791-132'}
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Aufruf des Programms:
# Version 1: python ex02.py
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

'''
2.  n-Gramm-Modelle
Abzugeben ist ein Skript, welches die Korpora aus Aufgabe 1 einliest, die Texte in frei wählbare
n-Gramme umwandelt und die entsprechenden Abfragefunktionen zur Verfügung stellt. Das Skript
sollte sich in den folgenden Aufgaben ohne Probleme als Modul aufrufen lassen.

Schreibe eine Sammlung von Funktionen, welche das Korpus aus Aufgabe 1 in n-Gramme umwandelt
und auf verschiedene Eigenschaften testet:
a) Ein Test, ob ein bestimmtes n-Gramm im Korpus vorkommt.
b) Eine Funktion die eine Liste mit allen n-Grammen ausgibt, welche mit dem gewählten (n-1)-
Gramm beginnen.
c) Eine Funktion zur Berechnung der unbedingten Wahrscheinlichkeit eines n-Gramms.
d) Eine Funktion zur Berechnung der bedingten Wahrscheinlichkeit eines n-Gramms.
e) Eine Funktion welche testet, ob ein n-Gramm eine Kollokation darstellt; die Kriterien sind
selber zu wählen und im Programmcode zu begründen.
Da NLTK schon viele Werkzeuge zum Umgang mit n-Grammen enthält, sollen die Funktionen dei-
ner Sammlung auf keine externe Module zugreifen, ausser natürlich auf deine Implementation von
Aufgabe 1.
'''

import ex01


#a) Ein Test, ob ein bestimmtes n-Gramm im Korpus vorkommt.
def is_n_gram_in_corpus(n_gram):

#b) Eine Funktion die eine Liste mit allen n-Grammen ausgibt,
# welche mit dem gewählten (n-1)-Gramm beginnen.
def list_all_n_grams_conditional_on_nminus1_gram(nminus1_gram):

#c) Eine Funktion zur Berechnung der unbedingten Wahrscheinlichkeit
# eines n-Gramms.
def compute_unconditional_probability_of_n_gram(n_gram):

#d) Eine Funktion zur Berechnung der bedingten Wahrscheinlichkeit
# eines n-Gramms.
def compute_conditional_probability_of_n_gram(n_gram):

#e) Eine Funktion welche testet, ob ein n-Gramm eine Kollokation
# darstellt;
def is_n_gram_a_collocation(n_gram):


if __name__ == "__main__":