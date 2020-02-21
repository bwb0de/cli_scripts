#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys

pag = int(sys.argv[1])

def folheto(n):
	m = (4,1,2,3)
	loops = n/4
	count = 0
	r = ''
	while count != loops:
		for i in m:
			r = r + str(i+(4*count)) + ','
		count = count + 1
	r = r[:-1]	
	return r

output = folheto(pag)
print output

