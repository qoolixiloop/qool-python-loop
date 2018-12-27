#!/usr/bin/env python
# -*- coding: utf-8 -*-
#PCL II, Uebung 1, FS2016
#Aufgabe 3
#Autoren: Janis Goldzycher, Jasmin Walser

#Es gibt ein Problem mit komplexen Regexausdrücken. 
#Sobald nicht nur ein Wort, sondern ein Ausdruck wie '(mogeln|arbeiten)'
#als Pattern angegeben wird, erscheint die Fehlermeldung: 
#'bash: Syntaxfehler beim unerwarteten Wort »(«'
#Es scheint also irgendein Problem zu bestehen, bei dem das Argument 
#'s/pattern/replacement/g', wenn Klammern oder Ähnliches darin vorkommen, 
#nicht als Argument an Python weitergegeben wird, sondern von Bash 
#selber ausgelesen wird. Wie man das Problem löst, haben wir nicht 
#herausgefunden.


import re
import argparse
import sys
import codecs


################################
#####argumenthandling###########
################################


parser = argparse.ArgumentParser()
parser.add_argument('string', type=str, help="s/pattern/replace/g string")
	
parser.add_argument('-e','--encoding', default= 'utf-8', help="encoding of text")
parser.add_argument('-o','--out', type=argparse.FileType('w'), default=sys.stdout, metavar='FILE', help='out file')
parser.add_argument('-f','--file', type=argparse.FileType('r'), default=sys.stdin, metavar='FILE', help='in file')

args = parser.parse_args()


################################
#####defining the functions#####
################################


def cmd_input():
	'''
	userinput through terminal
	'''
	print 'Please write your inputtext. Press first enter and then ctrl + D to proceed.'
	input_cmd = stdin.read()
	try:
		input_cmd.decode(args.encoding)
	except UnicodeDecodeError:
		print 'Your Input caused a UnicodeDecodeError. Please try again'
		sys.exit()
	text = str(input_cmd)
	return text

def file_input():
	text = ''.join(args.file)
	try:
		text.decode(args.encoding)
	except UnicodeDecodeError:
		print 'Your Input caused a UnicodeDecodeError. Please try again'
		sys.exit()
	return text

def patternreplaceparser(cmd_argument, text_input):
	'''
	Parse the cmd-input-pattern, replace pattern in text
	'''
	split_str = cmd_argument.split('/')
	sed_pattern = split_str[1]
	sed_pattern2 = sed_pattern.strip(')')
	sed_pattern3 = sed_pattern.strip('(')
	sed_replace = split_str[2]
	new_text = re.sub(sed_pattern3, sed_replace, text_input)
	return new_text
	
def file_output(new_text):
	'''
	write the result into an outputfile
	'''
	outfile = args.out
	outfile.write(new_text)
	outfile.close()

def cmd_output(new_text):
	'''
	print result to the commandline
	'''
	print new_text


################################
#####Execution##################
################################


def main():
	#checking the encoding
	if args.encoding is not None:
		try:
			args.string.decode(args.encoding)
		except UnicodeDecodeError:
			print 'Your Input caused a UnicodeDecodeError. Please try again'
			sys.exit()
	
	#get input
	if args.file is not None:
		#print 'Please write your inputtext. Press first enter and then ctrl + D to proceed.'
		text_input = file_input()
	else:
		print 'Please write your inputtext. Press first enter and then ctrl + D to proceed.'
		text_input = cmd_input()
	
	#replace pattern
	altered_text = patternreplaceparser(args.string, text_input)
	
	#generate output
	if args.out is not None:
		file_output(altered_text)
	else:
		cmd_output(altered_text)

if __name__ == '__main__':
	main()
