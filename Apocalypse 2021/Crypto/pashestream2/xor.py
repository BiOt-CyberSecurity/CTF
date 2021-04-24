#!/usr/bin/env python

from pwn import *

lines = read('output.txt').splitlines()

for i in range(0xff):
	info('XORin\' lines with %#x',i)
	byte = bytes([i])
	for line in lines:
		xored =xor(unhex(line), byte)
		if b"CHTB" in xored:
			print(xored)
