#!/bin/bash
# -*- coding: utf-8 -*-
#
#  copy2workdesk.sh
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

clear
echo "Este aplicativo cria hardlinks a partir de uma árvore de diretórios alvo."
echo ""
echo
echo
echo
echo
echo
echo

echo "Selecione a pasta de destino"

find /home/bwb0de/Imagens/ -type f -iname "*" -exec ln {} /home/bwb0de/Work2Do_Fotos/ \;


