#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# PCL2-Ü3-Aufgabe 1
# Musterlösung von Raphael Balimann (raphael.balimann@uzh.ch) - HS 2015
#
import nltk
from nltk.corpus.reader.plaintext import PlaintextCorpusReader

# Main function to showcase functionality
# One corpus for ham, one for spam, no other distinctions
# Files are expected to be merged into one respective directory,
# other layouts are easily doable with simple loops and function calls
def main():

    ham_dir =  'ham/'
    ham_corpus = buildCorpus(ham_dir)

    spam_dir = 'spam/'
    spam_corpus = buildCorpus(spam_dir)

    if (utf8Checker(ham_corpus) & utf8Checker(spam_corpus)):
        return
    else:
        print """Something's wrong with the file encodings.
                Please refer to the comment in aufgabe_01.py to
                make sure that all files are converted to UTF-8."""
        return

# Wrapper function to build the corpus given the directory
def buildCorpus(corpus_directory):

    corpus = PlaintextCorpusReader(corpus_directory,'.*')
    return corpus

# A quick check if everything is properly encoded as UTF-8
def utf8Checker(corpus):
    for i in corpus.fileids():
        if corpus.encoding(i) != "utf8":
            return False
    return True

# Standard boilerplate to call the main() function to begin the program.
if __name__ == '__main__':
    main()

"""
If there are problems with encodings (using the data from the source webpage),
the following snippet proved helpful to convert all files to the same encoding.
Needs to be run in the directory where the files are stored.

find . -name "*.txt" -exec sh -c "iconv -f ISO-8859-1 -t UTF-8 {} > {}.utf8"  \; -exec mv "{}".utf8 "{}" \;

Courtesy of 'UTF_or_Death' on http://stackoverflow.com/a/24836200

"""
