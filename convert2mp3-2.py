#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os, sys, shutil

print 'Procurando por arquivos de som não-mp3...'
st=os.getcwd()

#Esse script usa os pacotes: vorbis-tools, lame, flac, mplayer, ffmpeg

#mplayer -vo null -vc dummy -af resample=44100 -ao pcm:waveheader %s && lame -m s audiodump.wav -o %s.mp3

#Diretório de destino dos arquivos antigos...
#Deve ser um caminho absoluto e deve terminar com '/'...
fd='/home/bwb0de/'

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
				if i.find(".wma") != -1:
					new=i.replace('.wma','.mp3')
					os.system('mplayer -vo null -vc dummy -af resample=44100 -ao pcm:waveheader "%s" && lame -m s audiodump.wav -o "%s"; rm audiodump.wav; mv "%s" "%s%s"' % (i,new,i,fd,i))
				elif i.find(".wav") != -1:
					new=i.replace('.wav','.mp3')
					os.system('lame -b 192 "%s" "%s"; mv "%s" "%s%s"' % (i,new,i,fd,i))
				elif i.find(".ogg") != -1:
					new=i.replace('.ogg','.mp3')
					transit=i.replace('.ogg','.wav')
					os.system('oggdec "%s"; lame -b 192 "%s" "%s"; rm "%s"; mv "%s" "%s%s"' % (i,transit,new,transit,i,fd,i))
				elif i.find(".flac") != -1:
					new=i.replace('.flac','.mp3')
					os.system('flac -cd "%s" | lame -b 192 -h - "%s"; mv "%s" "%s%s"' % (i,new,i,fd,i))
				elif i.find(".ape") != -1:
					new=i.replace('.ape','.mp3')
					os.system('ffmpeg -ab 192 -i "%s" "%s"; mv "%s" "%s%s"' % (i,new,i,fd,i))
				elif i.find(".amr") != -1:
					new=i.replace('.amr','.mp3')
					os.system('ffmpeg -ab 192 -i "%s" -ar 441000 "%s"; mv "%s" "%s%s' % (i,new,i,fd,i))

			except:
				pass
	os.chdir('..')
	#print r

filegetmd5(sys.argv[1])
