#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os, sys

print 'Renomeando...'
dir = sys.argv[1]
all_files = {}

def rename2date(pasta):
	os.chdir(pasta)
	lista = os.listdir(os.curdir)
	for i in lista:
		command = os.popen('if test -d "%s"; then echo "True"; else echo "False";fi' % (i))
		command_output = command.read().replace(os.linesep,'')
		if command_output == 'True':
			print 'Acessando diretório "%s"' % i
			rename2date(i)
		else:
			if i.find('.jpg') != -1:
				command = os.popen('exiftool "%s" | grep "Create Date" | sed "s/ //g"' % (i))
				command_output = command.read().replace(os.linesep,'').split(':')
				if command_output[1] == '0000':
					print "Ignorando arquivo %s, exif data é 0000." % i
				elif command_output[1] == '':
					print "Ignorando arquivo %s, não possui dados exif relativos a data de criação." % i
				else:
					newname = command_output[1] + command_output[2] + command_output[3] + command_output[4] + command_output[5] + command_output[6] + '.jpg'
					if all_files.has_key(newname):
						print "Ignorando arquivo %s, pois um arquivo já recebeu esse nome." % i
					else:
						all_files[newname] = 1
						command = os.popen('mv "%s" "%s"' % (i, newname))
	os.chdir(os.pardir)

rename2date(dir)
