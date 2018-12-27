#!/usr/bin/python
#import unittest

import doctest



class LevDist():
    def compute(self, a, b):
        '''
        >>> lev.compute('ich', 'du')
        2
        >>> lev.compute("apple", "orange")
        3
        >>> lev.compute("apple", "apple")
        1'''
        
        m = []

        #this is a comment
        for i in range(0,len(a)+1):
            m += [[]]
            for j in range(0,len(b)+1):
                m[i] += [0]
                if (i > 0 and j > 0):
                    m[i][j] = min(
                    m[i-1][j]+1,m[i][j-1]+1,
                    m[i-1][j-1]+(0 if
                    (a[i-1]==b[j-1]) else 1))
                    # these two lines make all the difference
                #else:
                    #	m[i][j] = max(i, j)
        return m[len(a)][len(b)]

if __name__ == "__main__":
	doctest.testmod(extraglobs={'lev': LevDist()})
	print "please input the first word:"
	ld = LevDist()
	a = raw_input()
	print "please input the second word:"
	b = raw_input()
	print ld.compute(a, b)
