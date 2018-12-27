#!/usr/bin/env python
# -*- coding: utf-8 -*-
#PCL II Uebung 02
#Aufgabe 3
#Musterloesung
#AutorIn: Irene

from lxml import etree as ET

#Initiating etree object form XML file
plants_file = ET.parse("plants.xml")
plants = plants_file.getroot()

zone5 = []
zone3 = []
cost = 0
shade = []

#Iterating through XML file
for plant in plants:
	if plant.get('zone') == '5':
		for common in plant.iter('COMMON'):
			zone5.append(common.text)
	elif plant.get('zone') == '3':
		name = ''
		light = ''
		for common in plant.iter('COMMON'):
			name = common.text
		for lightcond in plant.iter('LIGHT'):
			light = lightcond.text
		zone3.append((name,light))
	for price in plant.iter('PRICE'):
		cost += float(price.text)
	for lightcond in plant.iter('LIGHT'):
		if lightcond.text == 'Shade':
			for botanical in plant.iter('BOTANICAL'):
				shade.append(botanical.text)

#counting elements with xpath				
count = plants.xpath('count(//PLANT)')

#printing results
print 'Pflanzen der Zone 5:'
for plant in zone5:
	print plant
print '\nPflanzen der Zone 3 und ihre Lichtbedingung: '
for plant in zone3:
	print plant[0],':',plant[1]
print '\nSummer aller Kosten:',cost
print '\nDie botanischen Namen der Pflanzen, welche Schatten brauchen: '
for plant in set(shade):
	print(plant)
print '\nAnzahl Pflanzen: ',count

