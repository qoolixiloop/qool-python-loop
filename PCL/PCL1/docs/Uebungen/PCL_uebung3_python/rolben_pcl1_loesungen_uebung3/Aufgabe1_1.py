#!/usr/bin/env python
# -*- coding: utf-8 -*-


#PCL I, Übung 3, HS15
#Aufgabe 1_1
#Autor: Roland Benz
#Matrikel-Nr.: 97-923-163

'''
1.1 Listen bearbeiten und manipulieren
Nutze für diese Aufgabe die Python-Dokumentation zu Listen (Abschnitt 5.1 More on Lists und
5.6.4. Mutable Sequence Types) und das Lehrvideo.
Für diese Aufgabe steht ein Programm Aufgabe1.py bereit, welches die Liste text beinhaltet. Er-
gänze das gegebene Skript so, dass es (nacheinander)
a) am Ende der Liste ein Ausrufezeichen anhängt,
b) der Liste die Wörter des Satzes ’Dies ist mein Satz’ hinzufügt
c) die Anzahl der Vorkommen des Tokens ’ist’ ermittelt und mitteilt,
d) das erste Vorkommen von ’&’ aus der Liste entfernt und '%'
e) vor dem dritten Element (achte auf Index!) das Wort ’so’ einfügt,
f) das erste Element mit dem Wort ’Computerlinguistik’ ersetzt (d.h. Anzahl Elemente bleibt gleich),
g) und zum Schluss das erste Vorkommen von ’sehr’ mit ’unglaublich’ ersetzt (schwieriger).
Am Ende soll die modifizierte Liste als Text ausgegeben werden. Benutze ' '.join(list_name) um
die Ausgabe zu formatieren.
Versuche die Lösung so allgemein wie möglich zu halten, z.B. sollte d) auch noch korrekt funktionie-
ren, wenn am Anfang der Liste zusätzliche Elemente eingefügt werden.
Kommentiere dein Programm sinnvoll. Abzugeben ist das komplette von dir ergänzte, ausführbare
Skript. (Bitte benenne das Dokument wie oben definiert.)
'''

lstText = ['Programmieren', 'macht', '%', 'Spass', 'und', 'ist', 
			'sehr', 'spannend','.', 'Jetzt', 'wollen', 'wir', 'den', 
			'Umgang', 'mit', 'Listen', 'verstehen']
		
#Your code
dBug=False
if dBug:                  
	import pdb              
	pdb.set_trace()

#a)
lstText_a = lstText + ["!"]
#b)
strText_b = "Dies ist mein Satz"
lstText_b = strText_b.split(" ")
lstText_b = lstText + lstText_b
#c)
intCntIst_c=0
for word in lstText_b:
	if word == "ist":
		intCntIst_c +=1
print "Das Wort \"ist\" kommt " + str(intCntIst_c) + " Mal vor."
#d)
iter=0
lstText_d=[]
for word in lstText_b:	
	if word == "%":
		lstText_d = lstText_b
		del lstText_d[iter]
		break
	iter+=1	
print lstText_d
#e)
lstText_e = lstText_d
lstText_e.insert(2,"so")	
print lstText_e	
#f
lstText_f = lstText_e
lstText_f[0] = "Computerlinguistik"
print lstText_f
#g
iter=0
lstText_g=[]
for word in lstText_f:	
	if word == "sehr":
		lstText_g = lstText_f
		lstText_g[iter] =  "unglaublich"
		break
	iter+=1	
print lstText_g



