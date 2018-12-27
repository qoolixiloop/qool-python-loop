#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PCL-I: Uebung 02 - Aufgabe 4, FS16

# Autoren:
# c(Student, Martikelnummer) -> 	{'Roland Benz'			: '97-923-163',
#									 'Linus Manser' 		: '13-791-132'}
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Aufruf des Programms:
# Version 1: python ex04.py (user input: output_pcl_ex04)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from nltk.corpus import brown
from lxml import etree
import codecs

## time module for fun
import time


def build_xml_file():
    """
    NO INPUT
    OUTPUT: Builds the XML-file with information from the brown corpus
    """
    # starting message
    print "building XML-file ..."

    # start time-measurement
    start = time.time()

    # number of texts (500) and categories (15)
    text_number = len(brown.fileids())
    cat_number = len(brown.categories())

    # creating a new root element called 'browncorpus'
    # with attributes textcount and categorycount
    root = etree.Element("browncorpus", textcount=str(text_number),
                         categorycount=str(cat_number))


    # for every fileID (individual texts) in the browncorpus...
    iter=1
    cnt=1
    for id in brown.fileids():

        # adding the SubElement 'textfile' to 'browncorpus'
        textfile = etree.SubElement(root, "textfile")

        # define attributes for each textfile element
        textfile.attrib["textID"] = str(id)
        list_category=brown.categories(fileids=[id]) #returns one element list
        textfile.attrib["category"] = str(list_category[0])

        # add SubElement 'wordcount' to 'textfile'
        wordcount = etree.SubElement(textfile, "wordcount")
        list_words=brown.words(fileids=[id])
        wordcount.text = str(len(list_words))

        # add SubElement 'lastsentence' to 'textfile'
        last_sentence = etree.SubElement(textfile, "lastsentence")
        str_last_sentence=brown.sents(fileids=[id])[-1]
        last_sentence.text = " ".join(str_last_sentence)

        # just for fun
        if iter%50==0:
            percent=text_number/50*cnt
            print percent,"% completed"
            cnt=cnt+1
        iter=iter+1

    end = time.time()
    # time difference (just for fun)
    elapsed_time = end - start

    # completion message
    print "... completed after %.3f seconds" % elapsed_time

    # returns root element (whole xml-document)
    return etree.tostring(root, xml_declaration=True,
                          encoding="utf-8", pretty_print=True)


def write_out_file(filename):
    """
    INPUT: filename
    OUTPUT: writes out the built xml-file to the file 'filename.xml'
    """
    # create or overwrite file this defined filename
    with codecs.open(filename, "w", "utf-8") as outfile:
        str_etree = build_xml_file()
        outfile.write(str_etree)

    # completion message
    print "wrote out to XML-file '%s'" % filename



if __name__ == "__main__":

    # file in which output is written (stored in same folder like ex04.py)
    # e.g. output_pcl_ex04
    filename = raw_input("please enter a filename for your XML-file, "
                         "in which the output is written: ") + ".xml"

    # opens file object (filename)
    # calls function build_xml_file() which:
    #   iterates through all files in brown corpus
    #   extracts information (id, category, nr of words, last sentence)
    #   builds xlm tree
    # writes tree to file
    write_out_file(filename)

