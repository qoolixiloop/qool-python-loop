#!/usr/bin/env python
# -*- coding: utf-8 -*-

# simon.clematide@uzh.ch
# PCL I

def foo(a):
    """ Return foo of a """
    result = 0
    for item in a:
        result += item
    return result

c = foo([5,10,23])
print c
