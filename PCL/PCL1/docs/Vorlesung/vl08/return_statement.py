#!/usr/bin/env python
# -*- coding: utf-8 -*-

# simon.clematide@uzh.ch
# PCL I

def describe_number(n):
    if n > 1000000:
        return "LARGE"
    elif n > 1000:
        return "Medium"
    else:
        return "small"

    print "Never printed!"
    

print 9, ":", describe_number(9)
print 999, ":",describe_number(999)
print 999999, ":",describe_number(99999)
print 9999999999, ":",describe_number(9999999999)

