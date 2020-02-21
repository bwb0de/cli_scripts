#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os, sys, hashlib, shutil

print 'Procurando por duplicatas...'

st=os.getcwd()

r={}

mplayer -vo null -vc dummy -af resample=44100 -ao pcm:waveheader %s && lame -m s audiodump.wav -o %s.mp3

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
			try:
				if i.find(".wma"):
					os.system('mplayer -vo null -vc dummy -af resample=44100 -ao pcm:waveheader "%s" && lame -m s audiodump.wav -o "%s.mp3"; rm audiodump.wav; mv "%s" "/home/bwb0de/%s"' % (i,i.replace('.wma',''),i,i))
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
					shutil.move(filelocation, str("/home/findDUP/"+i))
				else:
					r[filedata] = filelocation
			except:
				pass
	os.chdir('..')
	#print r

filegetmd5(sys.argv[1])
os.chdir(st)
try:
	filegetmd5(sys.argv[2])
	os.chdir('/home/findDUP/')
	f=open('findDUP.py','w')
	f.write('r='+str(r))
	f.close()
except:
	os.chdir('/home/findDUP/')
	f=open('findDUP.py','w')
	f.write('r='+str(r))
	f.close()
