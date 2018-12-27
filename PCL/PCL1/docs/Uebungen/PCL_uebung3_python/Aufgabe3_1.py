#!/usr/bin/env python
# -*- coding: utf-8 -*-

#PCL I, Übung 3, HS15
#Aufgabe 3_1
#Autor: Roland Benz
#Matrikel-Nr.: 97-923-163 

'''
Der Schweizer Alpen-Club SAC hat die Lieblingsberge der Mitglieder als Python Dictionary regis-
triert. Verwende die Datei Aufgabe3_1.py und das darin definierte Dictionary SAC und schreibe ein
Python-Skript, welches folgendes ausführt:
a) Füge dem Dictionary ein weiteres Schlüssel-Wert-Paar hinzu, und gib die aktuelle Dictionary aus.
• Was passiert, wenn der neue Schlüssel mit einem bisherigen Schlüssel übereinstimmt, wenn
beispielsweise in unser Dictionary ’Schoenenberger’:’Rigi’ eingefügt wird?
• Was passiert, wenn danach ’Schoenenberger’:’Eiger’ eingefügt wird?
b) Gib die Schlüssel-Wert-Paare zeilenweise aus, wobei Schlüssel und Wert jeweils durch ein Tabu-
latorzeichen (Repräsentation: ’t’) getrennt sein sollen. Löse diese Aufgabe mit einer for- Schleife.
Die Ausgabe soll so aussehen:
Schoenenberger
Zueberbuehler
Stepankova
...
Rigi
Pizol
Pizol
c) Gib die sortierten Nachnamen aus, deren Lieblingsberge einen Namen länger als fünf Zeichen
haben. Ausgabe:
Bizirianis
Blickenstorfer
Helbling
Rutz
...
'''
'''
1	cmp(dict1, dict2)
Compares elements of both dict.
2	len(dict)
Gives the total length of the dictionary. This would be equal to the number of items in the dictionary.
3	str(dict)
Produces a printable string representation of a dictionary
4	type(variable)
Returns the type of the passed variable. If passed variable is dictionary, then it would return a dictionary type.
1	dict.clear()
Removes all elements of dictionary dict
2	dict.copy()
Returns a shallow copy of dictionary dict
3	dict.fromkeys()
Create a new dictionary with keys from seq and values set to value.
4	dict.get(key, default=None)
For key key, returns value or default if key not in dictionary
5	dict.has_key(key)
Returns true if key in dictionary dict, false otherwise
6	dict.items()
Returns a list of dict's (key, value) tuple pairs
7	dict.keys()
Returns list of dictionary dict's keys
8	dict.setdefault(key, default=None)
Similar to get(), but will set dict[key]=default if key is not already in dict
9	dict.update(dict2)
Adds dictionary dict2's key-values pairs to dict
10	dict.values()
Returns list of dictionary dict's values
'''

#Your code
dictSAC = {'Schoenenberger':'Rigi', 'Zueberbuehler':'Pizol', 'Stepankova':'Pizol', 'Schmid':'Flumserberge',
       'Rutz':'Pilatus', 'Zimmerli':'Jungfrau', 'Bizirianis':'Pfannenstiel', 'Maurer':'Dom',
       'Ferrari':'Eiger', 'Wiedmer':'Pfannenstock', 'Helbling':'Platthorn' , 'Blickenstorfer':'Weisshorn'}
strSAC=str(dictSAC)
print "\nSAC Dictionary:\n %s\n" % (strSAC)

#a) Füge dem Dictionary ein weiteres Schlüssel-Wert-Paar hinzu, und gib die aktuelle Dictionary aus.
print "\nTask a)"
#new key value pair
newKeyValuePair={"Benz":"Uetliberg"}
strNewKeyValuePair=str(newKeyValuePair)
print "New key-value pair:\n %s\n" % (strNewKeyValuePair)
#update dictionary with new key value pair
dictSAC.update(newKeyValuePair)
strSAC=str(dictSAC)
print "SAC Dictionary:\n %s\n" % (strSAC)

#a.1)• Was passiert, wenn der neue Schlüssel mit einem bisherigen Schlüssel übereinstimmt, wenn
#beispielsweise in unser Dictionary ’Schoenenberger’:’Rigi’ eingefügt wird?
print "\nTask a.1)"
#new key value pair
newKeyValuePair={"Schoenenberger":"Rigi"}
strNewKeyValuePair=str(newKeyValuePair)
print "New key-value pair:\n %s\n" % (strNewKeyValuePair)
#update dictionary with new key value pair
dictSAC.update(newKeyValuePair)
strSAC=str(dictSAC)
print "SAC Dictionary:\n %s\n" % (strSAC)
#-->Anser: no duplication! Dictionaries are unsorted sets of key-value tuples

#a.2)• Was passiert, wenn danach ’Schoenenberger’:’Eiger’ eingefügt wird?
print "\nTask a.2)"
#new key value pair
newKeyValuePair={"Schoenenberger":"Eiger"}
strNewKeyValuePair=str(newKeyValuePair)
print "New key-value pair:\n %s\n" % (strNewKeyValuePair)
#update dictionary with new key value pair
dictSAC.update(newKeyValuePair)
strSAC=str(dictSAC)
print "SAC Dictionary:\n %s\n" % (strSAC)
#-->Anser: no duplication! Rigi will be replaced with Eiger for the key Schoenenberger

#b) Gib die Schlüssel-Wert-Paare zeilenweise aus, wobei Schlüssel und Wert jeweils durch ein Tabu-
#latorzeichen (Repräsentation: ’t’) getrennt sein sollen. Löse diese Aufgabe mit einer for- Schleife.
print "\nTask b)"
lstKeysDictSAC=dictSAC.keys()
for elem in lstKeysDictSAC:
	print "Key: %s \t Value: %s" %(elem,dictSAC[elem])


#c) Gib die sortierten Nachnamen aus, deren Lieblingsberge einen Namen länger als fünf Zeichen
#haben.
print "\nTask c)"
lstOfTplKeyValuePairsOfDictSAC=dictSAC.items()
#unsorted
print "\nUnsorted list of tuples\n"
for elem in lstOfTplKeyValuePairsOfDictSAC:
	if len(elem[1])>5:
		print "Name: %s \t Long mountain name: %s" %(elem[0], elem[1])
#sorted
print "\nSorted list of tuples, sorted on first tuple element x[0]\n"
lstsortedOfTplKeyValuePairsOfDictSAC = sorted(lstOfTplKeyValuePairsOfDictSAC,key=lambda x: x[0])
for elem in lstsortedOfTplKeyValuePairsOfDictSAC:
	if len(elem[1])>5:
		print "Name: %s \t Long mountain name: %s" %(elem[0], elem[1])
