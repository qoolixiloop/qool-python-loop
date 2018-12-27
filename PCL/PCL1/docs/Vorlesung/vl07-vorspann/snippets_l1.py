#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import sys
reload(sys)
sys.setdefaultencoding('iso-8859-1')

print """File is encoded with iso-8859-1
      File Coding needs to specified (see 2. line)
      so that python is able to read letter �"""

#Encoding for letter �
#http://www.utf8-zeichentabelle.de/
print """\nEncodings for letter �:
      iso-8859-1 (Latin 1): C4 (=196 or 11000100);
      unicode             : U+00C4 (=196 or 11000100);
      utf-8               : c3 84 (=50052 or 11000011 10000100)"""

#Conversion between hex, decimal and binary
print "\nConversion between hex, decimal and binary"
print int('0xc4',16)                  #196
print bin(196)                        #0b11000100
print int('0xc384',16)                #50052
print bin(50052)                      #0b 11000011 10000100

#String type str with iso-8859-1 encoding
print "\nString type str with iso8859-1 encoding"
apple_type_str_l1 = "\xC4pple"        #�pple with iso-8859-1 encoding
print type(apple_type_str_l1)         #<type 'str'>
print apple_type_str_l1               #?pple

#String type str with utf-8 encoding
print "\nString type str with utf-8 encoding"
apple_type_str_utf8 = "\xC3\x84pple"  #�pple with utf-u encoding
print type(apple_type_str_utf8)       #<type 'str'>
print apple_type_str_utf8             #�pple

#String type unicode
print "\nString type unicode"
apple_type_unicode = u"\xC4pple"      #�pple with unicode encoding
print type(apple_type_unicode)        #<type 'unicode'>
print apple_type_unicode              #�pple

#Conversion between iso8859-1, unicode and utf-8
print "\nConversion between iso8859-1, unicode and utf-8"
apple_type_unicode = apple_type_str_l1.decode('iso-8859-1')
print type(apple_type_unicode)        #<type 'unicode'>
print apple_type_unicode              #�pple with unicode encoding
apple_type_str_utf8 = apple_type_unicode.encode('utf-8')
print type(apple_type_str_utf8)       #<type 'str'>
print apple_type_str_utf8             #�pple with utf-u encoding

print "\nConversion between utf-8, unicode and iso8859-1"
apple_type_unicode = apple_type_str_utf8.decode('utf-8')
print type(apple_type_unicode)        #<type 'unicode'>
print apple_type_unicode              #�pple with unicode encoding
apple_type_str_l1 = apple_type_unicode.encode('iso-8859-1')
print type(apple_type_str_l1)         #<type 'str'>
print apple_type_str_l1               #?pple with iso-8859-1 encoding