# -*- coding: utf-8 -*-

# simon.clematide@uzh.ch
# PCL I

import re
#Achtung beim Bilden von Gruppen (). Gibt es capturing groups ()
#dann werden nur die Werte der capturing groups zurückgegeben.
#Sollen alle Matches zurückgegeben werden müssen alle Gruppen
#non capturing groups (?: ) sein.
text = "That U.S.A. poster-print costs $12.40... per m^2."
pattern = r'''(?x)         # set flag (?x) to allow verbose regexes
     (?:[A-Z]\.)+          # abbreviations, e.g. U.S.A.
   | \$?\d+(?:[.,]\d+)*%?  # currency/percentages, $12.40, 82%
   | \w+(?:-\w+)*          # words with optional internal hyphens
   | \.\.\.                # ellipsis
   | [.,;?]+               # punctuation
   | \S+                   # catch-all for non-layout characters
   '''
m = re.findall(pattern,text)
print m
