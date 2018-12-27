#!/usr/bin/env python
# -*- coding: utf-8 -*-

# simon.clematide@uzh.ch
# PCL I
# Rechenzeit und Speichereffizienz messen
#========================================
import nltk, timeit, time, os

print 'process id:', os.getpid()

words = nltk.corpus.brown.words()

def test_listcomprehension():
    return set([w.lower() for w in words])

# Initialisiere Timer-Objekt
tl = timeit.Timer(test_listcomprehension)

# Timing von Listenkomprehension
print 'Timed list comprehension (seconds):', tl.timeit(1)

# Speicherverbrauch muss von ausserhalb gemessen werden.
# Es gibt keinen einfachen Weg, das innerhalb von Python zu machen.
time.sleep(600) # 600 Sekunden

# HOWTO und Erklärungen
# (1) Programm via Terminal im Hintergrund aufstarten (&):
#     $ python timeit_listcomprehension.py &
#     $ python timeit_generator.py &
#     Das Programm gibt jeweils die Prozess-ID aus, unter der es läuft.
#     Damit können die Programme auseinander gehalten werden.
#     Im Folgenden steht PID1 bzw. PID2 für die jeweilge nummerische ID.

# (2) Speicherverbrauch messen im Terminal mit ps:
#     $ ps -vp PID1
#     $ ps -vp PID2
#     Die entscheidende Information steckt im Attribut RSS (resident set size),
#     das den physikalisch belegten Speicher in Kilobytes (im Gegensatz zum
#     virtuellen Speicher) misst.

# (3) Speicherverbrauch messen mit Task Manager (WIN) oder Aktivitätsanzeige (MACOS)
#     Am besten Filtern auf python, danach den Prozess über seine Prozess-ID identifizieren.
