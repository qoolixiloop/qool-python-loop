#!/usr/bin/env python
# -*- coding: utf-8 -*-
#PCL II Uebung 02
#Aufgabe 3
#Musterloesung
#AutorIn: Irene

from lxml import etree
from nltk.corpus import brown

print "Putting together XML Tree..."
#setting root with its attributes
root = etree.Element('browncorpus')
count_cat = len(brown.categories())
count_files = len(brown.fileids())
root.set("categories",str(count_cat))
root.set("files",str(count_files))
for id in brown.fileids():
	text = etree.SubElement(root,'file')
	text.set("id",id)
	text.set("cat",brown.categories(fileids=id)[0])
	w_count = len(brown.words(fileids=id))
	words = etree.SubElement(text,'words')
	words.text = str(w_count)
	sent = brown.sents(fileids=id)[-1]
	lastsent = etree.SubElement(text, 'last_sentence')
	lastsent.text = ' '.join(sent)

print "Creating XML file..."
#putting the XML "tree" together and write the actual XML file
tree = etree.ElementTree(root)
tree.write('thebrowncorpus.xml', xml_declaration=True,pretty_print=True, encoding='utf-8')
print "XML file thebrowncorpus.xml ready."