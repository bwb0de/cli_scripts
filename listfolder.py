#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os, glob, time, sys

homedir = '/home/elbode'
initdir = os.getcwd()
targetfolder = sys.argv[1]


try:
	oldlist = sys.argv[2]
except:
	pass

f= open('tmpout','r')
d = f.read()
f.close()

os.chdir(initdir)

d = d.replace('./','/')
d = d.split(':\n')
x = []

for i in d:
	n = initdir + i
	x.append(n)

out = ''
for i in x:
	os.chdir(i)
	p = glob.glob('*.*')
	for ii in p:
		out = out + i + ii + '\n'

os.chdir(initdir)
f = open('LISTA '+ str(time.ctime()),'w')
f.write(out)
f.close()

