#!/usr/bin/env python
# -*- coding: utf-8 -*-
#PCL II, Übung 1, FS16
#Aufgabe 1
#Autor: Linus Manser, Roland Benz
#Matrikel-Nr.: 13-791-132, 97-923-163


##Aufgabe 3
#Das UNIX-Programm sed ist ein beliebtes Tool, um Text in einer Pipeline zu editieren. Die am häufigsten
#genutzte Funktion dieses Programms ist der Befehl s/pattern/replace/g, um Ersetzungen mit regulären Ausdrücken
#durchzuführen. Du sollt nun ein Python-Programm schreiben, dass einen solchen Filter implementiert.
#Dein Programm soll von der Kommandozeile einen Befehl in der Form s/pattern/replacement/g einlesen.
#Den Text soll es standardmässig von der Standardeingabe lesen und den bearbeiteten Text auf der Standardausgabe
#wieder ausgeben.

#Das Programm sollte folgende Kommandozeilenoptionen unterstützen:
#a) -e|--encoding: Das Encoding der eingelesenen Datei. Dein Programm sollte mindestens die
#Encodings ascii, latin-1 und utf-8 unterstützen.
#b) -f|--file: Datei, aus der der Rohtext gelesen werden soll, wenn er nicht von der Standard-
#eingabe kommt.
#c) -o|--out: Datei, in die der bearbeitete Text geschrieben werden soll, wenn er nicht auf der Kommandozeile ausgegeben werden soll.

print "Programm Aufgabe 3:\n~~~~~~~~~~~~~~~~~~~~~~~~"

import sys
import regex as re
import codecs


def get_encoding(list):
    """
    Input: takes in a list and looks for "-e" or "--encoding" to set encoding

    Output: returns the given encoding (first part after the command) as string ("utf-8", "latin-1",...)
    """
    cmd = ["-e", "--encoding"]
    #if optional command exists, do the following.
    for i in cmd:
        if i in list:
        	#Take the next element in the input_list after -e or --encoding
            list_index=list.index(i)+1
            print "info get_encoding.1 list_index: ", list_index
            encoding = list[list_index]
            return encoding
    #default encoding is utf-8 (if no encoding defined)
    encoding = "utf-8"
    return encoding

def get_sed_query(list):
    """
    Input:  list
            searches for the sed-query in the form of s/pattern/replacement/g

    Exceptions: if nothing is given -> no query defined
                if first element in the input_list isnt the query -> incorrect query defined

    Output: extracts the pattern and replacement and returns it as a tuple (pattern, replacement)
    """
    
    pattern = "s/(.*?)/(.*?)/g"
        
    #check if there is any input
    try:
        query = list[0]
        print "info get_sed_query.1 query: ", query
        
    except IndexError:
        print "No query defined\n~~~~~~~~~~~~~~~~~~~~~~~~"
        exit();
        
    #extraction of pattern and replacement from the query 
    try:
        match = re.search(pattern,query)
        pattern = match.group(1)
        replacement = match.group(2)
        #output: Tuple
        return (pattern, replacement)
    #if the first element of the input_list doesn't follow the query-form, raise exception and exit programm
    except AttributeError:
        print "incorrect query defined -> s/pattern/replacement/g"
        exit();


def get_text(list):
    """
    Input: list
            checks whether a file or just the given text in the command-line is processed
            if a file is declared, it opens it with the given encoding (default=utf-8)

    Output: returns the text inside of the file or the text behind the option-commands
    """
    text = []
    cmd = ["-f","--file"]
    #if optional command exists, open the given document (first element after -f/--file)
    for i in cmd:
        if i in list:
            input_filename = list[list.index(i)+1]
            with codecs.open(input_filename, "r", encoding=get_encoding(list)) as input_file:
                try:
                    for line in input_file:
                        text.append(line)
                    #join the list into one string -> whole document in one string 
                    text = "".join(text)
                    return text.encode(get_encoding(list))
                except UnicodeDecodeError:
                    print "the given encoding doesn't support characters in this file. please change the encoding..."
                    exit();
                    
    #default behaviour: take the text that isnt part of a optional command
    cmd = ["-o", "--output","-e", "--encoding"]
    index_list = []
    for i in cmd:
        if i in list:
            index_list.append(list.index(i))
    try:
        max_val_in_list = max(index_list)
        text = " ".join(list[max_val_in_list+2:])
        return text
    # if he doesnt find any optional commands (-o, -e etc.), take everything after the sed-query as text
    except ValueError:
        text = " ".join(list[1:])
        return text


def apply_sed_filter(list, text):
    """
    Input: list, unprocessed text
    Output: processed text (replaced text)
    """
    try:
        pattern, replacement = get_sed_query(list)
        print "replacing '%s' with '%s' ...\n~~~~~~~~~~~~~~~~~~~~~~~~" % (pattern, replacement)
        out_text = re.sub(pattern,replacement,text)
        return out_text
    except TypeError:
        print "couldnt replace any text!"
        

def write_out(list, out_text):
    """
    Input: list, processed text
    Output: if a file is declared, write processed text to file
            else it shows the text in the bash
    """
    cmd = ["-o","--out"]
    #if optional command (cmd) exists, do the following.
    for i in cmd:
        if i in list:
            output_filename = list[list.index(i)+1]
            #FIXME: encoding stays UTF-8 regardless of encoding...!?
            #encoding="iso-8859-1"
            with codecs.open(output_filename, mode="w", encoding="ascii") as output_file:
                print "info write_out.1 out_text: ", out_text
                output_file.write(out_text)

                print "wrote text to file '%s' ..." % output_filename
                exit();
    #default behaviour: print output text directly into the bash
    print "output:\n\n", out_text, "\n~~~~~~~~~~~~~~~~~~~~~~~~"

if __name__ == "__main__":
    input_list = sys.argv[1:]
    print "info main.1 input_list: ", input_list
    encoding=get_encoding(input_list)
    print "info main.2 encoding: ", encoding
    get_sed_query(input_list)
    out_text=apply_sed_filter(input_list, get_text(input_list))
    print "info main.3 out_text: ", input_list
    write_out(input_list, out_text)

# Zeit gebraucht: ca 6 Stunden