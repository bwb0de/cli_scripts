#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#
#  Copyright 2017 Daniel Cruz <bwb0de@bwb0dePC>
#  bwb0de Functools Version 0.1
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
#


from collections import OrderedDict
from sys import platform
from os import linesep
from os import path
from os import system as sh
from os import listdir as ls
from subprocess import check_output as sh2

from colored import fg, bg, attr

def vermelho(string):
	return "{}{}{}".format(fg(1), string, attr(0))

def azul_claro(string):
	return "{}{}{}".format(fg(12), string, attr(0))

def verde(string):
	return "{}{}{}".format(fg(2), string, attr(0))

def amarelo(string):
	return "{}{}{}".format(fg(3), string, attr(0))

def rosa(string):
	return "{}{}{}".format(fg(5), string, attr(0))




def edit_textfield(nome, nfo=None):
	if nfo != None:
		f = open('/tmp/siur_textfield', 'w')
		f.write(str(nfo))
		f.close()
		sh("nano /tmp/siur_textfield")
		return sh2("cat /tmp/siur_textfield", shell=True).decode('utf-8')
	else:
		sh("echo '{}' > /tmp/siur_textfield; nano /tmp/siur_textfield".format(nome))
		return sh2("cat /tmp/siur_textfield", shell=True).decode('utf-8')




def make_event_order(lista=None):
	if lista != None:
		lista.sort()
		lista.reverse()
		eventos = OrderedDict()
		for i in lista:
			eventos[i] = []
		return eventos
	ev = [idx for idx in range(0,30)]
	eventos = OrderedDict()
	ev.reverse()
	for i in ev:
		eventos[i] = []
	return eventos








def copiar_lista(lista):
	output = []
	for i in lista:
		output.append(i)
	return output













