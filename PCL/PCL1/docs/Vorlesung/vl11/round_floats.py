#!/usr/bin/env python
# -*- coding: utf-8 -*-

# simon.clematide@uzh.ch
# PCL I
# Achtung: Python-Versionen > 2.6 unterscheiden sich von denen <= 2.6
# Möglichst fehlerfreies Runden ist ein schwieriges Thema:
# http://en.wikipedia.org/wiki/Rounding#Round_half_away_from_zero

print  "Zahlen runden"

print "round(0.05,1) ==>", round(0.05,1)," up"
print "round(0.15,1) ==>", round(0.15,1)
print "round(0.25,1) ==>", round(0.25,1)," up"
print "round(0.35,1) ==>", round(0.35,1)
print "round(0.45,1) ==>", round(0.45,1)," up"
print "round(0.55,1) ==>", round(0.55,1)
print "round(0.65,1) ==>", round(0.65,1)," up"
print "round(0.75,1) ==>", round(0.75,1)," up"
print "round(0.85,1) ==>", round(0.85,1)
print "round(0.95,1) ==>", round(0.95,1)
print
print "round(1.05,1) ==>", round(1.05,1)," up"
print "round(1.15,1) ==>", round(1.15,1)
print "round(1.25,1) ==>", round(1.25,1)," up"
print "round(1.35,1) ==>", round(1.35,1)," up"
print "round(1.45,1) ==>", round(1.45,1)
print "round(1.55,1) ==>", round(1.55,1)," up"
print "round(1.65,1) ==>", round(1.65,1)
print "round(1.75,1) ==>", round(1.75,1)," up"
print "round(1.85,1) ==>", round(1.85,1)," up"
print "round(1.95,1) ==>", round(1.95,1)
print
print "'Runden' durch die Formatierung"
print "'%.1f' % 0.05 ==>",'%.1f' % 0.05," up"
print "'%.1f' % 0.15 ==>",'%.1f' % 0.15
print "'%.1f' % 0.25 ==>",'%.1f' % 0.25
print "'%.1f' % 0.35 ==>",'%.1f' % 0.35
print "'%.1f' % 0.45 ==>",'%.1f' % 0.45," up"
print "'%.1f' % 0.55 ==>",'%.1f' % 0.55," up"
print "'%.1f' % 0.65 ==>",'%.1f' % 0.65," up"
print "'%.1f' % 0.75 ==>",'%.1f' % 0.75," up"
print "'%.1f' % 0.85 ==>",'%.1f' % 0.85
print "'%.1f' % 0.95 ==>",'%.1f' % 0.95
