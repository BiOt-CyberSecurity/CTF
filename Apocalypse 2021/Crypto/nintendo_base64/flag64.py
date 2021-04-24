#!/usr/bin/env python 

import base64

f = open('output.txt' , 'r')

content = f.read()

for i in range(8):

	x = content.decode('base64')
	content = x 

print content
