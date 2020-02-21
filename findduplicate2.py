#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os, sys, hashlib

print 'Procurando por duplicatas...'

dir = sys.argv[1]
dirb = sys.argv[2]

r={}

def filegetmd5(pasta):
	os.chdir(pasta)
	lista = os.listdir('.')
	for i in lista:
		result = os.system('test -d "%s"' % i)
		if result == 0:
			print 'Acessando diretório "%s"' % i
			filegetmd5(i)
		else:
			#Reconhecendo e adicionando
			f = open(i, 'r')
			filedata = f.read()
			f.close()
			filedata = hashlib.new('md5', filedata)
			filedata = filedata.digest()
			#print filedata
			filelocation = os.getcwd() + '/' + i
			#print filelocation
			if r.has_key(filedata):
				print '"%s" é uma duplicata de "%s"?' % (filelocation,r[filedata])
			else:
				r[filedata] = filelocation
	os.chdir('..')
	#print r

filegetmd5(dir)
filegetmd5(dirb)

