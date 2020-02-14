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

from modules.functools import check_item_list
from collections import OrderedDict

def create_players_db():
	db = OrderedDict()
	db['Protagonistas'] = OrderedDict()
	db['Antagonistas'] = OrderedDict()
	db['Extras'] = OrderedDict()
	return db

def create_trama_db():
	db = OrderedDict()
	db['Tramas'] = OrderedDict()
	db['Cenas'] = OrderedDict()
	return db



def verificar_tipo_de_info(info_nome):
	if check_item_list(info_nome, ['Tipo de personagem', 'Metatipo', 'Profissão', 'Personalidade', 'Moralidade', 'Sexo']):
		return "Fechada"
	else:
		return "Aberta"



def verificar_tipo_de_atributo(info_nome):
	if check_item_list(info_nome, ['Força', 'Destreza', 'Agilidade', 'Vigor']):
		return "Físico"
	elif check_item_list(info_nome, ['Presença', 'Manipulação', 'Compostura']):
		return "Social"
	else:
		return "Mental"



def verificar_tipo_de_habilidade(info_nome):
	if check_item_list(info_nome, ['Armas brancas', 'Armas de projétil', 'Briga', 'Condução', 'Dissimulação', 'Esportes', 'Furto', 'Sobrevivência']):
		return "Físico"
	elif check_item_list(info_nome, ['Astúcia', 'Empatia', 'Expressão', 'Intimidação', 'Manha', 'Persuasão', 'Socialização', 'Trato com animais']):
		return "Social"
	else:
		return "Mental"

