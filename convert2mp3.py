#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#
#  Copyright 2017 Daniel Cruz <bwb0de@bwb0dePC>
#  Version 0.1
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#  Dependências:
#  Esse script usa os pacotes: vorbis-tools, lame, flac, mplayer, ffmpeg
#

import argparse
from os import system as sh
from os import linesep as nl
from os import sep
from os import listdir as ls
from subprocess import check_output as sh2
from os import walk, path, remove, getcwd, chdir

script_nfo="""
Script de clonagem de diretórios e arquivos...
"""

parser = argparse.ArgumentParser(description=script_nfo)
parser.add_argument("alvo", help="defina o diretório que possui os arquivos a serem convertidos...")
parser.add_argument("-f", help="defina o formato de saída: ogg ou mp3...")
args = parser.parse_args()
basedir = getcwd()


def main():
	if args.f == 'mp3':
		for root, dirs, files in walk(args.alvo):
			for f in files:
				fname = path.join(basedir, path.join(root, f))
				if f.find(".wma") != -1:
					new_file=fname.replace('.wma','.mp3')
					sh('mplayer -vo null -vc dummy -af resample=44100 -ao pcm:waveheader "{f}" && lame -m s audiodump.wav -o "{new}"; rm audiodump.wav'.format(f=fname, new=new_file))
				elif f.find(".wav") != -1:
					new_file=fname.replace('.wav','.mp3')
					sh('lame -b 128 "{f}" "{new}"'.format(f=fname, new=new_file))
				elif f.find(".ogg") != -1:
					new_file=fname.replace('.ogg','.mp3')
					transit=fname.replace('.ogg','.wav')
					sh('oggdec "{f}"; lame -b 128 "{transit}" "{new}"; rm "{transit}";'.format(f=fname, transit=transit, new=new_file))
				elif f.find(".flac") != -1:
					new_file=fname.replace('.flac','.mp3')
					sh('flac -cd "{f}" | lame -b 128 -h - "{new}";'.format(f=fname, new=new_file))
				elif f.find(".ape") != -1:
					new_file=fname.replace('.ape','.mp3')
					sh('ffmpeg -ab 128 -i "{f}" "{new}";'.format(f=fname, new=new_file))
				elif f.find(".amr") != -1:
					new_file=fname.replace('.amr','.mp3')
					sh('ffmpeg -ab 128 -i "{f}" -ar 441000 "{new}";'.format(f=fname, new=new_file))
				elif f.find(".mp4") != -1:
					new_file=fname.replace('.mp4','.mp3')
					sh('ffmpeg -i {f} -vn -acodec libmp3lame {new} -n -loglevel quiet'.format(f=fname, new=new_file))	
				elif f.find(".webm") != -1:
					new_file=fname.replace('.webm','.mp3')
					sh('ffmpeg -i {f} -vn -acodec libmp3lame {new} -n -loglevel quiet'.format(f=fname, new=new_file))	
	elif args.f == 'ogg':
		for root, dirs, files in walk(args.alvo):
			for f in files:
				fname = path.join(basedir, path.join(root, f))
				if f.find(".wma") != -1:
					new_file=fname.replace('.wma','.ogg')
					sh('ffmpeg -i "{f}" -acodec libvorbis "{new}"'.format(f=fname, new=new_file))	
				elif f.find(".wav") != -1:
					new_file=fname.replace('.wav','.ogg')
					sh('ffmpeg -i "{f}" -acodec libvorbis "{new}"'.format(f=fname, new=new_file))
				elif f.find(".flac") != -1:
					new_file=fname.replace('.flac','.ogg')
					sh('flac -cd "{f}" | lame -b 128 -h - "{new}";'.format(f=fname, new=new_file))
				elif f.find(".ape") != -1:
					new_file=fname.replace('.ape','.ogg')
					sh('ffmpeg -i {f} -vn -acodec libvorbis {new} -n -loglevel quiet'.format(f=fname, new=new_file))	
				elif f.find(".amr") != -1:
					new_file=fname.replace('.amr','.ogg')
					sh('ffmpeg -i {f} -vn -acodec libvorbis {new} -n -loglevel quiet'.format(f=fname, new=new_file))	
				elif f.find(".mp4") != -1:
					new_file=fname.replace('.mp4','.ogg')
					sh('ffmpeg -i {f} -vn -acodec libvorbis {new} -n -loglevel quiet'.format(f=fname, new=new_file))	
				elif f.find(".webm") != -1:
					new_file=fname.replace('.webm','.ogg')
					sh('ffmpeg -i {f} -vn -acodec libvorbis {new} -n -loglevel quiet'.format(f=fname, new=new_file))	
	else:
		print("Formato de saída não suportado pelo script...")
	return 0

if __name__ == '__main__':
	main()


