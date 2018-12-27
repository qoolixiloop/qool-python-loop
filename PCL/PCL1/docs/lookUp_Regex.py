#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re  ## necessary for regular expressions
import random 

'''
Klassen/Methoden/Funktionen: Signatur, Attribute, Instanzvariablen
******************************************************************
import inspect
inspect.getmembers(object)
dir(object)
repr(object.__doc__)
vars(object)
object.__dict__
'''

'''
Module Contents
***************
re.compile(pattern, flags=0)¶
re.search(pattern, string, flags=0)¶
re.match(pattern, string, flags=0)¶
re.split(pattern, string, maxsplit=0, flags=0)¶
re.findall(pattern, string, flags=0)¶
re.finditer(pattern, string, flags=0)¶
re.sub(pattern, repl, string, count=0, flags=0)¶
re.subn(pattern, repl, string, count=0, flags=0)¶
re.escape(string)¶
re.purge()
##flags
re.DEBUG¶
re.I
re.IGNORECASE¶
re.L
re.LOCALE
re.M
re.MULTILINE
re.S
re.DOTALL
re.U
re.UNICODE
re.X
re.VERBOSE¶

Regular Expression Objects¶
re.RegexObject
***************************
search(string[, pos[, endpos]])¶
match(string[, pos[, endpos]])¶
split(string, maxsplit=0)¶
findall(string[, pos[, endpos]])¶
finditer(string[, pos[, endpos]])¶
sub(repl, string, count=0)¶
subn(repl, string, count=0)¶
flags¶
groups¶
groupindex¶
pattern¶
'''
'''
Python offers two different primitive operations based on regular 
expressions: re.match() checks for a match only at the beginning of
the string, while re.search() checks for a match anywhere in the 
string (this is what Perl does by default).
'''
pattern = re.compile("d")
var=pattern.search("dog")     # Match at index 0
print var
#<_sre.SRE_Match object at ...>
var=pattern.search("dog", 1)  # No match; search doesn't include the "d"
print var

pattern = re.compile("o")
var=pattern.match("dog")      # No match as "o" is not at the start of "dog".
print var
var=pattern.match("dog", 1)   # Match as "o" is the 2nd character of "dog".
print var
#<_sre.SRE_Match object at ...>

'''

Match Objects
re.MatchObject
**************
Match objects always have a boolean value of True. Since match() 
and search() return None when there is no match, you can test 
whether there was a match with a simple if statement:
'''
#match = re.search(pattern, string)
#if match:
#	process(match)
'''
Match objects support the following methods and attributes:

expand(template)

	Return the string obtained by doing backslash substitution on 
	the template string template, as done by the sub() method. 
	Escapes such as \n are converted to the appropriate characters, 
	and numeric backreferences (\1, \2) and named backreferences 
	(\g<1>, \g<name>) are replaced by the contents of the 
	corresponding group.

group([group1, ...])

	Returns one or more subgroups of the match. If there is a single 
	argument, the result is a single string; if there are multiple 
	arguments, the result is a tuple with one item per argument. 
	Without arguments, group1 defaults to zero (the whole match is 
	returned). If a groupN argument is zero, the corresponding return 
	value is the entire matching string; if it is in the inclusive 
	range [1..99], it is the string matching the corresponding 
	parenthesized group. If a group number is negative or larger 
	than the number of groups defined in the pattern, an IndexError 
	exception is raised. If a group is contained in a part of the 
	pattern that did not match, the corresponding result is None. 
	If a group is contained in a part of the pattern that matched 
	multiple times, the last match is returned.
'''
m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
var=m.group(0)       # The entire match
print var
#'Isaac Newton'
var=m.group(1)       # The first parenthesized subgroup.
print var
#'Isaac'
var=m.group(2)       # The second parenthesized subgroup.
print var
#'Newton'
var=m.group(1, 2)    # Multiple arguments give us a tuple.
print var
#('Isaac', 'Newton')
'''
	If the regular expression uses the (?P<name>...) syntax, 
	the groupN arguments may also be strings identifying groups 
	by their group name. If a string argument is not used as a 
	group name in the pattern, an IndexError exception is raised.

	A moderately complicated example:
'''
m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Malcolm Reynolds")
var=m.group('first_name')
print var
#'Malcolm'
var=m.group('last_name')
print var
#'Reynolds'
'''
	Named groups can also be referred to by their index:
'''
var=m.group(1)
print var
#'Malcolm'
var=m.group(2)
print var
#'Reynolds'
'''
	If a group matches multiple times, only the last match is accessible:
'''
m = re.match(r"(..)+", "a1b2c3")  # Matches 3 times.
var=m.group(1)                    # Returns only the last match.
print var
#'c3'

m = re.match(r"(..)", "a1b2c3")  
var=m.group(0)                   
print var
#'a1'
'''
groups([default])

	Return a tuple containing all the subgroups of the match, from 1 
	up to however many groups are in the pattern. The default argument
	 is used for groups that did not participate in the match; it 
	 defaults to None. (Incompatibility note: in the original Python 1.5 
	 release, if the tuple was one element long, a string would be 
	 returned instead. In later versions (from 1.5.1 on), a singleton 
	 tuple is returned in such cases.)

	For example:
'''
m = re.match(r"(\d+)\.(\d+)", "24.1632")
var=m.groups()
print var
#('24', '1632')
'''
	If we make the decimal place and everything after it optional, 
	not all groups might participate in the match. These groups will
	default to None unless the default argument is given:
'''
m = re.match(r"(\d+)\.?(\d+)?", "24")
var=m.groups()      # Second group defaults to None.
print var
#('24', None)
var=m.groups('0')   # Now, the second group defaults to '0'.
print var
#('24', '0')
'''
groupdict([default])

	Return a dictionary containing all the named subgroups of the match,
	 keyed by the subgroup name. The default argument is used for groups
	  that did not participate in the match; it defaults to None. 
	  For example:
'''
m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Malcolm Reynolds")
var=m.groupdict()
print var
#{'first_name': 'Malcolm', 'last_name': 'Reynolds'}
'''
start([group])
end([group])

	Return the indices of the start and end of the substring matched 
	by group; group defaults to zero (meaning the whole matched substring).
	Return -1 if group exists but did not contribute to the match.
	For a match object m, and a group g that did contribute to the
	match, the substring matched by group g (equivalent to m.group(g)) is

	m.string[m.start(g):m.end(g)]

	Note that m.start(group) will equal m.end(group) if group matched a 
	null string. For example, after m = re.search('b(c?)', 'cba'), 
	m.start(0) is 1, m.end(0) is 2, m.start(1) and m.end(1) are both 2, 
	and m.start(2) raises an IndexError exception.

	An example that will remove remove_this from email addresses:
'''
email = "tony@tiremove_thisger.net"
m = re.search("remove_this", email)
email[:m.start()] + email[m.end():]
#'tony@tiger.net'
'''
span([group])

	For MatchObject m, return the 2-tuple (m.start(group), m.end(group)). 
	Note that if group did not contribute to the match, this is (-1, -1).
	 group defaults to zero, the entire match.

pos

	The value of pos which was passed to the search() or match() method
	 of the RegexObject. This is the index into the string at which the
	  RE engine started looking for a match.

endpos

	The value of endpos which was passed to the search() or match()
	 method of the RegexObject. This is the index into the string
	  beyond which the RE engine will not go.

lastindex

	The integer index of the last matched capturing group, or None if no
	 group was matched at all. For example, the expressions
	  (a)b, ((a)(b)), and ((ab)) will have lastindex == 1 if applied to
	   the string 'ab', while the expression (a)(b) will have 
	   lastindex == 2, if applied to the same string.

lastgroup

	The name of the last matched capturing group, or None if the group
	 didn’t have a name, or if no group was matched at all.

re

	The regular expression object whose match() or search() method
	 produced this MatchObject instance.

string

	The string passed to match() or search().
'''

'''
Examples¶
*********
Checking For a Pair
'''

def displaymatch(match):
    if match is None:
		#<type 'NoneType'>
		return None
    return '<Match: %r, groups=%r>' % (match.group(), match.groups())

valid = re.compile(r"^[a2-9tjqk]{5}$")
print valid
var=displaymatch(valid.match("akt5q"))  # Valid.
print var
#"<Match: 'akt5q', groups=()>"
var=displaymatch(valid.match("akt5e"))  # Invalid. no "e" in regex class
print var
#None
var=displaymatch(valid.match("akt"))    # Invalid. not exact 5 characters 
print var
#None
var=displaymatch(valid.match("727ak"))  # Valid.
print var
#"<Match: '727ak', groups=()>"


pair = re.compile(r".*(.).*\1")
displaymatch(pair.match("717ak"))     # Pair of 7s.
#"<Match: '717', groups=('7',)>"
displaymatch(pair.match("718ak"))     # No pairs.
displaymatch(pair.match("354aa"))     # Pair of aces.
#"<Match: '354aa', groups=('a',)>"

pair.match("717ak").group(1)
#'7'

# Error because re.match() returns None, which doesn't have a group() method:
#pair.match("718ak").group(1)
#Traceback (most recent call last):
#  File "<pyshell#23>", line 1, in <module>
#    re.match(r".*(.).*\1", "718ak").group(1)
#AttributeError: 'NoneType' object has no attribute 'group'

pair.match("354aa").group(1)
#'a'

'''
search() vs. match()¶
'''
re.match("c", "abcdef")  # No match
re.search("c", "abcdef") # Match
#<_sre.SRE_Match object at ...>

re.match("c", "abcdef")  # No match
re.search("^c", "abcdef") # No match
re.search("^a", "abcdef")  # Match
#<_sre.SRE_Match object at ...>

re.match('X', 'A\nB\nX', re.MULTILINE)  # No match
re.search('^X', 'A\nB\nX', re.MULTILINE)  # Match
#<_sre.SRE_Match object at ...>

'''
Making a Phonebook¶
'''
text = """Ross McFluff: 834.345.1254 155 Elm Street

Ronald Heathmore: 892.345.3428 436 Finley Avenue
Frank Burger: 925.541.7625 662 South Dogwood Way


Heather Albrecht: 548.326.4584 919 Park Place"""
print "\n", text

entries = re.split("\n+", text)
print "\n", entries
#['Ross McFluff: 834.345.1254 155 Elm Street',
#'Ronald Heathmore: 892.345.3428 436 Finley Avenue',
#'Frank Burger: 925.541.7625 662 South Dogwood Way',
#'Heather Albrecht: 548.326.4584 919 Park Place']

#max split = 3
var=[re.split(":? ", entry, 3) for entry in entries]
print "\n",var
#[['Ross', 'McFluff', '834.345.1254', '155 Elm Street'],
#['Ronald', 'Heathmore', '892.345.3428', '436 Finley Avenue'],
#['Frank', 'Burger', '925.541.7625', '662 South Dogwood Way'],
#['Heather', 'Albrecht', '548.326.4584', '919 Park Place']]

#max split = 4
var=[re.split(":? ", entry, 4) for entry in entries]
print "\n",var
#[['Ross', 'McFluff', '834.345.1254', '155', 'Elm Street'],
#['Ronald', 'Heathmore', '892.345.3428', '436', 'Finley Avenue'],
#['Frank', 'Burger', '925.541.7625', '662', 'South Dogwood Way'],
#['Heather', 'Albrecht', '548.326.4584', '919', 'Park Place']]

'''
Text Munging
'''
#Vertausche in jedem Wort die Buchstaben im innern (erster und letzer nicht)
def repl(m):
	inner_word = list(m.group(2))
	random.shuffle(inner_word)
	return m.group(1) + "".join(inner_word) + m.group(3)
text = "Professor Abdolmalek, please report your absences promptly."
var=re.sub(r"(\w)(\w+)(\w)", repl, text)
print "\n",var
#'Poefsrosr Aealmlobdk, pslaee reorpt your abnseces plmrptoy.'
var=re.sub(r"(\w)(\w+)(\w)", repl, text)
print "\n",var
#'Pofsroser Aodlambelk, plasee reoprt yuor asnebces potlmrpy.'

'''
Finding all Adverbs
'''
text = "He was carefully disguised but captured quickly by police."
var=re.findall(r"\w+ly", text)
print "\n",var 
#['carefully', 'quickly']

'''
Finding all Adverbs and their Positions
'''
text = "He was carefully disguised but captured quickly by police."
for m in re.finditer(r"\w+ly", text):
	print '%02d-%02d: %s' % (m.start(), m.end(), m.group(0))
#07-16: carefully
#40-47: quickly
