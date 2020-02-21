#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os, sys

print 'Taggeando...'
dir = sys.argv[1]
tag = sys.argv[2]

def addtag2pic(pasta, tag):
	os.chdir(pasta)
	lista = os.listdir('.')
	for i in lista:
		result = os.system('test -d "%s"' % i)
		if result == 0:
			print 'Acessando diretório "%s"' % i
			addtag2pic(i, tag)
		else:
			#Reconhecendo e adicionando
			if i.find('.jpg') != -1:
				os.system('exiftool -keywords+=%s "%s" >> /dev/null' % (tag, i))
				file = i + '_original'
				os.remove(file)
			if i.find('.JPG') != -1:
				os.system('exiftool -keywords+=%s "%s" >> /dev/null' % (tag, i))
				file = i + '_original'
				os.remove(file)
			if i.find('.Jpg') != -1:
				os.system('exiftool -keywords+=%s "%s" >> /dev/null' % (tag, i))
				file = i + '_original'
				os.remove(file)
			'''if i.find('.bmp') != -1:
				os.system('exiftool -keywords+=%s "%s"' % (tag, i))
				file = i + '_original'
				os.remove(file)
			if i.find('.BMP') != -1:
				os.system('exiftool -keywords+=%s "%s"' % (tag, i))
				file = i + '_original'
				os.remove(file)
			if i.find('.png') != -1:
				os.system('exiftool -keywords+=%s "%s"' % (tag, i))
				file = i + '_original'
				os.remove(file)
			if i.find('.PNG') != -1:
				os.system('exiftool -keywords+=%s "%s"' % (tag, i))
				file = i + '_original'
				os.remove(file)'''
			if i.find('.ini') != -1:
				os.remove(i)
			
			if i.find('ws_ftp.log') != -1:
				os.remove(i)
				
			if i.find('.thm') != -1:
				os.remove(i)
				
			if i.find('.THM') != -1:
				os.remove(i)
				
	os.chdir('..')

addtag2pic(dir, tag)
