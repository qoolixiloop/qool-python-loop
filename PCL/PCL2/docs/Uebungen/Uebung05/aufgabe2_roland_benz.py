#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PCL-I: Uebung 04 - Aufgabe 1, FS16
#
# Autoren:
# c(Student, Martikelnummer) -> {'Roland Benz'	: '97-923-163',
#								 'Linus Manser' : '13-791-132'}
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Reflexion/Feedback
# a) Fasse deine Erkenntnisse und Lernfortschritte in zwei Sätzen
# zusammen.
# Die Arbeiten von Richard Bellman gehören mit zum Schwierigsten,
# was ich an der ETH hätte verstehen sollen. Ich habe diese Übung
# zwar mit viel Aufwand mit einem bottom-up-approach lösen können,
# war jedoch nicht in der Lage einen rekursiven Algorithmus mit
# Memoization zu implementieren. Mir war auch lange nicht klar,
# ob meine Implementation richtig funktioniert, da sie eine
# Subtitution mit Kosten 16 durch ein löschen und einfügen ersetzt.
# In der Matrix also nicht diagonal, sondern erst nach unten dann
# nach rechts geht.
# b) Wie viel Zeit hast du in diese Übungen investiert?
# Roland 20 Stunden
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#import
from __future__ import division
from nltk.corpus import brown
import re, string, nltk
from collections import defaultdict

#global variables
rePunct = re.compile("^[" + string.punctuation + "]*$")
reNum = re.compile("^[0-9]*$")
reWord = re.compile("^[a-zA-ZäöüÄÖÜ0-9_]*$")
matrix = defaultdict(lambda: defaultdict(float))

#debug flag
debug = 0
print_matrix = 1

def main():

	# levenshtein distance for lists of tokens
	#-----------------------------------------
    #PCL Solutions
    #-------------
    print "~~~~~~~~~Beispiel)~~~~~~~~~~~~~~"
    l1 = "Vladimir Levenshtein uebernahm dies im Jahre 1960 .".split()
    l2 = "Vladimir Iosifovich Levenshtein entwickelte dies im Jahre 1965 .".split()
    ld = levenshtein_on_tokens(l1, l2)
    print l1, "\n", l2
    print "ld=3+1.3+4=8.3, ->%s" % (ld)
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"

    print "~~~~~~~~~2a und 2b)~~~~~~~~~~~~~"
    l1 = "Computerlinguistik 2 ist spannend .".split()
    l2 = "Computerlinguistik macht Spass und ist spannend !".split()
    ld = levenshtein_on_tokens(l1, l2)
    print l1, "\n", l2
    print "ld= nicht 22.1, ->%s" % (ld)
    print "\nWeshalb ist 22.1 nicht die Optimale Lösung?\n" \
		  "Meine Version geht wie folgt vor:\n" \
		  "delete: 2 (Kosten 1 * 3)\n" \
		  "insert: macht Spass und (Kosten 3 * 3.0)\n" \
		  "substitute: . und ! (Kosten 1 * 0.1)\n" \
		  "Totale Kosten von 12.1 nicht 22.1\n" \
		  "Die substitution (go diagonal) mit Kosten 16\n" \
		  "wird immer umgangen\n" \
		  "und durch ein delete (go down) und \n" \
		  "ein insert (go right) ersetzt."
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"

    print "~~~~~~~~~2c)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    l1 = "In Raetsel immer Yoda spricht .".split()
    l2 = "Yoda spricht immer in Raetsel .".split()
    ld = levenshtein_on_tokens(l1, l2)
    print l1, "\n", l2
    print "ld=5.2, ->%s" % (ld)
    print "Zwei benachbarte Wörter transponieren\n" \
		  "wurde nicht eingebaut.\n" \
		  "Funktioniert offenbar trotzdem korrekt\n" \
		  "für dieses Beispiel."
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"

    print "~~~~~~~~~2d)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    #load brown corpus sents
    print "Brown categories:\n %s\n" %brown.categories()
    brown_sents=brown.sents(categories = "romance")

    #find minimal distance between l1 and l2
    l1 = "I wish you loved me .".split()
    ld_min=1000 #Startwert

    #iterate through sent in brown corpus
    print"\nUm die beste Lösung zu finden:\n" \
		 "Setze den print_matrix flag auf 0" \
		 "und iteriere über die gesamte Kategorie" \
		 "romance (entferne auf folgender Zeile [0:2]\n"
    for sent in brown_sents[0:2]:

        #calculate distance
        l2 = sent
        ld = levenshtein_on_tokens(l1, l2)

        #print out best match so far
        print l1, "\n", l2
        print "ld= , ->%s" % (ld)
        if ld<ld_min:
            ld_min=ld
            l2_min=l2
        print "ld_min= ", ld_min
        print "l2_min= ", l2_min
        print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"


    # Additional:
    # Test cases
    print"\nZusätzliche Testfälle:\n"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
	# ----------------------------------------
    l1 = "a b c d . a a".split()
    l2 = "a b c d . a b".split()
    ld = levenshtein_on_tokens(l1, l2)
    print l1, "\n", l2
    print "1) ld= 1.3, ->%s" % (ld)
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"

    l1 = "a b c d . a 2".split()
    l2 = "a b c d . a 4".split()
    ld = levenshtein_on_tokens(l1, l2)
    print l1, "\n", l2
    print "2) ld= 4.0, ->%s" % (ld)
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"

    l1 = "a b .".split()
    l2 = "a b !".split()
    ld = levenshtein_on_tokens(l1, l2)
    print l1, "\n", l2
    print "3) ld= 0.1, ->%s" % (ld)
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"

    l1 = "a b c 4".split()
    l2 = "a b c .".split()
    ld = levenshtein_on_tokens(l1, l2)
    print l1, "\n", l2
    print "4) ld= 16.0?, ->%s" % (ld)
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"

    l1 = "a b c d".split()
    l2 = "a e".split()
    ld = levenshtein_on_tokens(l1, l2)
    print l1, "\n", l2
    print "5) ld= 7.3, ->%s" % (ld)
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"

    l1 = "a b c d .".split()
    l2 = "a e i o".split()
    ld = levenshtein_on_tokens(l1, l2)
    print l1, "\n", l2
    print "6) ld= 4.0, ->%s" % (ld)
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"

    l1 = "a b c d !".split()
    l2 = "a b c d .".split()
    ld = levenshtein_on_tokens(l1, l2)
    print l1, "\n", l2
    print "7) ld= 0.1, ->%s" % (ld)
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"

    l1 = "!".split()
    l2 = "b".split()
    ld = levenshtein_on_tokens(l1, l2)
    print l1, "\n", l2
    print "8) ld= 16?, ->%s" % (ld)
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"

    l1 = "! 3 4".split()
    l2 = "b ? a".split()
    ld = levenshtein_on_tokens(l1, l2)
    print l1, "\n", l2
    print "9) ld=? , ->%s" % (ld)
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"

    l1 = "l e v e n s h t e i n".split()
    l2 = "m e i l e n s t e i n".split()
    ld = levenshtein_on_tokens(l1, l2)
    print l1, "\n", l2
    print "10) ld=? , ->%s" % (ld)
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"


    # levenshtein distance for strings of characters
    # -----------------------------------------------
    print"\nZusätzlich:"
    print "levenshtein distance for strings of chars\n" \
		  "Dieser Algorithmus war das Grundgerüst der\n" \
		  "gesamten Aufgabe"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    s1 = "kitten"
    s2 = "sitting"
    ld = levenshtein_on_characters(s1, s2)
    print "\nld= ", ld
    print s1, "\n", s2



#The first version is a Dynamic Programming algorithm,
#with the added optimization that only the last two rows of
#the dynamic programming matrix are needed for the computation:

def levenshtein_on_tokens(l1, l2):

    # l1 must be the longer list
    if len(l1) < len(l2):
        return levenshtein_on_tokens(l2, l1)

    # now len(l1) >= len(l2)
    if len(l2) == 0:
        return len(l1)

    # first row
    previous_row=[0]
    for j, c2 in enumerate(l2):
        previous_row.append(previous_row[j]+costs_insertion(c2))
    if (print_matrix):
        print ("%5s")%(""),
        for j, c2 in enumerate(l2):
            print ("%5s" % (c2[:4])),
        print
        for j, c2 in enumerate(l2):
            print ("%5s" % (previous_row[j])),
        print ("%5s" % (previous_row[j+1])),
        print

    # iterate through the longer list (go down)
    for i, c1 in enumerate(l1):

        if (debug): print "i=%s, c1=%s" % (i+1, c1)

        # first element of row i+1
        current_row = [previous_row[0]+costs_deletion(c1)]

        if (debug): print " current_row", current_row

        # iterate through the smaller list (go right)
        for j, c2 in enumerate(l2):

            if (debug): print "   j=%s, c2=%s" % (j+1, c2)

            """"
            compare current element (i+1,j+1) with:
            element above (i,j+1): equivalent to previous_row[j + 1]
            element left (i+1,j): equivalent to current_row[j]
            element left above (i,j): previous_row[j]
            """

            #element above: move down -> delete label from l1
            cost_deletion = costs_deletion(c1)#1
            deletions = previous_row[j + 1] + cost_deletion
            deletions = round(deletions,2)

            #element left: move right -> insert label of l2 to l1
            cost_insertion = costs_insertion(c2)#1
            insertions = current_row[j] + cost_insertion
            insertions = round(insertions, 2)

            #element left above -> substitute or keep
            cost_substitution = (c1 != c2)*costs_substitution(c1,c2)#(c1 != c2)
            substitutions = previous_row[j] + cost_substitution
            substitutions = round(substitutions, 2)

            #current element gets the min of its neighbours
            #above, left, and left above
            current_row.append(
                min(insertions, deletions, substitutions))

            if (debug): print "   cost_insertion, cost_deletion, cost_substitution", \
                cost_insertion, cost_deletion, cost_substitution

        if (print_matrix):
            for j, c2 in enumerate(l2):
                print ("%5s" %(current_row[j])),
            print ("%5s %5s" % (current_row[j+1],c1)),
            print

        # previous row gets updated
        previous_row = current_row

    #return last element of last row
    return previous_row[-1]


def costs_insertion(x):
    # 1. Eine Interpunktion einfügen: 0.1
    # Alles andere einfügen: 3.0

    match_obj = re.match(rePunct, x)

    if (match_obj):
        return 0.1
    else:
        return 3.0


def costs_deletion(x):
    # 2. Eine Interpunktion entfernen: 0.1
    # Alles andere entfernen: 3.0

    match_obj = re.match(rePunct, x)

    if (match_obj):
        return 0.1
    else:
        return 3.0


def costs_substitution(x, y):
    # 3. Element x mit Element y ersetzen:
    # x und y sind beides Interpunktionen: 0.1
    # x und y sind beides Zahlen: 4.0
    # x und y sind beides Wörter (‘abc3’ gilt als ein Wort): 1.3
    # x und y sind nicht vom gleichen Typ: 16.0

    match_obj_x_punct = re.match(rePunct, x)
    match_obj_y_punct = re.match(rePunct, y)

    match_obj_x_num = re.match(reNum, x)
    match_obj_y_num = re.match(reNum, y)

    match_obj_x_word = re.match(reWord, x)
    match_obj_y_word = re.match(reWord, y)

    # x und y sind beides Interpunktionen: 0.1
    if (match_obj_x_punct and match_obj_y_punct):
        return 0.1

    # x und y sind beides Zahlen: 4.0
    elif (match_obj_x_num and match_obj_y_num):
        return 4.0

    # x und y sind beides Wörter (‘abc3’ gilt als ein Wort): 1.3
    elif (match_obj_x_word and match_obj_y_word
          and not match_obj_x_num and not match_obj_y_num):
        return 1.3

    # x und y sind nicht vom gleichen Typ: 16.0
    else:
        return 16.0


#DP
def levenshtein_on_characters(s1, s2):
    """The Levenshtein algorithm (also called Edit-Distance) calculates the least
    number of edit operations that are necessary to modify one string to obtain
    another string. The most common way of calculating this is by the dynamic
    programming approach. A matrix is initialized measuring in the (m,n)-cell
    the Levenshtein distance between the m-character prefix of one with the
    n-prefix of the other word. The matrix can be filled from the upper left
    to the lower right corner. Each jump horizontally or vertically corresponds
    to an insert or a delete, respectively. The cost is normally set to 1 for each
    of the operations. The diagonal jump can cost either one, if the two characters
    in the row and column do not match or 0, if they do. Each cell always minimizes
    the cost locally. This way the number in the lower right corner is the
    Levenshtein distance between both words. Here is an example that features
    the comparison of "meilenstein" and "levenshtein":"""

    if len(s1) < len(s2):
        return levenshtein_on_characters(s2, s1)

    # len(s1) >= len(s2)
    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    if (debug): print "previous_row", previous_row

    for i, c1 in enumerate(s1):

        if (debug): print "i=%s, c1=%s" %(i, c1)
        current_row = [i + 1]

        if (debug): print " current_row", current_row

        for j, c2 in enumerate(s2):

            if (debug): print "   j=%s, c2=%s" % (j, c2)

            # j+1 instead of j since previous_row and current_row
            # are one character longer than s2

            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)

            if (debug): print "   insertions, deletions, substitutions", \
                insertions, deletions, substitutions

            current_row.append(
                min(insertions, deletions, substitutions))

        if (debug): print " current_row", current_row
        previous_row = current_row

    return previous_row[-1]


if __name__ == "__main__":
	main()