#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#
#  Copyright 2017 Daniel Cruz <bwb0de@bwb0dePC>
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

import argparse
from os import system as sh
from os import linesep as nl
from os import listdir as ls
from subprocess import check_output as sh2

script_nfo="""
Armazena os arquivos da pasta selecionada em ISOs conforme o tamanho máximo estipulado por iso..."""

parser = argparse.ArgumentParser(description=script_nfo)
parser.add_argument("folder", help="seleciona a pasta alvo onde os arquivos da ISO estarão")
parser.add_argument("maxsize", help="define o tamanho máximo de cada ISO em MB")
args = parser.parse_args()


def create_config_files():
	try: sh("mkdir ~/.mkbk 2> /dev/null; touch ~/.mkbk/backup_folders; touch ~/.mkbk/target_folder")
	except: pass

def purge_config_files():
	sh("rm -fR ~/.mkbk")
	create_config_files()

def insert_into_sources(insert_folder):
	sh("echo '{}' >> ~/.mkbk/backup_folders".format(insert_folder))

def set_target_folder(insert_folder):
	sh("echo '{}' > ~/.mkbk/target_folder".format(insert_folder))

def main(args):
	if (check_item_list('run', args) or check_item_list('purge', args) or check_item_list('config', args) or check_item_list('view', args)) == False:
		print("Ação desconhecida... Digite a opção '-h' para obter ajuda.")
		return 1

	if check_item_list('config', args):
		if check_item_list('-i', args):
			new_folder = args[args.index("-i") + 1]
			insert_into_sources(new_folder)

		if check_item_list('--insert-dir', args):
			new_folder = args[args.index("--insert-dir") + 1]
			insert_into_sources(new_folder)

		if check_item_list('-t', args):
			new_folder = args[args.index("-t") + 1]
			set_target_folder(new_folder)

		if check_item_list('--set-target-dir', args):
			new_folder = args[args.index("--set-target-dir") + 1]
			set_target_folder(new_folder)

	if check_item_list('view', args):
		sh("echo 'Diretórios de backup listados:'")
		sh("cat < ~/.mkbk/backup_folders")
		sh("echo ''")
		sh("echo 'Diretório de destino listado:'")
		sh("cat < ~/.mkbk/target_folder")
		sh("echo ''")

	if check_item_list('purge', args):
		purge_config_files()

	return 0

if __name__ == '__main__':
	main()
