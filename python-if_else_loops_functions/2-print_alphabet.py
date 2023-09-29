#!/usr/bin/python3
c = 'a'
while c <= 'z':
	print(f"{c}", end="")
	c = chr(ord(c) + 1)
