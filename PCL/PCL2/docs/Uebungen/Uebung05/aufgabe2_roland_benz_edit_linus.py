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
		  "Unsere Version geht wie folgt vor:\n" \
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
    l1 = "spricht Yoda in immer Raetseln .".split()
    l2 = "Yoda spricht immer in Raetseln !".split()
    ld = levenshtein_on_tokens(l1, l2)
    print l1, "\n", l2
    print "ld=0.9, ->%s" % (ld)
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
    l1 = "das ist !".split()
    l2 = "ist das !".split()
    ld = levenshtein_on_tokens(l1, l2)
    print l1, "\n", l2
    print "ld=0.4, ->%s" % (ld)
    print "~~~~~~~~~2d)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    #load brown corpus sents
    print "Brown categories:\n %s\n" %brown.categories()
    brown_sents=brown.sents(categories = "romance")

    #find minimal distance between l1 and l2
    l1 = "I wish you loved me .".split()
    ld_min=1000 #Startwert

    #iterate through sent in brown corpus
    print"\nUm die beste Lösung zu finden:\n" \
		 "Setze den print_matrix flag auf 0 " \
		 "und iteriere über die gesamte Kategorie " \
		 "romance (entferne auf nachfolgender Zeile [0:2])\n"
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
    l2 = "a b c d . a c".split()
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
    print "4) ld= nicht 16.0, 3.1, ->%s" % (ld)
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
    print "8) ld= nicht 16, 3.1 , ->%s" % (ld)
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"

    l1 = "! 3 4".split()
    l2 = "b ? a".split()
    ld = levenshtein_on_tokens(l1, l2)
    print l1, "\n", l2
    print "9) ld=12.1 , ->%s" % (ld)
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"

    l1 = "l e v e n s h t e i n".split()
    l2 = "m e i l e n s t e i n".split()
    ld = levenshtein_on_tokens(l1, l2)
    print l1, "\n", l2
    print "10) ld=7.8 , ->%s" % (ld)
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
    """
    function to return a levenshtein-distance (float)
    This task was solved BOTTM-UP (starting at the first
        token an continue up to the whole sentence)
    input:  two sentences
    output: levenshtein distance (float)
    """

    # l1 must be the longer list
    if len(l1) < len(l2):
        return levenshtein_on_tokens(l2, l1)

    # now len(l1) >= len(l2)
    if len(l2) == 0:
        return len(l1)

    pprevious_row=[]
    
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


            # element above: move down -> delete label from l1
            cost_deletion = costs_deletion(c1)#1
            deletions = previous_row[j + 1] + cost_deletion
            deletions = round(deletions, 2)

            # element left: move right -> insert label of l2 to l1
            cost_insertion = costs_insertion(c2)#1
            insertions = current_row[j] + cost_insertion
            insertions = round(insertions, 2)

            # element left above -> substitute or keep
            cost_substitution = (c1 != c2)*costs_substitution(c1,c2)#(c1 != c2)
            substitutions = previous_row[j] + cost_substitution
            substitutions = round(substitutions, 2)

            ## implementation of transposing costs
            transposing = False
            try:
                transposing_list1 = [l1[i], l1[i-1]]
                transposing_list2 = [l2[j], l2[j-1]]
                ##  by jumping over one row and accessing the pprev-row directly, the matrix 
                #   doesn't get filled in correctly, because the computing-steps in
                #   between don't get ignored. This makes it impossible to backtrack the path nicely
                transposing = pprevious_row[j-1] + costs_transposing(transposing_list1,\
                     transposing_list2)
            except IndexError:
                None
            except TypeError:
                None

            # in case a tranposition is possible, consider it as a possible minimal value as well
            if transposing:
                current_row.append(min(insertions, deletions, substitutions, transposing))
    
            current_row.append(min(insertions, deletions, substitutions))

            if (debug): print "   cost_insertion, cost_deletion, cost_substitution", \
                cost_insertion, cost_deletion, cost_substitution

        if (print_matrix):
            for j, c2 in enumerate(l2):
                print ("%5s" %(current_row[j])),
            print ("%5s %5s" % (current_row[j+1],c1)),
            print

        # previous row gets updated
        if (previous_row): pprevious_row = previous_row
        previous_row = current_row

    #return last element of last row
    return previous_row[-1]

def costs_transposing(x,y):
    """
    input:  two lists with len = 2
    output: returns the cost of 0.4 if the items in the list
            satisfy the condition to be able to be transposed

    Ex: Yoda spricht immer in Rätseln!
        spricht Yoda in immer Rätseln!
        extracted lists as input for this function:
        ["Yoda", "spricht"], ["spricht", "Yoda"]
        -> returns 0.4
    """
    try:
        if x[1] == y[0] and x[0] == y[1]:
            return 0.4
    # if the lists aren't long enough (at the start/end of the sentence)
    except IndexError:
        None


def costs_insertion(x):
    """
    cost-function for insertions of a token

    input:  a single token
    output: depending on the type of token (punctuation or not)
            returns the cost:
                > punctuation:      0.1
                > everything else:  3.0
    """
    # checks whether the token is a punctuation
    match_obj = re.match(rePunct, x)

    if (match_obj):
        return 0.1
    else:
        return 3.0


def costs_deletion(x):
    """
    cost-function for deletions of a token

    input:  a single token
    output: depending on the type of token (punctuation or not)
            returns the cost:
                > punctuation:      0.1
                > everything else:  3.0
    """
    # checks whether the token is a punctuation
    match_obj = re.match(rePunct, x)

    if (match_obj):
        return 0.1
    else:
        return 3.0


def costs_substitution(x, y):
    """
    cost-function for substitutions of tokens

    input:  two tokens
    output: returns the cost according to the combination
            of tokens:
                > x,y are both punctuations: 0.1
                > x,y are both numbers:      4.0
                > x,y are both words:        1.3
                (as soon as the string contains a alphabetical 
                    character it counts as word)
                > x,y are different types:   16.0
    """
    # checking the types of the tokens x and y
    match_obj_x_punct = re.match(rePunct, x)
    match_obj_y_punct = re.match(rePunct, y)

    match_obj_x_num = re.match(reNum, x)
    match_obj_y_num = re.match(reNum, y)

    match_obj_x_word = re.match(reWord, x)
    match_obj_y_word = re.match(reWord, y)

    # both are punctuations
    if (match_obj_x_punct and match_obj_y_punct):
        return 0.1

    # both are numbers
    elif (match_obj_x_num and match_obj_y_num):
        return 4.0

    # both are words
    elif (match_obj_x_word and match_obj_y_word
          and not match_obj_x_num and not match_obj_y_num):
        return 1.3

    # they are from a different type
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