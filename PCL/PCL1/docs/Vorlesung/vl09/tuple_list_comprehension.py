#!/usr/bin/env python
# -*- coding: utf-8 -*-

# simon.clematide@uzh.ch
# PCL I


tuples2 = [('a',1),('b',2),('c',3),('d',4)]
#tuples2= "klklk"   #funktioniert nicht da kein Tupel

l1 = [(c2,c1) for (c1,c2) in tuples2]

print l1   #[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
