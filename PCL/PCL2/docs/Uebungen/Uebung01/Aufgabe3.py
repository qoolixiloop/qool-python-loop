#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PCL-II: Uebung 01 - Aufgabe 3, FS16

# Autoren:
# c(Student, Martikelnummer) -> 	{'Roland Benz'	: '97-923-163',
#									 'Linus Manser' : '13-791-132'}

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Aufruf des Programms:
#
# #Test1: kein Text
# python Aufgabe3.py s/Regex/Python/g
# (Enter, dann 3 Mal Ctrl-D)
#
# #Test2: kein Regex
# python Aufgabe3.py
# Regex macht spass (Enter, dann 3 Mal Ctrl-D)
# couldnt replace any text!
#
# #Test3: echo
# echo "Regex macht spass" | python Aufgabe3.py s/Regex/Python/g
# Python macht spass
#
# #Test4: codecs.getreader ()(sys.stdin)
# python Aufgabe3.py s/Regex/Python/g
# Regex macht spass (Enter, dann 3 Mal Ctrl-D)
# Python macht spass
#
# #Test5: output file, option -o
# python Aufgabe3.py s/Regex/Python/g -o out.txt
# Regex macht spass (Enter, dann 3 Mal Ctrl-D)
# wrote text to file 'out.txt' ...
# Python macht spass
#
# #Test6: encoding, option -e
# python Aufgabe3.py s/Regex/Python/g -o out.txt -e latin1
# Regex macht spöss (Enter, dann 3 Mal Ctrl-D)
# wrote text to file 'out.txt' ...
# Python macht sp�ss
# $file -i out.txt (Enter)
# charset=iso-8859-1
#
# #Test7: input file, option -f
# python Aufgabe3.py s/Regex/Python/g -o out.txt -e latin1 -f test_latin1_.txt
# Das ist ein Beispieltext
# þorsteinn heit maðr. Hann var Egilsson.
# TEST ðéóæÆ.
# Je suis désolé.
# üÜäÄöÖÉéàÀèÈ
# ÿ#±Ç[]
# $file -i out.txt (Enter)
# charset=iso-8859-1
#
# Test8: None Ascii characters in find/replace string
# Aufgabe3.py s/Regöx/Pythön/g
# Regöx macht spass
# ASCII doesn't support characters in your input
#
# Test9: None Ascii characters in find/replace string, latin1 encoding
# Aufgabe3.py s/Regöx/Pythön/g -e latin1
# Regöx macht spass (Enter, dann 3 Mal Ctrl-D)
# Pythön macht spass
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ## Python Code um Encoding einer Textdatei zu ändern.
# import codecs
# in_filename = "/media/benzro/OS/Users/benzro/Desktop/Studium Uni/" \
#                 "2)ZweitesSemester/27)PCL-2/Uebungen/Uebung01/test_latin1.txt"
# out_filename="/media/benzro/OS/Users/benzro/Desktop/Studium Uni/" \
#                 "2)ZweitesSemester/27)PCL-2/Uebungen/Uebung01/test_latin1_.txt"
# infile = codecs.open(in_filename, 'r', encoding='utf-8')
# outfile = codecs.open(out_filename, 'w', encoding='latin1')
# for line in infile:
#      outfile.write(line)
# infile.close()
# outfile.close()
#
# file -i test_latin1_.txt
# charset=iso-8859-1
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

'''
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
'''

## debug
# set to 1 for debugging purposes
DEBUG_FLAG=0

## import packages
import sys
import regex as re
import codecs

## function definitions
# extract find/replace pattern
def get_sed_query(list):
    """
    Functionality:
        extract find/replace pattern
    Input:  list
            searches for the sed-query in the form of s/pattern/replacement/g

    Exceptions: if nothing is given -> no query defined
                if first element in the input_list isnt the query -> incorrect query defined

    Output: extracts the pattern and replacement and returns it as a tuple (pattern, replacement)
    """
    if DEBUG_FLAG: print " info from 1.0: get_sed_query()"


    #find/replace pattern to search for
    pattern = "s/(.*?)/(.*?)/g"
    if DEBUG_FLAG: print " info from 1.1:", pattern

    #search for find/replace argument parameter in input parameter list
    # extraction of pattern and replacement from the query
    for i in list:

        try:
            #check each list element if it
            # matches find/replace input argument
            match = re.search(pattern,i)
            pattern = match.group(1)
            replacement = match.group(2)

            #output: Tuple
            if DEBUG_FLAG: print " info from 1.2:", pattern, replacement
            return (pattern, replacement)
        
    	# Ignores AttributeError -> if the first element in the command line isnt the query, the search continues
        except AttributeError:
            None

# extract encoding string
def get_encoding(list):
    """
    Functionality:
        extract encoding string
    Input: takes in a list and looks for "-e" or "--encoding" to set encoding

    Output: returns the given encoding (first part after the command) as string ("utf-8", "latin-1",...)
    """
    if DEBUG_FLAG: print " info from 2.0: get_encoding()"

    cmd = ["-e", "--encoding"]

    # read out required encoding
    # if optional command exists, do the following.
    for i in cmd:
        if i in list:

            # Take the next element in the input_list after -e or --encoding
            encoding = list[list.index(i)+1]
            if DEBUG_FLAG: print " info from 2.1:", encoding

            return encoding

    # default encoding is utf-8 (if no encoding defined)
    encoding = "ASCII"
    if DEBUG_FLAG: print " info from 2.2:", encoding
    return encoding
    

# extract text from file or sys.stdin
def get_text(list):
    """
    Functionality:
        extract text from file or sys.stdin
    Input: list
            checks whether a file or just the given text in the command-line is processed
            if a file is declared, it opens it with the given encoding (default=utf-8)

    Output: returns the text inside of the file or the text behind the option-commands
    """
    if DEBUG_FLAG: print " info from 3.0: get_text()"

    text = []
    cmd = ["-f","--file"]
    ## Read input file
    # if optional command exists, open the given document (first element after -f/--file)
    for i in cmd:
        if i in list:

            #input_filename directly after option -f
            input_filename = list[list.index(i)+1]
            if DEBUG_FLAG: print " info from 3.1:", input_filename

            #open input file for reading
            encoding=get_encoding(list)
            with codecs.open(input_filename, "r", encoding) as input_file:
                if DEBUG_FLAG: print " info from 3.2:", input_file, encoding

                try:
                    #list, one line one list element
                    for line in input_file:
                        text.append(line)
                    if DEBUG_FLAG: print " info from 3.3:", text

                    #convert to string
                    # join the list into one string -> whole document in one string
                    text = "".join(text)
                    if DEBUG_FLAG: print " info from 3.4:", text
                    return text

                except UnicodeDecodeError:
                    print "the given encoding doesn't support characters in this file. please change the encoding..."
                    exit();

    ## Wait for user input and read text from console
    # if no -f or --file flag given, get the standard-in as input            
    input_text = codecs.getreader(get_encoding(list))(sys.stdin)
    try:
        #list, one line one list element
        for i in input_text:
            text.append(i)
        if DEBUG_FLAG: print " info from 3.5:", text

        #convert to string
        text = "".join(text)
        if DEBUG_FLAG: print " info from 3.6:", text
        return text

    except UnicodeDecodeError:
        print "%s doesn't support characters in your input" % (get_encoding(list))
        exit();


# apply find/replace pattern on text
def apply_sed_query(list, text):
    """
    Functionality:
        apply find/replace pattern on text
    Input: list, unprocessed text
    Output: processed text (replaced text)
    """
    if DEBUG_FLAG: print " info from 4.0: apply_sed_query()"

    try:
        #get find/replace command line argument
        pattern, replacement = get_sed_query(list)
        if DEBUG_FLAG: print " info from 4.1:", pattern, replacement

        #change to unicode
        pattern = pattern.decode(get_encoding(list))
        replacement = replacement.decode(get_encoding(list))
        if DEBUG_FLAG: print " info from 4.2:", pattern, replacement

        #find/replace
        out_text = re.sub(pattern,replacement,text)
        #print "replaced '%s' with '%s'\n~~~~~~~~~~~~~~~~~~~~~~~~" % (pattern, replacement)
        if DEBUG_FLAG: print " info from 4.3:", out_text

        return out_text

    except TypeError:
        print "couldnt replace any text!"

    except UnicodeDecodeError:
        print "%s doesn't support characters in your input" % (get_encoding(list))


# write adapted text into file or console
def write_out(list, out_text):
    """
    Functionality:
        write adapted text into file or console
    Input: list, processed text
    Output: if a file is declared, write processed text to file
            else it shows the text in the bash
    """
    if DEBUG_FLAG: print " info from 5.0: write_out()"

    cmd = ["-o","--out"]
    # if optional command (cmd) exists, do the following:
    for i in cmd:
        if i in list:

            #output_filename directly after option -o
            output_filename = list[list.index(i)+1]
            if DEBUG_FLAG: print " info from 5.1:", output_filename

            #write text into output_file with requested encoding
            encoding_ = get_encoding(list)
            output_file=codecs.open(output_filename, "w", encoding=encoding_)
            output_file.write(out_text)
            if DEBUG_FLAG: print " info from 5.2:", output_file, encoding_, out_text

            print "wrote text to file '%s' ..." % output_filename

            output_file.close
            exit();

    # default behaviour: print output text directly into the bash
    if DEBUG_FLAG: print " info from 5.3:", out_text
    print out_text


## main procedure
if __name__ == "__main__":

    #print "~~~~~~~~~~~~~~~~~~~Start: Programm Aufgabe 3~~~~~~~~~~~~~~~~~~~~~~~~"
    if DEBUG_FLAG: print " info from 0.0: main()"

    #get argument parameter list
    command_list = sys.argv[1:]
    if DEBUG_FLAG: print " info from 0.1: ", command_list

    #get (sys.stdin) standard input text of input file or user input
    in_text=get_text(command_list)
    if DEBUG_FLAG: print " info from 0.2: ", in_text

    #apply find/replace on input text
    out_text = apply_sed_query(command_list, in_text)
    if DEBUG_FLAG: print " info from 0.3: ", out_text

    #write out adapted text after find/replace
    write_out(command_list, out_text)

    #print "~~~~~~~~~~~~~~~~~~~Ende: Programm Aufgabe 3~~~~~~~~~~~~~~~~~~~~~~~~"
