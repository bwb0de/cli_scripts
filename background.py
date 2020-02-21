#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os, random

background = '/home/bwb0de/.background'
backgrounds = os.listdir(background)

os.chdir(background)
size = len(backgrounds)
while True:
	foto = random.randint(0,size-1)
	# Is there a background set?
	files = os.listdir('../')
	files = str(files)
	result = files.find('.backgroundpic')
	if result != -1: os.remove('../.backgroundpic')
	os.link(backgrounds[foto], '../.backgroundpic')
	os.system('sleep 30s')

