#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from collections import defaultdict

def main():

    # Driver program
    X = "AATCC"
    Y = "ACACG"
    m = len(X)
    n = len(Y)
    C = LCS(X, Y)

    print LCS(X, Y)
    print "Some LCS: '%s'" % backTrack(C, X, Y, m, n)
    print "All LCSs: %s" % backTrackAll(C, X, Y, m, n)

    # Driver program
    print "Length of LCS is ", \
        lcs_dynamic_programming(X, Y)

    # Driver program
    X = [
        "This part of the document has stayed",
        "the same from version to version.",
        "",
        "This paragraph contains text that is",
        "outdated - it will be deprecated '''and'''",
        "deleted '''in''' the near future.",
        "",
        "It is important to spell check this",
        "dokument. On the other hand, a misspelled",
        "word isn't the end of the world.",
    ]
    Y = [
        "This is an important notice! It should",
        "therefore be located at the beginning of",
        "this document!",
        "",
        "This part of the document has stayed",
        "the same from version to version.",
        "",
        "It is important to spell check this",
        "document. On the other hand, a misspelled",
        "word isn't the end of the world. This",
        "paragraph contains important new",
        "additions to this document.",
    ]

    C = LCS(X, Y)
    printDiff(C, X, Y, len(X), len(Y))


#Computing the length of the LCS
def LCS(X, Y):
    m = len(X)
    n = len(Y)
    # An (m+1) times (n+1) matrix
    C = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                C[i][j] = C[i-1][j-1] + 1
            else:
                C[i][j] = max(C[i][j-1], C[i-1][j])
    return C

#Reading out an LCS
def backTrack(C, X, Y, i, j):
    if i == 0 or j == 0:
        return ""
    elif X[i-1] == Y[j-1]:
        return backTrack(C, X, Y, i-1, j-1) + X[i-1]
    else:
        if C[i][j-1] > C[i-1][j]:
            return backTrack(C, X, Y, i, j-1)
        else:
            return backTrack(C, X, Y, i-1, j)

#Reading out all LCSs
def backTrackAll(C, X, Y, i, j):
    if i == 0 or j == 0:
        return set([""])
    elif X[i-1] == Y[j-1]:
        return set([Z + X[i-1] for Z in backTrackAll(C, X, Y, i-1, j-1)])
    else:
        R = set()
        if C[i][j-1] >= C[i-1][j]:
            R.update(backTrackAll(C, X, Y, i, j-1))
        if C[i-1][j] >= C[i][j-1]:
            R.update(backTrackAll(C, X, Y, i-1, j))
        return R

# Dynamic Programming implementation of LCS problem
def lcs_dynamic_programming(X , Y):
    # find the length of the strings
    m = len(X)
    n = len(Y)

    # declaring the array for storing the dp values
    L = [[None]*(n+1) for i in xrange(m+1)]

    """Following steps build L[m+1][n+1] in bottom up fashion
    Note: L[i][j] contains length of LCS of X[0..i-1]
    and Y[0..j-1]"""
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0 :
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j] , L[i][j-1])

    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    return L[m][n]
    #end of function lcs

#Print the diff
def printDiff(C, X, Y, i, j):
    if i > 0 and j > 0 and X[i-1] == Y[j-1]:
        printDiff(C, X, Y, i-1, j-1)
        print "  " + X[i-1]
    else:
        if j > 0 and (i == 0 or C[i][j-1] >= C[i-1][j]):
            printDiff(C, X, Y, i, j-1)
            print "+ " + Y[j-1]
        elif i > 0 and (j == 0 or C[i][j-1] < C[i-1][j]):
            printDiff(C, X, Y, i-1, j)
            print "- " + X[i-1]


if __name__ == "__main__":
	main()