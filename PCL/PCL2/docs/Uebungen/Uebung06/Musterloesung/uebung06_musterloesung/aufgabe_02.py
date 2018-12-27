#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# PCL2-Ü6-Aufgabe 2
# Musterlösung von Raphael Balimann (raphael.balimann@uzh.ch) - HS 2015
#

import nltk
import sys

def main():
    """ Showcasing the functionality with the sentences given"""

    # How can this be made more robust? Hint: getopt
    grammar_path = sys.argv[1]
    sentence_path = sys.argv[2]
    output_path = sys.argv[3]

    forest = parse_file(grammar_path, sentence_path)
    # for item in forest:
    #     for i in item:
    #         print pretty_print_qtree(i)

    # Achtung: forest ist ein Iterator, wird er durchlaufen
    # beim drucken, muss er erst auf Null zurückgesetzt werden
    generate_qtree_document(forest, output_path)

    return

def create_grammar(raw_grammar):
    """ A wrapper that returns a CFG in CNF"""

    return nltk.CFG.fromstring(raw_grammar)

def parse_sentence(grammar, sentence):
    """ A wrapper that accepts:
        - a CFG in CNF
        - a sentence as a list of token
        Returns a tree object
    """
    cfg_grammar = create_grammar(grammar)
    current_parser = nltk.ChartParser(cfg_grammar)
    tree = current_parser.parse(sentence)

    return tree

def parse_file(grammar_path, sentence_path):
    """ A wrapper that accepts two file paths:
        - a CFG as plain text
        - a plain text file with sentences
        Returns a list of tree objects
    """
    with open(grammar_path) as grammar_file:
        raw_grammar = []
        for line in grammar_file:
            raw_grammar.append(line)

    with open(sentence_path) as sentence_file:
        raw_sentences = []
        for line in sentence_file:
            raw_sentences.append(line)

    print "1.1:\n", raw_grammar #list of strings (production is string)
    print "1.2:\n", raw_sentences #list of strings (sent is string)

    sentences = [nltk.word_tokenize(raw_sent) for raw_sent in raw_sentences]

    print "1.3:\n", sentences #list of list of strings

    tree_list = []
    for sentence in sentences:
        tree_list.append(parse_sentence(raw_grammar, sentence))

    print "1.4:\n", tree_list #generator object: tree

    return tree_list


def pretty_print_qtree(tree):
    """ A function to convert tree objects
        into the notation used by the LaTeX qtree package
        Accepts a single tree item,
        returns a string that can be used further
    """
    return tree.pformat_latex_qtree()

def pretty_print_stree(tree):
    """ A function to convert tree objects
        into a notation that can be displayed on the standard output
        Accepts a single tree item,
        prints directly to the standard output
    """
    tree.pretty_print()

    return

def generate_qtree_document(trees, filepath):
    """ A function to create a full (Xe)LaTeX document containing trees
        Accepts a list of tree objects
        Writes a full source file to the the specified path
    """

    # frontmatter for a full tex file, should be usable with many
    # different (La)TeX varieties
    frontmatter = r"""
\documentclass[12pt]{article}
\usepackage{tikz}
\usepackage{tikz-qtree}

\title{Programmiertechniken in der Computerlinguistik II: Assignment 6}
\author{Raphael Balimann - 11-739-679}
\date{Abgabe: 2016/06/02}

\begin{document}

\maketitle
"""

    # centering
    start_center = r"""\begin{center}
"""
    end_center = r'\end{center}'

    # endmatter for document
    endmatter = r"""
\end{document}
    """

    with open(filepath, 'w') as output:
        output.write(frontmatter)
        for forest in trees:
            for tree in forest:
                print "Writing tree to file:"
                pretty_print_stree(tree) #to console
                output.write(start_center)
                output.write(pretty_print_qtree(tree)) #tex file
                output.write(end_center)
        output.write(endmatter)

    return

if __name__ == '__main__':
    main()
