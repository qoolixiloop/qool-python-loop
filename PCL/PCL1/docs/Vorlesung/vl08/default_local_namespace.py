#!/usr/bin/env python
# -*- coding: utf-8 -*-

# simon.clematide@uzh.ch
# PCL I

s = 'Python is great!'
def f():
    s = "But that's strange."
    print s

print s
f()
print s

# Output
# Python is great!
# But that's strange.
# Python is great!