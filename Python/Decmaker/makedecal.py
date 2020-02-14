#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import os
f = open('Modelo.odp','r')
m = f.read()
f.close()

f = open('lista','r')
l = f.read().split(os.linesep)
f.close()

os.chdir('TMP')

for i in l:
	line = i.split(',')
	nome = line[0]
	hh = line[1]
	f = open('Mod.odp','w')
	f.write(m)
	f.close()
	os.system('unzip Mod.odp; rm Mod.odp')
	f = open('content.xml','r')
	d = f.read()
	f.close()
	d = d.replace('NOME',nome).replace('HH',hh)
	f = open('content.xml','w')
	f.write(d)
	f.close()
	os.system('zip -0 -r -m "%s.odp" *; mv "%s.odp" ..' % (nome,nome))

os.chdir('..')
os.system('libreoffice --convert-to pdf *.odp')

