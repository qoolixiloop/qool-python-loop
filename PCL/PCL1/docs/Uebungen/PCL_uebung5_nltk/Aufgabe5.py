#!/usr/bin/env python
# -*- coding: utf-8 -*-
#PCL I, Übung 5, HS15
#Aufgabe 5
#Autor: Dein Name
#Matrikel-Nr.: Deine Matrikel-Nr

import nltk, operator
from nltk.corpus import webtext


#Dein Code


def printresult(dict):
	dict_sorted = sorted(dict.items(), key = operator.itemgetter(1)) #sortiert dict nach Wert
	#Dein Code


def main():
	text = webtext.words('grail.txt')
	#Dein Code


if __name__ == "__main__":
	main()