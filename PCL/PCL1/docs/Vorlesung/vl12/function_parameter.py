#!/usr/bin/env python
# -*- coding: utf-8 -*-

# simon.clematide@uzh.ch
# PCL I
#
global_list = [('der',1200),('die',1000),('das',900)]
print "\nfrom 0: ", global_list

def del_first(l):
    print "\nfrom 1.1: ", 'global_list is parameter l:',\
        global_list is l
    del l[0]
    print "\nfrom 1.2: ", 'global_list is parameter l:',\
        global_list is l

del_first(global_list)
print "\nfrom 2: ", global_list

del_first(global_list)
print "\nfrom 3: ", global_list

