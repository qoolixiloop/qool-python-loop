#!/usr/bin/python
# -*- coding: utf-8 -*-

# simon.clematide@uzh.ch
# PCL I

import codecs

#Datei ae-l1.txt Western(ISO-8859-15)
#a� mit utf-8; a\E4 mit Gedit

#http://unicode-table.com/de/#latin-1-supplement
#http://www.utf8-zeichentabelle.de/
#https://de.wikipedia.org/wiki/ISO_8859-1
print "\nHexadezimale Representation des Speicherinhalts für:"
print "ä: ISO8859-1=E4; Unicode=U+00E4(228); utf-8=c3 a4(11000011 10100100)"
print "Ä: ISO8859-1=C4; Unicode=U+00C4(196); utf-8=c3 84(11000011 10000100)"

print "ü: ISO8859-1=FC; Unicode=U+00FC(252); utf-8=c3 bc"
print "Ü: ISO8859-1=DC; Unicode=U+00DC(220); utf-8=c3 9c"
print "ö: ISO8859-1=F6; Unicode=U+00F6(246); utf-8=c3 b6"
print "Ö: ISO8859-1=D6; Unicode=U+00D6(214); utf-8=c3 96"


#Encode-Decode
#.------------
#Decode: Typ String --> Typ Unicode
#Encode: Typ Unicode --> Typ String

# Decode from l1 encoded file into unicode strings
f = open("./ae-l1.txt", "r")
f1 = codecs.open("./ae-l1.txt", "r", "l1")
f2 = codecs.open("./ae-l1.txt", "r", "utf-8")

# Encode unicode strings into UTF-8 or l1 encoded file
g = open("./AE-encoded.txt", "w")
g1 = codecs.open("./AE-l1-encoded-as-l1.txt", "w", "l1")
g2 = codecs.open("./AE-l1-encoded-as-utf8.txt", "w", "utf-8")
g3 = codecs.open("./AE-utf-8-encoded-as-l1.txt", "w", "l1")
g4 = codecs.open("./AE-utf-8-encoded-as-utf8.txt", "w", "utf-8")

print "\nDatei ae-l1.txt hat Western(ISO-8859-15)= l1 Kodierung\
 und enthält die Zeichen a\E4 (Gedit), also aä; a� mit utf-u8 \n"

print 'f ist vom Typ String und übernimmt a\E4. E4 wird jedoch' \
      'nicht erkannt von der upper() Methode und ignoriert'
print 'g schreibt A\E4 in Datei AE-encoded.txt' \
      ' (ISO-8859 text) gemäss file *\n'\
      ' (Es erscheint beim Öffnen: A� mit utf-8; A\E4 mit Gedit)'
for line in f: #f thought input was utf-8
    g.write(line.upper())
    print "f Type:", type(line) #output as l1
    print "f Canonical repr(line.upper()):", "==>",repr(line.upper()), "<=="
    print "f Canonical repr(line):", "==>",repr(line), "<=="
    print "f Printed line.upper():","==>",line.upper(), "<=="
    print "f Printed line:","==>",line, "<==\n"

print 'f1 ist von Typ unicode. f1 wusste, dass Input l1 kodiert ' \
      'ist, E4 wird von upper()Methode erkannt und auf C4 geändert'
print 'g1 schreibt A\C4 in Datei AE-l1-encoded-as-l1.txt' \
      ' (ISO-8859 text) gemäss file *\n' \
      ' (Es erscheint beim Öffnen: A� mit UTF-8; A\C4 mit Gedit)'
print 'g2 schreibt AÄ in Datei AE-l1-encoded-as-utf8.txt' \
      ' (UTF-8 Unicode text) gemäss file *\n' \
      ' (Es erscheint beim Öffnen: AÄ mit UTF-8; AÄ mit Gedit)'
for line in f1: #f1 knew input was l1
    g1.write(line.upper())
    g2.write(line.upper()) #output as utf-8
    print "f1 Type:", type(line) #output as l1
    print "f Canonical repr(line.upper()):", "==>",repr(line.upper()), "<=="
    print "f Canonical repr(line):", "==>",repr(line), "<=="
    print "f Printed line.upper():","==>",line.upper(), "<=="
    print "f Printed line:","==>",line, "<==\n"

print 'f2 ist von Typ unicode. f2 dachte Input sei utf-8 und ' \
      'ignorierte das unbekannte ä'
print 'g3 schreibt A in Datei AE-utf-8-encoded-as-l1.txt' \
      ' (very short file (no magic)) gemäss file *\n' \
      ' (Es erscheint beim Öffnen: A mit UTF-8; A mit Gedit)'
print 'g4 schreibt A in Datei AE-utf-8-encoded-as-utf8.txt' \
      ' (very short file (no magic)) gemäss file *\n' \
      ' (Es erscheint beim Öffnen: A mit UTF-8; A mit Gedit)'
for line in f2: #f2 thought input was utf-8
    g3.write(line.upper())
    g4.write(line.upper()) #output as utf-8
    print "f2 Type:", type(line) #output as l1
    print "f Canonical repr(line.upper()):", "==>",repr(line.upper()), "<=="
    print "f Canonical repr(line):", "==>",repr(line), "<=="
    print "f Printed line.upper():","==>",line.upper(), "<=="
    print "f Printed line:","==>",line, "<==\n"

print type(f), type(f1), type(f2),

f1.close()
g1.close()
f2.close()
g2.close()

