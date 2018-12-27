#!/usr/bin/python
# -*- coding: utf-8 -*-

#ohne die coding Zeile gibt es eine Fehlermeldung, wenn diese
#Datei einen Umlaut enthält (wie in enthält)
#(line 4 SyntaxError: Non-ASCII character '\xc3' in file)
#Roland Benz

#Die unicode, L1 und utf-8 Tabellen enthalten die Ascii Tabelle
#Die unicode Tabelle enthält die L1 Tabelle (oder zumindest Teile davon)
#Die unicode und utf-8 Tabellen ähneln zwischen den Zeichen 128-191
#utf-8 hat in diesem Bereich lediglich eine c2 oder c3 davor.

def tell_me_about(s): return (type(s), s)

#A plain string
#----------------
v = "\xC4pple" # type string
u = u'\xc4pple' # type unicode

print "0:", tell_me_about(v)
#(<type 'str'>, '\xc4pple')

print "1:",tell_me_about(u)
#(<type 'unicode'>, u'\xc4pple')

#Versuch den String als utf-8 interpretiert(encoded) darzustellen
print "2:", repr(v), str(v)
#'\xc4pple' �pple
#aber im Interpreter:
#>>> str('\xC4pple')
#'\xc4pple'
#>>> print str('\xC4pple')
#�pple

print "3:", repr(u)
#u'\xc4pple'

#Versuch aus einem Typ unicode einen String darzustellen
#scheitert daran, dass ascii ein Problem hat.
#print "3:",str(u)
# UnicodeEncodeError: 'ascii' codec can't encode character
# u'\xc4' in position 0: ordinal not in range(128)

#Versuch den String als utf-8 interpretiert(encoded) darzustellen
print "4:", v
#�pple

#Der Typ unicode wird korrekt verarbeitet
print "5:", u
#Äpple

#Decoding a iso8859-1 string - convert plain string to unicode
#---------------
#decode string to unicode with L1 table
uv = v.decode("iso-8859-1") #benützt L1 Tabelle
print "6:", repr(uv)
#u'\xc4pple'      #c4 ist Ä in unicode (und L1)

print "7:", tell_me_about(uv)
#(<type 'unicode'>, u'\xc4pple')

#Der Typ unicode wird korrekt verarbeitet
print "8:",uv,  "\xC4pple".decode("iso-8859-1")
#Äpple Äpple

print "9:", v.decode('iso-8859-1') == u'\xc4pple'
#True

#Versuch den String mit utf-8 Tabelle zu decoden schlägt fehl
#uv1 = v.decode("utf-8")
#print "9:", repr(uv)
# return codecs.utf_8_decode(input, errors, True)
# UnicodeDecodeError: 'utf8' codec can't decode byte 0xc4
# in position 0: invalid continuation byte

#decode String (in utf-8) to unicode with (useless?) L1 table
#Es wird ein Typ unicode erzeugt mit utf-8 Kodierung
uv2 = "Äpple".decode("iso-8859-1")
print "10:", repr(uv2), repr("Äpple")
#u'\xc3\x84pple'    #c3 84 ist utf-8 für Ä

print "11:", tell_me_about(uv2)
#(<type 'unicode'>, u'\xc3\x84pple')

#decode String (in utf-8) to unicode with utf-8 table
#Es wird ein Typ unicode erzeugt mit unicode (und L1) Kodierung
uv3 = "Äpple".decode("utf-8")
print "12:", repr(uv3)
#u'\xc4pple'        #c4 ist Ä in unicode (und L1)

print "13:", tell_me_about(uv3)
#(<type 'unicode'>, u'\xc4pple')


#A little more illustration — with “Ä”
#----------------
#Typ unicode ist gleich Typ unicode
print "14:", u"Ä" == u"\xc4", repr(u"Ä"), repr(u"\xc4")
#True u'\xc4' u'\xc4'

#Typ String in utf-8 ist nicht gleich Typ unicode
print "15:", "Ä" == u"\xc4", repr("Ä"), repr(u"\xc4")
#False '\xc3\x84' u'\xc4'

#Typ String in utf-8 ist gleich Typ unicode im Ascii Bereich
print "16:", "a" == u"a", repr("a"), repr(u"a")

#Typ String (in utf-8) in Typ unicode dekodiert ist gleich Typ unicode
print "17:", "Ä".decode('utf8') == u"\xc4", \
    repr("Ä".decode('utf-8')), repr(u"\xc4")
#True u'\xc4' u'\xc4'

#Typ String (in utf-8) ist ungleich Typ String (in L1, unicode)
print "18:", "Ä" == "\xc4"
#False

#Encode-Decode
#.------------
#Decode: Typ String --> Typ Unicode
#Encode: Typ Unicode --> Typ String

#Encoding to UTF
#----------------
#v = "\xC4pple" # type string
# convert Type String (in iso-8859-1) to Type unicode
# and to Type String (in utf-8)
u8 = v.decode("iso-8859-1").encode("utf-8")
print "19:",repr(u8), str(u8), u8
#'\xc3\x84pple' Äpple Äpple

print "20:",tell_me_about(u8)
#(<type 'str'>, '\xc3\x84pple')

#Convert to String in utf-16
u16 = v.decode('iso-8859-1').encode('utf-16')
print "21:",tell_me_about(u16), str(u16), u16
#(<type 'str'>, '\xff\xfe\xc4\x00p\x00p\x00l\x00e\x00')
#  ��� p p l e  ��� p p l e

#Convert to Type unicode
print "22:",tell_me_about(u8.decode('utf8'))
#(<type 'unicode'>, u'\xc4pple')

#Convert to Type unicode
print "23:",tell_me_about(u16.decode('utf16'))
#(<type 'unicode'>, u'\xc4pple')

#Relationship between unicode and UTF and latin1
#----------------
#Typ String in utf-8
print "24:", u8
#Äpple

#Typ unicode
print "25:",u8.decode('utf-8') # printing unicode
#Äpple

#Typ String in utf-16, print statement interprets u16 as utf-8
print "26:",u16     # printing 'bytes' of u16
#���pple

#Typ unicode
print "27:",u16.decode('utf16')
#Äpple             # printing unicode

#Typ String in L1 vs Typ String in utf-8
print "28:",v == u8
#False             # v is a iso8859-1 string; u8 is a utf-8 string

#Typ unicode vs Typ String in utf-8
print "29:",v.decode('iso8859-1') == u8
#False             # v.decode(...) returns unicode

#Strings decode to the same representation in Typ unicode
print "30:",u8.decode('utf-8') == v.decode('latin1') == u16.decode('utf-16')
#True              # all decode to the same unicode memory representation
                  # (latin1 is iso-8859-1)

#Unicode Exceptions
#----------------
#Versuch Typ String in utf-8 direkt nach Typ String in l1 zu kodieren
print "31:", u8.encode('iso8859-1')
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#UnicodeDecodeError: 'ascii' codec can't decode byte 0xc3 in position 0:
#  ordinal not in range(128)

print "32:", u16.encode('iso8859-1')
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#UnicodeDecodeError: 'ascii' codec can't decode byte 0xff in position 0:
#  ordinal not in range(128)

v.encode('iso8859-1')
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#UnicodeDecodeError: 'ascii' codec can't decode byte 0xc4 in position 0:
#  ordinal not in range(128)