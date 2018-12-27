#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PCL-I: Uebung 06 - FS16
#
# Autoren:
# c(Student, Martikelnummer) -> {'Roland Benz'	: '97-923-163',
#								 'Linus Manser' : '13-791-132'}
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Aufgabe 1:
# siehe 'Aufgabe01.jpg'
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Aufgabe 3:
# (Wir haben uns entschieden, den PCFG-Parser direkt in die Aufgabe 2
# zu integrieren. Je nach Grammatik (mit oder ohne Wahrscheinlichkeiten)
# waehlt das Script den funktionierenden Parser aus.)
# 
# Bei der PCFG ergeben sich unter anderem diese Schwierigkeiten:
# - Lexikalische Informationen werden bei der Beschaffung der Wahrschein-
#   lichkeiten nicht miteinbezogen. Dies würde viele Ambiguitäten aus
#   dem Weg schaffen.
# - Die Summe der Wahrscheinlichkeiten für jede Art von Regel muss 1.0
#   ergeben. Dies führt bei inkompletten Grammatiken zu teils falschen 
#   Wahrscheinlichkeitsverteilungen bzw. man schreibt einem Konstituenten
#   einen zu hohen Wert zu.
# 
# Gegeben: NP -> Det N [0.4] | Det N PP [0.3] | 'I' [0.3]
# ... haben wir gesehen, dass bei 'VP -> V NP [0.25] | VP PP [0.75]'
# der Wendepunkt für die beiden verschiedenen Baumvarianten ist.
# Theoretisch sollten nur diese Regeln für die verschiedenen Baum-
# varianten ausschlaggebend sein. Jedoch haben wir es noch nicht 
# geschafft, den Parser so weit zu bringen, dass er sich gar nicht
# entscheiden kann und beide Varianten ausgibt.
#
# komplette Ausgabe (fyi)
# S -> NP VP [1.0]
# PP -> P NP [1.0]
# NP -> Det N [0.4] | Det N PP [0.3]| 'I' [0.3]
# VP -> V NP [0.25] | VP PP [0.75]
# Det -> 'an' [0.5] | 'my' [0.5]
# N -> 'elephant' [0.6] | 'pajamas' [0.4]
# V -> 'shot' [1.0]
# P -> 'in' [1.0]

# # Wendepunkt bei:
# VP -> V NP [0.25] | VP PP [0.75]

# VP PP mehr als 0.75:
#         S                                                            
#  ┌──────┴───────────────────────┐                                        
#  │                              VP                                   
#  │              ┌───────────────┴────────────────┐                       
#  │              VP                               PP                  
#  │      ┌───────┴──────┐                  ┌──────┴──────┐                
#  │      │              NP                 │             NP           
#  │      │       ┌──────┴────────┐         │      ┌──────┴────────┐       
#  NP     V      Det              N         P     Det              N   
#  │      │       │               │         │      │               │       
#  I     shot     an           elephant     in     my           pajamas
 
#  VP PP weniger als 0.75:
#         S                                                     
#  ┌──────┴────────────────┐                                        
#  │                       VP                                   
#  │      ┌────────────────┴─────────┐                              
#  │      │                          NP                         
#  │      │       ┌────────┬─────────┴──────┐                       
#  │      │       │        │                PP                  
#  │      │       │        │         ┌──────┴──────┐                
#  │      │       │        │         │             NP           
#  │      │       │        │         │      ┌──────┴────────┐       
#  NP     V      Det       N         P     Det              N   
#  │      │       │        │         │      │               │       
#  I     shot     an    elephant     in     my           pajamas
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Reflexion/Feedback
# a) Ich habe ein neues Modul von nltk kennengelernt, welches mir 
#    erlaubt mit kontextfreien Grammatiken (mit oder ohne Wahr-
#    scheinlichkeiten) Syntaxbäume zu generieren und sie auf 
#    verschiedene Arten auszugeben. Zusätzlich konnte ich mit
#    der ersten auf Aufgabe von Hand den CYK-Algorithmus "visualisieren" 
#    und ihn somit besser kennenlernen.
#    
# b) 8 Stunden
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#imports
import nltk
import argparse
import sys
import os

#debug flag - set to 1 if in debug mode
DEBUG = 0


def build_tree_variations(parser, sent):
    """
    function that compiles all possible or the most probable tree(s)
    for a sentence, depending on which parser you use

    input:  parser (ChartParser, ViterbiParser, ...)
            a sentence which needs to be parsed
    output: ChartParser -> all possible trees
            ViterbiParser -> most probable tree
            as a tuple together with the corresponding sentence
    """
    # list of all possible trees generated from one sentence
    tree_variations = []

    if DEBUG: print "\ninformation for sent:", sent
    
    for tree in parser.parse(sent):
        if DEBUG: print "type of tree: ", type(tree)
        tree_variations.append(tree)

    if DEBUG: print "tree variations: ", tree_variations
    # returns the trees together with the original sentence as a tuple
    # the sentence is passed on, to be able to be accessed later on for the display
    return (sent, tree_variations)


def write_out_to_tex(trees, out_file, grammar):
    """
    all-in-one function to convert all trees from all sentences into a .tex-file
    combines static content (prolog, epilog, subsections, ...) with the syntax trees
    and used grammar

    input:  all trees from all sentences
            output file (given as an argument)
            the grammar used for parsing the trees
    output: TeX-file written to the output file (pref: *.tex)

    The TeX-file is compilable with the 'pdflatex' command
    """
    br = "\n" #linebreak

    ## casting the grammar to a string object (was CFG/PCFG object)
    #  it will later be inserted into the static content
    grammar = str(grammar)

    ## hard-coded text as static content for the .tex-file
    #  including:
    #    -the prolog (usedpackages, author, date, ...)
    #    -the grammar (static, since only one grammar is used per file)
    #    -the "epilog" a.k.a end-of-document declaration
    #  the variable content i.e. non-static content 

    if DEBUG: print "grammar for texfile:", grammar

    prolog = r"\documentclass[12pt]{article}" + br + \
    r"\usepackage{tikz}" + br + \
    r"\usepackage{tikz-qtree}" + br + \
    r"\title{Programiertechniken in der Computerlinguistik II: Assignment 6}" + br + \
    r"\author{Linus Manser (13-791-132), Roland Benz (97-923-163)}" + br + \
    r"\date{Abgabe: 2016/06/08}" + br + br + \
    r"\begin{document}" + br + br + \
    r"\maketitle" + br + \
    r"\section{Grammar}" + br + \
    r"\begin{verbatim}" + br + \
    grammar + br + \
    r"\end{verbatim}" + br + \
    r"\section{Syntax trees}" + br

    content = ""

    # non-static content starts here
    for tree_variations in trees:
        # extracting the data from the tuple
        (sent, tree_variations) = tree_variations
        sent = " ".join(sent)
        content += r"\subsection{'" + sent + r"'}" +\
            br + r"\begin{enumerate}" + br
        
        for tree in tree_variations:
            # http://www.nltk.org/howto/tree.html
            # compiling latex content which goes in-between (actual trees)
            content += r"\item\begin{center}" + "\n%s\n" % tree.pformat_latex_qtree() +\
                 br + r"\end{center}" + br
 
        content += r"\end{enumerate}" + br
        # non-static content ends here
            
    # marking the end of the latex-file
    epilog = r"\end{document}"
    # concatenating the whole content (static and non-static)
    whole_content = prolog + content + epilog
    # write the whole content to the given output file
    out_file.write(whole_content)

    if DEBUG: print "DONE: outfile written (see below)\n", whole_content


def main():
    """
    main function of the second and third part of PCL2 exercise 6

    call of the script via the command line. Example call:
        
        $ python aufgabe02.py -g grammar.txt -s sentences.txt -o out.tex

    required arguments:
     -g / --grammar: txt-file containing either a CFG or PCFG
    optional arguments:
     -s / --sents:   txt-file containing sentences (one per line)
     -o / --out:     tex-file where the trees should get written to

    Unless you set an output file, the parsed sentences are only displayed
    on the command line. Otherwise, the trees are written qtree-conform to
    the declared tex-file.

    Assuming you have LaTeX installed, you can create a pdf file with your 
    trees by typing the following command in your command line:

        $ pdflatex outfile.tex
    
    If no sentences(-s) given, you can write your sentences directly on the command
    line. To finish the input-mode, press 'ctrl+D'.

    """
    # setting up the arguments with argparse
    argparser = argparse.ArgumentParser()
    argparser.add_argument('-o','--out', type=argparse.FileType('w'),\
        metavar='FILE', help='output file')
    argparser.add_argument('-g','--grammar', type=argparse.FileType('r'),\
        metavar='FILE', help='grammar file')
    argparser.add_argument('-s','--sents', type=argparse.FileType('r'), \
        default=sys.stdin, metavar='FILE', help='sentence file')
    args = argparser.parse_args()
    
    # try to form a string from the data of the grammar file
    try:
        grammar_string = "".join(args.grammar)
    # if no grammar is given, exit the script
    # (assuming that nobody wants to write the same grammar over and over again)
    except TypeError:
        print "try:\t$ python aufgabe02.py -g [grammar.txt] -s [sentence.txt] -o "\
        "[outfile.tex]\n\t(where '-s' and '-o' are optional arguments)"
        exit()

    # parsing grammar from string
    try:
        grammar = nltk.CFG.fromstring(grammar_string)
        parser = nltk.ChartParser(grammar)
    except ValueError:
        # Part of Ex03
        # if the grammar contains probabilites, take the PCFG-method 
        # (and use the ViterbiParser)
        grammar = nltk.PCFG.fromstring(grammar_string)
        parser = nltk.ViterbiParser(grammar)
    
    if DEBUG: print "parser used:", type(parser)

    # collecting input form the given file (or: stdin by default)
    sent_file = args.sents
    # assigning the output file to a new variable
    out_file = args.out

    # list containing all possible trees for every sentence
    all_trees_from_all_sentences = []

    # parse all sentences inside the sentence file
    for sent in sent_file:
        if DEBUG: print "\nparsing sentence: ", sent, type(sent)
        sent = sent.split()
        try:
            # parsing the sentence with the given parser
            # and appending it to the bigger list (all_trees_from_all_sentences)
            all_trees_from_all_sentences.append(build_tree_variations(parser, sent))
            if DEBUG: print "parsing of sentence: ", sent, "DONE"
        except ValueError as e:
            print "\nERROR:", sent, "couldn't be parsed\nReason: %s" % e

    # printing the trees onto the command line with pretty print
    for tree_variations in all_trees_from_all_sentences:
        # extracting the data from the given tuple
        (sent, tree_variations) = tree_variations
        sent = " ".join(sent)
        print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
        print "sentence: '%s'" % sent
        v_enum = 1        
        for tree in tree_variations:
            print "version %i" % v_enum
            # http://www.nltk.org/howto/tree.html
            tree.pretty_print(unicodelines=True, nodedist=4)
            v_enum += 1

    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    # compiling the .tex file
    if out_file:
        write_out_to_tex(all_trees_from_all_sentences, out_file, grammar)
    else:
        print "(no output file selected. write '-o outfile.tex' as an argument when " \
            "running the script if you want to generate a .tex file)"


if __name__ == "__main__":
	main()