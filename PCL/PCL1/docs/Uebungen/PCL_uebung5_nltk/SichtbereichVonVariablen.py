#!/usr/bin/env python
# -*- coding: utf-8 -*-

a=1
print "1", a
if 1:
	print "2", a
	for a in range(1,10):
		print "3",a
		if 1:
			print "4",a
		print "5", a
	print "6",a
print "7",a

print "------------------------------------"
if 1:
	for b in range(1,10):
		print "3",b
		if 1:
			print "4",b
		print "5", b
	print "6",b
print "7",b

print "------------------------------------"
if 1:
	for b in range(1,10):
		print "3",b
		if 1:
			c=1
			print "4",c
		print "5", c
	print "6",c
print "7",c
