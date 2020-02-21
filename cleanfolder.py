#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Reescrever em shellscript usando find...
#
import os, sys, shutil

print 'Procurando por arquivos "desktop.ini" e "thumbs.db" para excluí-los...'
st=os.getcwd()

def filegetmd5(pasta):
	os.chdir(pasta)
	lista = os.listdir('.')
	for i in lista:
		result = os.system('test -d "%s"' % i)
		if result == 0:
			print 'Acessando diretório "%s"' % i
			filegetmd5(i)
		else:
			#Executando gatilho de conversão...
			try:
				if i.find("desktop.ini") != -1:
					os.remove(i)
				elif i.find("thumbs.db") != -1:
					os.remove(i)
				elif i.find(".url") != -1:
					os.remove(i)

			except:
				pass
	os.chdir('..')
	#print r

filegetmd5(sys.argv[1])
