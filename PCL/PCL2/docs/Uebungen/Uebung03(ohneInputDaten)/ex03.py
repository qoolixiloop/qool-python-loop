#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PCL-I: Uebung 03 - Aufgabe 3, FS16

# Autoren:
# c(Student, Martikelnummer) -> 	{'Roland Benz'			: '97-923-163',
#									 'Linus Manser' 		: '13-791-132'}
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Aufruf des Programms:
# Version 1: python ex03.py
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

'''
3 Klassifikation: Spam, Spam, Spam!
Nun ist es an der Zeit, die Daten einzusetzen um Emails auf Spam (unerwünschte) und Ham (er-
wünschte Emails) zu klassifizieren.
Verfahre analog zu Sektion 1.3 von Kapitel 6 im NLTK-Buch, wobei hier die Struktur deines Korpus
(oder deiner Korpora) den Ablauf stark beeinflusst.

a) Verwende am Anfang noch keine Merkmale (Features), sondern das untenstehende Code-
Schnipsel. Die resultierende Präzision des Klassifikators stellt die Baseline dar, welche dir bei
der Weiterentwicklung deiner Merkmale hilft. Auf welcher Basis entscheidet der Klassifikator,
ob ein Dokument Spam oder Ham ist?

b) Erstelle nun eigene Merkmale wie in Sektion 1.3 beschrieben steht. Experimentiere mit ver-
schiedenen Merkmalen sowie deren Kombinationen, vergleiche die Präzision deines Klassifika-
tors mit der Baseline und notiere deine Feststellungen direkt im Programmcode beim jeweiligen
Merkmal.
'''

# empty dictionary to comply with the requirements
def document_features (document , words):
    return{}


if __name__ == "__main__":
