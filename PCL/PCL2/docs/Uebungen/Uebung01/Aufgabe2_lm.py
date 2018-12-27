#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PCL-I: Uebung 01 - Aufgabe 2, FS16

# Autoren:
# c(Student, Martikelnummer) -> 	{'Roland Benz'			: '97-923-163',
#									 'Linus Manser' : ''}

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Aufruf des Programms:
# Version 1:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Debug:  python -m pdb <fileName.py>


'''
2 Fortgeschrittene Klassen
Wir möchten in Python einen Paket-Manager für die Linux-Distribution Y schreiben. Die Distri-
bution Y ist aus dem Zusammenschluss zweier kleinerer Distributionen entstanden. Beide dieser
Distributionen hatten bis anhin einen eigenen Paket-Manager, die beide ein anderes Format für
Paket-Konfigurationsdateien verwendeten, weshalb die Paketdatenbanken für Y Linux ein wildes
Gemisch beider Formate sind.
Glücklicherweise werden beide Formate von der Python-Standardbibliothek unterstützt: die Hälfte
der Dateien ist im JSON-Format, die andere im .ini-Format.
Um die Architektur unseres Systems eleganter zu gestalten, möchten wir gerne auf die Konfigurati-
onsdateien formatunabhängig zugreifen können. Zu diesem Zweck sollst du eine Klasse ConfigReader
schreiben, die ein solches Interface implementiert.
Deine Klasse soll beim Aufruf einen Dateinamen erhalten und das Format erkennen. Um die bei-
den unterschiedlichen Formate zu bearbeiten, sollst du zwei Subklassen definieren: JsonReader und
IniReader. Diese Subklassen sollen Dateien des jeweiligen Formats einlesen und sich nach aussen
wie Dictionaries der Schlüssel-Wert-Paare in der eingelesenen Datei verhalten (definiere dazu die
Methode __getitem__). Die Oberklasse ConfigReader soll die Methode __new__ so definieren, dass
je nach Format der übergebenen Datei die richtige Subklasse zurückgegeben wird. Zum Einlesen der
Dateien kannst du die Standardmodule json und ConfigParser verwenden.
Im Übungsordner ist ein Skript zum Testen deines Moduls test_installer.py enthalten.

'''

print "\n########################################################################"
print 'Hi, From Program 2 : '
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

## import packages
#json parser
import json
#ini parser
import ConfigParser
#dict printer
from pprint import pprint
#os to split extension from file name
import os


## class definitions
#superclass ConfigReader
class ConfigReader(object):

    def __new__(cls, file_path):
        #recognize extension
        (filename, file_extension) = os.path.splitext(file_path)

        if file_extension == ".json":
            #invoke subclass JsonReader and create new object
            print " info from 1.1: you are reading a ", \
                file_extension," file"
            JR = JsonReader.__new__(cls,file_path)
            print " info from 1.1.1:", JR
            #JR.__init__(file_path) is done
            #implicitly by next statement return JR
            return JR

        elif file_extension == ".ini":
            #invoke subclass IniReader and create new object
            print " info from 1.2: you are reading a ", \
                file_extension, "file "
            IR = IniReader.__new__(cls,file_path)
            print " info from 1.2.1:", IR
            #IR.__init__(file_path) is done
            #implicitly by next statement return IR
            return IR
        else:
            print " info from 1.3", filename, file_extension

#subclass JsonReader
class JsonReader(ConfigReader):
    def __new__(cls, file_path):
        print " info from 2.1:", cls
        return object.__new__(JsonReader)

    def __init__(self,file_path):
        #read file, parse file, assign content to instance variable dict_parsed_file
        #use imported json parser package
        '''
        {
        "name":"VSolve Statistical Dependency Parser",
        "path":"/usr/program_files/vsolve/vsolve",
        "size":169435,
        "signed":"yes",
        "author":"Torin Kvalm"
        }
        '''
        #json parser
        #(https://docs.python.org/2/library/json.html)
        #(http://stackoverflow.com/questions/2835559/parsing-values-from-a-json-file-in-python)
        print " info from 2.2:", self
        with open(file_path) as data_file:
            print " info from 2.2.1:", data_file

            #define instance variable
            self.dict_parsed_file = json.load(data_file)
            print " info from 2.2.2:", self.dict_parsed_file


    def __getitem__(self, key):
        #overloading of [];
        #invocation of myconfig["author"] should call myconfig.__getitem__("author")
        #and return "Torin Kvalm"
        return self.dict_parsed_file[key]

#subclass IniReader
class IniReader(ConfigReader):
    def __new__(cls, file_path):
        print " info from 3.1:", cls
        return object.__new__(IniReader)

    def __init__(self,file_path):
        #read file, parse file, assign content to instance variable dict_parsed_file
        #use imported json parser package
        '''
        [package]
        name = Stree Treebank Viewer
        path = /usr/program_files/stree/stree.exe
        size = 322024
        signed = no
        author = James J. Callaghan
        '''
        #ini parser
        #(https://docs.python.org/2/library/configparser.html)
        #(http://stackoverflow.com/questions/8884188/how-to-read-and-write-ini-file-with-python)
        print " info from 3.2:", self
        ini_parser = ConfigParser.ConfigParser()
        print " info from 3.2.1:", ini_parser

        ini_parser.read(file_ini)

        #define instance variable
        self.dict_parsed_file = self.as_dict(ini_parser)
        print " info from 3.2.2:", self.dict_parsed_file

    def __getitem__(self, keys):
        #overloading of [];
        #invocation of myconfig["author"] should call myconfig.__getitem__("author")
        #and return "Torin Kvalm"
        #(http://stackoverflow.com/questions/17478284/
        # python-is-there-a-way-to-implement-getitem-for-multidimension-array)
        
        ## Code so geändert, dass er nur einen key braucht -> test_install sollte somit funktionieren 
        #package_key, key = keys
        #return self.dict_parsed_file[package_key][key]
        print keys
        return self.dict_parsed_file["package"][keys]


    ## method to write into dictionary self.dict_parsed_file
    #(http://stackoverflow.com/questions/3220670/
    # read-all-the-contents-in-ini-file-into-dictionary-with-python)
    def as_dict(self,ini_parser):
        d = dict(ini_parser._sections)
        for k in d:
            d[k] = dict(ini_parser._defaults, **d[k])
            d[k].pop('__name__', None)
        return d

## data files
#json file
#file_json = "/media/benzro/OS/Users/benzro/Desktop/Studium Uni/" \
#            "2)ZweitesSemester/27)PCL-2/Uebungen/Uebung01/test.json"
file_json = "/users/linusmanser/cl/pcl2/exercises/uebung01/test.json"
#ini file
#file_ini = "/media/benzro/OS/Users/benzro/Desktop/Studium Uni/" \
#           "2)ZweitesSemester/27)PCL-2/Uebungen/Uebung01/test.ini"
file_ini = "/users/linusmanser/cl/pcl2/exercises/uebung01/test.ini"

## read file by calling superclass ConfigReader
#ConfigReader reads the suffix and calls either
#JsonReader or IniReader class
myconfig1 = ConfigReader(file_json)
print " info from 4.1:", myconfig1
print "info~~~~~~~~~~~"
myconfig2 = ConfigReader(file_ini)
print " info from 4.2:", myconfig2


## read data from dictionaries myconfig1, myconfig2
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
the_author1 = myconfig1["author"]
print " author: ", the_author1
#the_author2 = myconfig2["package", "author"]
the_author2 = myconfig2["author"]
print " author: ", the_author2

## print whole dictionary myconfig
#standard way
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
for key, value in myconfig1.dict_parsed_file.items():
    print key,":",value
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
for key, value in myconfig2.dict_parsed_file.items():
    for key2, value2 in myconfig2.dict_parsed_file[key].items():
        print key2,":",value2
#with pprint package
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
pprint(myconfig1.dict_parsed_file)
pprint(myconfig2.dict_parsed_file)

print "\n########################################################################"
print "Bye Bye und bis bald! :-)"
print "########################################################################"