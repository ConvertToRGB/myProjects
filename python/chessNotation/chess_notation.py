# -*- coding: utf-8 -*-

import os
import xml.etree.ElementTree as ET

'''put your path for your txt filehere'''
p = r"E:example.txt"

'''create xml tree and variables'''
tree = ET.parse(p)
root = tree.getroot()
counter = 0
move = ''

'''working iterator'''
for i, elem in enumerate(root.getiterator()):

	if not str(elem.text).isspace():	

		t = str(elem.text).strip()
		move = move + t + ' '

		counter+=1

		if counter % 3 == 0:
			print move
			counter = 0
			move = ''
