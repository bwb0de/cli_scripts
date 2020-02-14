#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#
#  Copyright 2017 Daniel Cruz <bwb0de@bwb0dePC>
#  Tabelas SiUR Version 0.1
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


from modules.paths import app_root_folder
from modules.functools import read_pickle
from collections import OrderedDict
from os import linesep


class Equipamentos:
	def __init__(self, nome, tipo, tipo_dano, dano_adicional, distancia, tempo_preparacao, tempo_ataque, modificador_de_uso, valor_de_mercado, peso, forca_minima, obs, rd, hp, habilidade_base=None):
		self.nome = nome
		self.tipo = tipo
		self.tipo_dano = tipo_dano
		self.dano_contundente = True
		self.dano_letal = False
		self.dano_agravado = False
		self.dano_adicional = dano_adicional
		self.distancia = distancia
		self.tempo_preparacao = tempo_preparacao
		self.tempo_ataque = tempo_ataque
		self.modificador_de_uso = modificador_de_uso
		self.valor_de_mercado = valor_de_mercado
		self.peso = peso
		self.peso_unitario = peso
		self.forca_minima = forca_minima
		self.obs = obs
		self.rd = rd
		self.hp = hp
		self.quantidade = 1
		self.em_uso = False
		self.arremessavel = False
		self.habilidade_base = habilidade_base
		self.preparada = False


equipamentos = OrderedDict()
equipamentos['Soco inglês'] = Equipamentos('Soco inglês', 'Arma', 'Contusão', '---', 'Corpo-a-corpo', 0, 2, 0, 10, 0.125, 2, 'Impede danos nas mãos mediante falha.', 4, 25, "Briga")
equipamentos['Faca'] = Equipamentos('Faca', 'Arma', 'Corte e perfuração', '---', 'Curta', 0, 2, 0, 30, 0.25, 2, 'Arremessável.', 4, 20, "Armas brancas")
equipamentos['Facão'] = Equipamentos('Facão', 'Arma', 'Corte e perfuração', '2D6[‡7]', 'Curta', 0, 2, 0, 40, 0.25, 3, 'Arremessável.', 3, 20, "Armas brancas")
equipamentos['Adaga'] = Equipamentos('Adaga', 'Arma', 'Perfuração', '2D6[‡7]', 'Curta', 0, 2, 0, 20, 0.125, 2, 'Arremessável.', 4, 30, "Armas brancas")
equipamentos['Estaca de madeira'] = Equipamentos('Estaca de madeira', 'Arma', 'Perfuração', '---', 'Curta', 0, 2, 0, 4, 0.25, 2, '', 2, 15, "Armas brancas")
equipamentos['Espada de lâmina larga'] = Equipamentos('Espada de lâmina larga', 'Arma', 'Contusão, corte, perfuração', '2D6[‡8]', 'Média', 0, 4, 1, 500, 1.5, 5, '', 5, 70, "Armas brancas")
equipamentos['Espada bastarda'] = Equipamentos('Espada bastarda', 'Arma', 'Contusão, corte, perfuração', '2D6[‡9]', 'Média', 0, 4, 1, 650, 2.5, 5, 'Recebe +1 em dano de perfuração.', 4, 70, "Armas brancas")
equipamentos['Sabre de cavalaria'] = Equipamentos('Sabre de cavalaria', 'Arma', 'Contusão, corte, perfuração', '2D6[‡8]', 'Média', 0, 4, 1, 500, 1.5, 5, 'Possui proteção para a mão. Dano de contusõa é igual ao dano base.', 4, 70, "Armas brancas")
equipamentos['Gládio'] = Equipamentos('Gládio', 'Arma', 'Contusão, corte, perfuração', '2D6[‡7]', 'Curta', 0, 3, 0, 400, 1, 4, 'Recebe +1 em dano de perfuração.', 4, 65, "Armas brancas")
equipamentos['Bastão'] = Equipamentos('Bastão', 'Arma', 'Contusão', '2D6[‡8]', 'Longa', 0, 3, 1, 10, 2, 3, 'Demanda uso das duas mãos.', 3, 30, "Armas brancas")
equipamentos['Lança'] = Equipamentos('Lança', 'Arma', 'Contusão e perfuração', '2D6[‡8]', 'Longa', 0, 3, 1, 40, 2, 4, 'Demanda uso das duas mãos.', (3,4), (30, 40), "Armas brancas")
equipamentos['Arco composto'] = Equipamentos('Arco composto', 'Arma', 'Perfuração', '2D6[‡9]', '40 80 120', (4, 3, 3), 1, 0, 300, 0.75, 6, '', 3, 40, "Armas de projétil")
equipamentos['Escudo grande híbrido (madeira e metal)'] = Equipamentos('Escudo grande híbrido (madeira e metal)', 'Arma', 'Contusão', '2D6[‡10]*', 'Curta', 4, 3, 0, 300, 7, 6, 'Dano base se estiver lutando em pé. Dano ampliado só aplica-se quando golpe desferido com a borda do escudo com oponente no chão.', 4, 100, "Armas brancas")

equipamentos['Cota de malha'] = Equipamentos('Cota de malha', 'Veste', '---', '---', '---', 0, 0, 0, 1200, 8, 6, '', 4, 50)
equipamentos['Armadura de placas'] = Equipamentos('Armadura de placas', 'Veste', '---', '---', '---', 0, 0, 0, 1200, 17, 6, '', 4, 70)
equipamentos['Couraça'] = Equipamentos('Cota de malha', 'Veste', '---', '---', '---', 0, 0, 0, 700, 8, 6, '', 4, 50)
equipamentos['Túnica'] = Equipamentos('Túnica', 'Veste', '---', '---', '---', 0, 0, 0, 30, 8, 6, '', 4, 50)
equipamentos['Botas'] = Equipamentos('Botas', 'Veste', '---', '---', '---', 0, 0, 0, 25, 0.5, 3, '', 3, 25)

equipamentos['Cota de malha'].blindagem = 2
equipamentos['Armadura de placas'].blindagem = 2
equipamentos['Couraça'].blindagem = 1
equipamentos['Túnica'].blindagem = 1
equipamentos['Botas'].blindagem = 1

equipamentos['Moedas'] = Equipamentos('Moedas', 'Dinheiro', '---', '---', '---', 0, 0, 0, 25, 0.05, 3, '', 3, 25)

equipamentos['Ervas, raízes medicinais [antinflamatória]'] = Equipamentos('Ervas, raízes medicinais [antinflamatória]', 'Ervas', '---', '---', '---', 0, 0, 0, 25, 0.05, 3, '', 3, 25)
equipamentos['Ervas, raízes medicinais [antiseptica/antibiótica]'] = Equipamentos('Ervas, raízes medicinais [antiseptica/antibiótica]', 'Ervas', '---', '---', '---', 0, 0, 0, 25, 0.05, 3, '', 3, 25)
equipamentos['Ervas, raízes medicinais [analgésica]'] = Equipamentos('Ervas, raízes medicinais [analgésica]', 'Ervas', '---', '---', '---', 0, 0, 0, 25, 0.05, 3, '', 3, 25)
equipamentos['Ervas, raízes medicinais [cicatrizante]'] = Equipamentos('Ervas, raízes medicinais [cicatrizante]', 'Ervas', '---', '---', '---', 0, 0, 0, 25, 0.05, 3, '', 3, 25)
equipamentos['Ervas, raízes medicinais [estimulante]'] = Equipamentos('Ervas, raízes medicinais [estimulante]', 'Ervas', '---', '---', '---', 0, 0, 0, 25, 0.05, 3, '', 3, 25)
equipamentos['Ervas, raízes medicinais [relaxante]'] = Equipamentos('Ervas, raízes medicinais [relaxante]', 'Ervas', '---', '---', '---', 0, 0, 0, 25, 0.05, 3, '', 3, 25)

equipamentos['Pão'] = Equipamentos('Pão', 'Alimentos', '---', '---', '---', 0, 0, 0, 25, 0.05, 3, '', 3, 25)
equipamentos['Queijo'] = Equipamentos('Queijo', 'Alimentos', '---', '---', '---', 0, 0, 0, 25, 0.05, 3, '', 3, 25)
equipamentos['Vinho'] = Equipamentos('Vinho', 'Alimentos', '---', '---', '---', 0, 0, 0, 25, 0.05, 3, '', 3, 25)
equipamentos['Cerveja'] = Equipamentos('Cerveja', 'Alimentos', '---', '---', '---', 0, 0, 0, 25, 0.05, 3, '', 3, 25)
equipamentos['Corda'] = Equipamentos('Corda', 'Alimentos', '---', '---', '---', 0, 0, 0, 25, 0.05, 3, '', 3, 25)


moralidade = OrderedDict()
moralidade['Bondoso'] = 5
moralidade['Justo'] = 4
moralidade['Vingativo'] = 3
moralidade['Maquiavélico'] = 2
moralidade['Selvagem'] = 1
moralidade['Cruel'] = 0

metatipo = OrderedDict()
metatipo['Humano'] = {'Força': 0, 'Agilidade': 0, 'Destreza': 0, 'Vigor': 0, 'Presença': 0, 'Manipulação': 0, 'Compostura': 0, 'Inteligência': 0, 'Sagacidade': 0, 'Raciocínio': 0, 'Determinação': 0}
metatipo['Vampiro'] = {'Força': 0, 'Agilidade': 0, 'Destreza': 0, 'Vigor': 0, 'Presença': 0, 'Manipulação': 0, 'Compostura': 0, 'Inteligência': 0, 'Sagacidade': 0, 'Raciocínio': 0, 'Determinação': 0}
metatipo['Fada'] = {'Força': 0, 'Agilidade': 0, 'Destreza': 0, 'Vigor': 0, 'Presença': 0, 'Manipulação': 0, 'Compostura': 0, 'Inteligência': 0, 'Sagacidade': 0, 'Raciocínio': 0, 'Determinação': 0}
metatipo['Lobisomem'] = {'Força': 0, 'Agilidade': 0, 'Destreza': 0, 'Vigor': 0, 'Presença': 0, 'Manipulação': 0, 'Compostura': 0, 'Inteligência': 0, 'Sagacidade': 0, 'Raciocínio': 0, 'Determinação': 0}
metatipo['Elfo'] = {'Força': 0, 'Agilidade': 0, 'Destreza': 0, 'Vigor': 0, 'Presença': 0, 'Manipulação': 0, 'Compostura': 0, 'Inteligência': 0, 'Sagacidade': 0, 'Raciocínio': 0, 'Determinação': 0}
metatipo['Hafling'] = {'Força': 0, 'Agilidade': 0, 'Destreza': 0, 'Vigor': 0, 'Presença': 0, 'Manipulação': 0, 'Compostura': 0, 'Inteligência': 0, 'Sagacidade': 0, 'Raciocínio': 0, 'Determinação': 0}
metatipo['Anão'] = {'Força': 0, 'Agilidade': 0, 'Destreza': 0, 'Vigor': 0, 'Presença': 0, 'Manipulação': 0, 'Compostura': 0, 'Inteligência': 0, 'Sagacidade': 0, 'Raciocínio': 0, 'Determinação': 0}

profissao = OrderedDict()
profissao['Sacerdotes'] = {'Força': 0, 'Agilidade': 0, 'Destreza': 0, 'Vigor': 0, 'Presença': 0, 'Manipulação': 0, 'Compostura': 0, 'Inteligência': 0, 'Sagacidade': 0, 'Raciocínio': 0, 'Determinação': 0}
profissao["Cavaleiros templários"] = {'Força': 2, 'Agilidade': 2, 'Destreza': 1, 'Vigor': 3, 'Presença': 2, 'Manipulação': 1, 'Compostura': 2, 'Inteligência': 3, 'Sagacidade': 2, 'Raciocínio': 2, 'Determinação': 2}
profissao["Soldado de infantaria"] = {'Força': 3, 'Agilidade': 2, 'Destreza': 1, 'Vigor': 3, 'Presença': 2, 'Manipulação': 1, 'Compostura': 2, 'Inteligência': 2, 'Sagacidade': 2, 'Raciocínio': 1, 'Determinação': 2}
profissao["Soldado de suporte"] = {'Força': 0, 'Agilidade': 0, 'Destreza': 0, 'Vigor': 0, 'Presença': 0, 'Manipulação': 0, 'Compostura': 0, 'Inteligência': 0, 'Sagacidade': 0, 'Raciocínio': 0, 'Determinação': 0}
profissao["Soldado de infantaria pesada"] = {'Força': 0, 'Agilidade': 0, 'Destreza': 0, 'Vigor': 0, 'Presença': 0, 'Manipulação': 0, 'Compostura': 0, 'Inteligência': 0, 'Sagacidade': 0, 'Raciocínio': 0, 'Determinação': 0}
profissao["Marinheiro"] = {'Força': 0, 'Agilidade': 0, 'Destreza': 0, 'Vigor': 0, 'Presença': 0, 'Manipulação': 0, 'Compostura': 0, 'Inteligência': 0, 'Sagacidade': 0, 'Raciocínio': 0, 'Determinação': 0}
profissao["Agente de segurança privada"] = {'Força': 0, 'Agilidade': 0, 'Destreza': 0, 'Vigor': 0, 'Presença': 0, 'Manipulação': 0, 'Compostura': 0, 'Inteligência': 0, 'Sagacidade': 0, 'Raciocínio': 0, 'Determinação': 0}
profissao["Policial"] = {'Força': 0, 'Agilidade': 0, 'Destreza': 0, 'Vigor': 0, 'Presença': 0, 'Manipulação': 0, 'Compostura': 0, 'Inteligência': 0, 'Sagacidade': 0, 'Raciocínio': 0, 'Determinação': 0}
profissao["Detetive"] = {'Força': 0, 'Agilidade': 0, 'Destreza': 0, 'Vigor': 0, 'Presença': 0, 'Manipulação': 0, 'Compostura': 0, 'Inteligência': 0, 'Sagacidade': 0, 'Raciocínio': 0, 'Determinação': 0}
profissao["Piloto"] = {'Força': 0, 'Agilidade': 0, 'Destreza': 0, 'Vigor': 0, 'Presença': 0, 'Manipulação': 0, 'Compostura': 0, 'Inteligência': 0, 'Sagacidade': 0, 'Raciocínio': 0, 'Determinação': 0}
profissao["Médico"] = {'Força': 0, 'Agilidade': 0, 'Destreza': 0, 'Vigor': 0, 'Presença': 0, 'Manipulação': 0, 'Compostura': 0, 'Inteligência': 0, 'Sagacidade': 0, 'Raciocínio': 0, 'Determinação': 0}
profissao["Curandeiro"] = {'Força': 1, 'Agilidade': 2, 'Destreza': 2, 'Vigor': 2, 'Presença': 2, 'Manipulação': 1, 'Compostura': 3, 'Inteligência': 3, 'Sagacidade': 2, 'Raciocínio': 2, 'Determinação': 2}
profissao["Cozinheiro"] = {'Força': 0, 'Agilidade': 0, 'Destreza': 0, 'Vigor': 0, 'Presença': 0, 'Manipulação': 0, 'Compostura': 0, 'Inteligência': 0, 'Sagacidade': 0, 'Raciocínio': 0, 'Determinação': 0}
profissao["Treinador animais"] = {'Força': 0, 'Agilidade': 0, 'Destreza': 0, 'Vigor': 0, 'Presença': 0, 'Manipulação': 0, 'Compostura': 0, 'Inteligência': 0, 'Sagacidade': 0, 'Raciocínio': 0, 'Determinação': 0}
profissao["Professor"] = {'Força': 0, 'Agilidade': 0, 'Destreza': 0, 'Vigor': 0, 'Presença': 0, 'Manipulação': 0, 'Compostura': 0, 'Inteligência': 0, 'Sagacidade': 0, 'Raciocínio': 0, 'Determinação': 0}
profissao["Político"] = {'Força': 0, 'Agilidade': 0, 'Destreza': 0, 'Vigor': 0, 'Presença': 0, 'Manipulação': 0, 'Compostura': 0, 'Inteligência': 0, 'Sagacidade': 0, 'Raciocínio': 0, 'Determinação': 0}
profissao["Oleiro"] = {'Força': 0, 'Agilidade': 0, 'Destreza': 0, 'Vigor': 0, 'Presença': 0, 'Manipulação': 0, 'Compostura': 0, 'Inteligência': 0, 'Sagacidade': 0, 'Raciocínio': 0, 'Determinação': 0}
profissao["Tecelão"] = {'Força': 0, 'Agilidade': 0, 'Destreza': 0, 'Vigor': 0, 'Presença': 0, 'Manipulação': 0, 'Compostura': 0, 'Inteligência': 0, 'Sagacidade': 0, 'Raciocínio': 0, 'Determinação': 0}
profissao["Coureiro"] = {'Força': 0, 'Agilidade': 0, 'Destreza': 0, 'Vigor': 0, 'Presença': 0, 'Manipulação': 0, 'Compostura': 0, 'Inteligência': 0, 'Sagacidade': 0, 'Raciocínio': 0, 'Determinação': 0}
profissao["Ferreiro"] = {'Força': 0, 'Agilidade': 0, 'Destreza': 0, 'Vigor': 0, 'Presença': 0, 'Manipulação': 0, 'Compostura': 0, 'Inteligência': 0, 'Sagacidade': 0, 'Raciocínio': 0, 'Determinação': 0}
profissao["Armeiro"] = {'Força': 0, 'Agilidade': 0, 'Destreza': 0, 'Vigor': 0, 'Presença': 0, 'Manipulação': 0, 'Compostura': 0, 'Inteligência': 0, 'Sagacidade': 0, 'Raciocínio': 0, 'Determinação': 0}
profissao["Marceneiro"] = {'Força': 0, 'Agilidade': 0, 'Destreza': 0, 'Vigor': 0, 'Presença': 0, 'Manipulação': 0, 'Compostura': 0, 'Inteligência': 0, 'Sagacidade': 0, 'Raciocínio': 0, 'Determinação': 0}
profissao["Mercador"] = {'Força': 2, 'Agilidade': 1, 'Destreza': 1, 'Vigor': 2, 'Presença': 2, 'Manipulação': 3, 'Compostura': 1, 'Inteligência': 2, 'Sagacidade': 3, 'Raciocínio': 2, 'Determinação': 2}
profissao["Proprietário de terras"] = {'Força': 0, 'Agilidade': 0, 'Destreza': 0, 'Vigor': 0, 'Presença': 0, 'Manipulação': 0, 'Compostura': 0, 'Inteligência': 0, 'Sagacidade': 0, 'Raciocínio': 0, 'Determinação': 0}
profissao["Burocrata"] = {'Força': 0, 'Agilidade': 0, 'Destreza': 0, 'Vigor': 0, 'Presença': 0, 'Manipulação': 0, 'Compostura': 0, 'Inteligência': 0, 'Sagacidade': 0, 'Raciocínio': 0, 'Determinação': 0}
profissao["Mercenário"] = {'Força': 0, 'Agilidade': 0, 'Destreza': 0, 'Vigor': 0, 'Presença': 0, 'Manipulação': 0, 'Compostura': 0, 'Inteligência': 0, 'Sagacidade': 0, 'Raciocínio': 0, 'Determinação': 0}
profissao["Escudeiro"] = {'Força': 0, 'Agilidade': 0, 'Destreza': 0, 'Vigor': 0, 'Presença': 0, 'Manipulação': 0, 'Compostura': 0, 'Inteligência': 0, 'Sagacidade': 0, 'Raciocínio': 0, 'Determinação': 0}
profissao["Agricultor"] = {'Força': 0, 'Agilidade': 0, 'Destreza': 0, 'Vigor': 0, 'Presença': 0, 'Manipulação': 0, 'Compostura': 0, 'Inteligência': 0, 'Sagacidade': 0, 'Raciocínio': 0, 'Determinação': 0}
profissao["Artista plástico"] = {'Força': 0, 'Agilidade': 0, 'Destreza': 0, 'Vigor': 0, 'Presença': 0, 'Manipulação': 0, 'Compostura': 0, 'Inteligência': 0, 'Sagacidade': 0, 'Raciocínio': 0, 'Determinação': 0}
profissao["Músico"] = {'Força': 0, 'Agilidade': 0, 'Destreza': 0, 'Vigor': 0, 'Presença': 0, 'Manipulação': 0, 'Compostura': 0, 'Inteligência': 0, 'Sagacidade': 0, 'Raciocínio': 0, 'Determinação': 0}
profissao["Artista marcial"] = {'Força': 2, 'Agilidade': 2, 'Destreza': 3, 'Vigor': 3, 'Presença': 2, 'Manipulação': 1, 'Compostura': 2, 'Inteligência': 1, 'Sagacidade': 2, 'Raciocínio': 2, 'Determinação': 2}
profissao["Artista circense"] = {'Força': 0, 'Agilidade': 0, 'Destreza': 0, 'Vigor': 0, 'Presença': 0, 'Manipulação': 0, 'Compostura': 0, 'Inteligência': 0, 'Sagacidade': 0, 'Raciocínio': 0, 'Determinação': 0}
profissao["Artista dramático"] = {'Força': 0, 'Agilidade': 0, 'Destreza': 0, 'Vigor': 0, 'Presença': 0, 'Manipulação': 0, 'Compostura': 0, 'Inteligência': 0, 'Sagacidade': 0, 'Raciocínio': 0, 'Determinação': 0}
profissao["Dramaturgo"] = {'Força': 0, 'Agilidade': 0, 'Destreza': 0, 'Vigor': 0, 'Presença': 0, 'Manipulação': 0, 'Compostura': 0, 'Inteligência': 0, 'Sagacidade': 0, 'Raciocínio': 0, 'Determinação': 0}
profissao["Bandido"] = {'Força': 0, 'Agilidade': 0, 'Destreza': 0, 'Vigor': 0, 'Presença': 0, 'Manipulação': 0, 'Compostura': 0, 'Inteligência': 0, 'Sagacidade': 0, 'Raciocínio': 0, 'Determinação': 0}
profissao["Ladrão"] = {'Força': 2, 'Agilidade': 3, 'Destreza': 2, 'Vigor': 2, 'Presença': 1, 'Manipulação': 2, 'Compostura': 1, 'Inteligência': 2, 'Sagacidade': 3, 'Raciocínio': 2, 'Determinação': 2}
profissao["Assassino"] = {'Força': 0, 'Agilidade': 0, 'Destreza': 0, 'Vigor': 0, 'Presença': 0, 'Manipulação': 0, 'Compostura': 0, 'Inteligência': 0, 'Sagacidade': 0, 'Raciocínio': 0, 'Determinação': 0}
profissao["Traficante"] = {'Força': 0, 'Agilidade': 0, 'Destreza': 0, 'Vigor': 0, 'Presença': 0, 'Manipulação': 0, 'Compostura': 0, 'Inteligência': 0, 'Sagacidade': 0, 'Raciocínio': 0, 'Determinação': 0}
profissao["Falsário"] = {'Força': 0, 'Agilidade': 0, 'Destreza': 0, 'Vigor': 0, 'Presença': 0, 'Manipulação': 0, 'Compostura': 0, 'Inteligência': 0, 'Sagacidade': 0, 'Raciocínio': 0, 'Determinação': 0}

profissao_habilidades_centrais = OrderedDict()
profissao_habilidades_centrais['Sacerdotes'] = []
profissao_habilidades_centrais["Cavaleiros templários"] = []
profissao_habilidades_centrais["Soldado de infantaria"] = []
profissao_habilidades_centrais["Soldado de suporte"] = []
profissao_habilidades_centrais["Soldado de infantaria pesada"] = []
profissao_habilidades_centrais["Marinheiro"] = []
profissao_habilidades_centrais["Agente de segurança privada"] = []
profissao_habilidades_centrais["Policial"] = []
profissao_habilidades_centrais["Detetive"] = []
profissao_habilidades_centrais["Piloto"] = []
profissao_habilidades_centrais["Médico"] = []
profissao_habilidades_centrais["Curandeiro"] = []
profissao_habilidades_centrais["Cozinheiro"] = []
profissao_habilidades_centrais["Treinador animais"] = []
profissao_habilidades_centrais["Professor"] = []
profissao_habilidades_centrais["Político"] = []
profissao_habilidades_centrais["Oleiro"] = []
profissao_habilidades_centrais["Tecelão"] = []
profissao_habilidades_centrais["Coureiro"] = []
profissao_habilidades_centrais["Ferreiro"] = []
profissao_habilidades_centrais["Armeiro"] = []
profissao_habilidades_centrais["Marceneiro"] = []
profissao_habilidades_centrais["Mercador"] = []
profissao_habilidades_centrais["Proprietário de terras"] = []
profissao_habilidades_centrais["Burocrata"] = []
profissao_habilidades_centrais["Mercenário"] = []
profissao_habilidades_centrais["Escudeiro"] = []
profissao_habilidades_centrais["Agricultor"] = []
profissao_habilidades_centrais["Artista plástico"] = []
profissao_habilidades_centrais["Músico"] = []
profissao_habilidades_centrais["Artista marcial"] = []
profissao_habilidades_centrais["Artista circense"] = []
profissao_habilidades_centrais["Artista dramático"] = []
profissao_habilidades_centrais["Dramaturgo"] = []
profissao_habilidades_centrais["Bandido"] = []
profissao_habilidades_centrais["Ladrão"] = []
profissao_habilidades_centrais["Assassino"] = []
profissao_habilidades_centrais["Traficante"] = []
profissao_habilidades_centrais["Falsário"] = []

select_op_pull = OrderedDict()

select_op_pull['Ações de combate'] = [\
	'Atacar',
	'Defender-se',
	'Esperar']


select_op_pull['Menu Principal'] = [\
	'Criar personagem',
	'Modificar protagonistas',
	'Modificar antagonistas',
	'Modificar extras',
	'Listar protagonistas',
	'Listar antagonistas',
	'Listar extras',
	'Remover protagonistas',
	'Remover antagonistas',
	'Remover extras',
	'Run fixeres script...',
	'Sair']

select_op_pull['Tipo de personagem'] = [\
	'Protagonistas',
	'Antagonistas',
	'Extras']

select_op_pull['Metatipo'] = [\
	'Humano',
	'Vampiro',
	'Fada',
	'Lobisomem',
	'Elfo',
	'Hafling',
	'Anão']

select_op_pull['Sexo'] = [\
	'Masculino',
	'Feminino',
	'Hermafrodita']


select_op_pull['Informações dos personagens'] = [\
	"Ver informações"]

select_op_pull['Editar personagens'] = [\
	"Informações gerais",
	"Prelúdio",
	"Atributos",
	"Habilidades",
	"Especializações",
	"Antecedentes",
	"Equipamentos",
	"Habilidades especiais/sobrenaturais",
	'Redefinir atributos secundarios',
	'Modificar status',
	"Particularidades"]

select_op_pull["Marcadores"] = [\
	'Vitalidade',
	'Sangue',
	'Força de vontade',
	'Fadiga física',
	'Fadiga mental',
	'Sede',
	'Fome',
	'Melancolia',
	'Pavor']

select_op_pull['Moralidade'] = [\
	'Bondoso',
	'Justo',
	'Vingativo',
	'Maquiavélico',
	'Selvagem',
	'Cruel']

select_op_pull['Personalidade'] = [\
	"Inventor",
	"Dominador",
	"Hedonista",
	"Aventureiro",
	"Celebrante",
	"Competidor",
	"Covarde",
	"Resignado",
	"Criança",
	"Regente",
	"Ladino",
	"Excêntrico",
	"Fanático",
	"Altruísta",
	"Galante",
	"Gozador",
	"Juiz",
	"Malandro",
	"Mártir",
	"Masoquista",
	"Monstro",
	"Pedagogo",
	"Penitente",
	"Perfeccionista",
	"Ranzinza",
	"Rebelde",
	"Sobrevivente",
	"Solitário",
	"Tradicionalista",
	"Valentão",
	"Visionário"]

select_op_pull['Profissão'] = [\
	"Sacerdotes",
	"Cavaleiros templários",
	"Soldado de infantaria",
	"Soldado de suporte",
	"Soldado de infantaria pesada",
	"Marinheiro",
	"Agente de segurança privada",
	"Policial",
	"Detetive",
	"Piloto",
	"Médico",
	"Curandeiro",
	"Cozinheiro",
	"Treinador animais",
	"Professor",
	"Político",
	"Oleiro",
	"Tecelão",
	"Coureiro",
	"Ferreiro",
	"Armeiro",
	"Marceneiro",
	"Proprietário de terras",
	"Burocrata",
	"Mercenário",
	"Escudeiro",
	"Agricultor",
	"Artista plástico",
	"Músico",
	"Artista marcial",
	"Artista circense",
	"Artista dramático",
	"Dramaturgo",
	"Bandido",
	"Ladrão",
	"Assassino",
	"Traficante",
	"Falsário",
	"Mercador"]

select_op_pull['Vantagens'] = [\
	'Alfabetização (●)',
	'Bom senso (●●●●)',
	'Cinismo ante ao sobrenatural (●●)',
	'Conhecimento enciclopédico (●●●●)',
	'Consciência holística (●●●)',
	'Legado ocultista (●●●)',
	'Memória eidética (●●)',
	'Mente meditativa (●)',
	'Senso do perigo (●●)',
	'Marcado pelo sobrenatural (●●●)',
	'Sexto sentido (●●●)',
	'Idiomas (● por idioma)',
	'Ambidestria (●●)',
	'Ás do volante (●●)',
	'Costas fortes (●)',
	'Desarme (●●)',
	'Esquiva [Armamento] (●)',
	'Esquiva [Briga] (●)',
	'Estômago de avestruz (●●)',
	'Gigante (●●)',
	'Imunidade natural (●)',
	'Pistoleiro (●●●)',
	'Pulmões fortes (●●●)',
	'Recuperação rápida (●)',
	'Refinamento em combate [Facas] (●●)',
	'Refinamento em combate [Espadas] (●●)',
	'Refinamento em combate [Bastões] (●●)',
	'Refinamento em combate [Armas de corrente] (●●)',
	'Resistência a toxinas (●●)',
	'Saque rápido [Armas brancas] (●)',
	'Saque rápido [Arma de projétil] (●)',
	'Saque rápido [Arqueirismo] (●)',
	'Senso de direção (●)',
	'Segunda chance (●)',
	'Estilo de luta [Boxe] (● até ●●●●●)',
	'Estilo de luta [Duas armas] (● até ●●●●)',
	'Estilo de luta [Kung Fu] (● até ●●●●●)',
	'Estilo de luta [Manobras defensivas] (● até ●●●●●)',
	'Ligeiro (● até ●●●)',
	'Reflexos rápidos (● até ●●)',
	'Resistência férrea (● até ●●●)',
	'Recursos (● até ●●●●●)',
	'Status (● até ●●●●●)',
	'Aliados [Contexto] (● até ●●●●●)',
	'Contatos [Contexto] (● até ●●●●●)',
	'Mentor (● até ●●●●●)',
	'Servo/Assistente (● até ●●●●●)',
	'Aparência surpreendente (●● ou ●●●●)',
	'Fama (● até ●●●)',
	'Fonte de inspiração (●●●●)',
	'Habitué (●)',
	'Maestria [Ciências exatas] (● até ●●●●●●●●●●)',
	'Maestria [Erudição] (● até ●●●●●●●●●●)',
	'Maestria [Informática] (● até ●●●●●●●●●●)',
	'Maestria [Investigação] (● até ●●●●●●●●●●)',
	'Maestria [Medicina] (● até ●●●●●●●●●●)',
	'Maestria [Ocultismo] (● até ●●●●●●●●●●)',
	'Maestria [Ofícios] (● até ●●●●●●●●●●)',
	'Maestria [Política] (● até ●●●●●●●●●●)',
	'Maestria [Armas brancas] (● até ●●●●●●●●●●)',
	'Maestria [Armas de projétil] (● até ●●●●●●●●●●)',
	'Maestria [Arqueirismo] (● até ●●●●●●●●●●)',
	'Maestria [Briga] (● até ●●●●●●●●●●)',
	'Maestria [Condução] (● até ●●●●●●●●●●)',
	'Maestria [Dissimulação] (● até ●●●●●●●●●●)',
	'Maestria [Esportes] (● até ●●●●●●●●●●)',
	'Maestria [Furto] (● até ●●●●●●●●●●)',
	'Maestria [Sobrevivência] (● até ●●●●●●●●●●)',
	'Maestria [Astúcia] (● até ●●●●●●●●●●)',
	'Maestria [Empatia] (● até ●●●●●●●●●●)',
	'Maestria [Expressão] (● até ●●●●●●●●●●)',
	'Maestria [Intimidação] (● até ●●●●●●●●●●)',
	'Maestria [Manha] (● até ●●●●●●●●●●)',
	'Maestria [Persuasão] (● até ●●●●●●●●●●)',
	'Maestria [Socialização] (● até ●●●●●●●●●●)',
	'Maestria [Trato com animais] (● até ●●●●●●●●●●)']

select_op_pull['Habilidades'] = [\
	'Ciências exatas',
	'Erudição',
	'Tecnologia',
	'Informática',
	'Investigação',
	'Medicina',
	'Ocultismo',
	'Ofícios',
	'Política',
	'Armas brancas',
	'Armas de projétil',
	'Briga',
	'Condução',
	'Dissimulação',
	'Esportes',
	'Furto',
	'Sobrevivência',
	'Astúcia',
	'Empatia',
	'Expressão',
	'Intimidação',
	'Manha',
	'Persuasão',
	'Socialização',
	'Trato com animais']

select_op_pull["Tipo especialização"] = [\
	'Área de interesse',
	'Especialidade']

select_op_pull["Equipamentos"] = [\
	'Soco inglês',
	'Faca',
	'Facão',
	'Adaga',
	'Estaca de madeira',
	'Espada de lâmina larga',
	'Espada bastarda',
	'Sabre de cavalaria',
	'Gládio',
	'Bastão',
	'Lança',
	'Escudo grande híbrido (madeira e metal)',
	'Arco composto',
	'Cota de malha',
	'Armadura de placas',
	'Couraça',
	'Vinho',
	'Pão',
	'Queijo duro',
	'Botas',
	'Moedas']



lista_de_especializacoes = OrderedDict()
lista_de_especializacoes['Ciências'] = [\
	'Ciência [Biologia]',
	'Ciência [Física]',
	'Ciência [Metalurgia]',
	'Ciência [Geologia]',
	'Ciência [Química]']

lista_de_especializacoes['Erudição'] = [\
	'Erudição [Antropologia]',
	'Erudição [Arte]',
	'Erudição [Direito]',
	'Erudição [História]',
	'Erudição [Letras]',
	'Erudição [Pesquisa]',
	'Erudição [Religião]']

lista_de_especializacoes['Tecnologia'] = [\
	'Tecnologia [Desenvolvimento de ferramentas]',
	'Tecnologia [Desenvolvimento de armas]']

lista_de_especializacoes['Informática'] = [\
	'Informática [Ciberpirataria]',
	'Informática [Computação Gráfica]',
	'Informática [Inteligência Artificial]',
	'Informática [Internet]',
	'Informática [*Vírus de computador]',
	'Informática [Recuperação de dados]']

lista_de_especializacoes['Investigação'] = [\
	'Investigação [Artefatos]',
	'Investigação [Cenas de crime]',
	'Investigação [Enigmas]',
	'Investigação [Criptografia]',
	'Investigação [Diagnóstico de Autópsias]',
	'Investigação [Experimentos científicos]',
	'Investigação [Linguagem corporal]',
	'Investigação [Sonhos]']

lista_de_especializacoes['Medicina'] = [\
	'Medicina [Cirurgia]',
	'Medicina [Fármacos]',
	'Medicina [Fisioterapia]',
	'Medicina [Patologia]',
	'Medicina [Pronto-socorro]',
	'Medicina [*Epidemiologia]']

lista_de_especializacoes['Ocultismo'] = [\
	'Ocultismo [Bruxaria]',
	'Ocultismo [Crenças culturais]',
	'Ocultismo [Fantasmas]',
	'Ocultismo [Magia]',
	'Ocultismo [Monstros]',
	'Ocultismo [Superstições]']

lista_de_especializacoes['Ofícios'] = [\
	'Ofícios [Automóveis]',
	'Ofícios [Aeronaves]',
	'Ofícios [Concertos improvisados]',
	'Ofícios [Costura]',
	'Ofícios [Escultura]',
	'Ofícios [Fundição]',
	'Ofícios [*Construções]',
	'Ofícios [Curaria]',
	'Ofícios [*Ferreiro]']

lista_de_especializacoes['Política'] = [\
	'Política [Eleições]',
	'Política [Escândalos]',
	'Política [Estadual]',
	'Política [Federal]',
	'Política [Municipal]',
	'Política [Suborno/Barganha]']

lista_de_especializacoes['Armamento'] = [\
	'Armamento [Armas improvisadas]',
	'Armamento [Facas]',
	'Armamento [Espadas]',
	'Armamento [Lanças/Bastões]',
	'Armamento [Armas com corrente]',
	'Armamento [Armas de arremesso]']

lista_de_especializacoes['Arqueirismo'] = [\
	'Arqueirismo [Arco]',
	'Arqueirismo [Besta]']

lista_de_especializacoes['Armas de fogo'] = [\
	'Armas de fogo [Atirador de elite]',
	'Armas de fogo [Pistolas]',
	'Armas de fogo [Armas automáticas]',
	'Armas de fogo [Armas de tambor]']

lista_de_especializacoes['Briga'] = [\
	'Briga [Bloqueio]',
	'Briga [*Submissão]',
	'Briga [Projeção]',
	'Briga [Boxe]',
	'Briga [Kung Fu]',
	'Briga [*Muay Thai]']

lista_de_especializacoes['Condução'] = [\
	'Condução [Carros de alto desempenho]',
	'Condução [Despiste]',
	'Condução [Motocicletas]',
	'Condução [Perseguição]',
	'Condução [Proezas]',
	'Condução [Tração nas quatro]',
	'Condução [*Tratores]',
	'Condução [Cavalo de batalha]']

lista_de_especializacoes['Dissimulação'] = [\
	'Dissimulação [Camuflagem]',
	'Dissimulação [Deslocamento no escuro]',
	'Dissimulação [Deslocamento no mato]',
	'Dissimulação [Multidões]',
	'Dissimulação [Disfarces]']

lista_de_especializacoes['Esportes'] = [\
	'Esportes [Acrobacia]',
	'Esportes [Arremesso]',
	'Esportes [Canoagem]',
	'Esportes [Corrida endurance]',
	'Esportes [Corrida velocidade]',
	'Esportes [Escalada]',
	'Esportes [Natação]',
	'Esportes [Saltar]']

lista_de_especializacoes['Furto'] = [\
	'Furto [Abrir fechaduras]',
	'Furto [Arrombamento de cofres]',
	'Furto [Ocultação de artigos roubados]',
	'Furto [Punga]',
	'Furto [Sistemas de segurança]']

lista_de_especializacoes['Sobrevivência'] = [\
	'Sobrevivência [Abrigo]',
	'Sobrevivência [Meteorologia]',
	'Sobrevivência [Orientação]',
	'Sobrevivência [Procurar alimento]']

lista_de_especializacoes['Astúcia'] = [\
	'Astúcia [Detectar mentiras]',
	'Astúcia [Disfarçar emoções]',
	'Astúcia [Eludir]',
	'Astúcia [Mentir]']

lista_de_especializacoes['Empatia'] = [\
	'Empatia [Emoções]',
	'Empatia [Mentiras]',
	'Empatia [Motivos]',
	'Empatia [Personalidades]']

lista_de_especializacoes['Expressão'] = [\
	'Expressão [Artigos de jornal]',
	'Expressão [Dança]',
	'Expressão [Discursos]',
	'Expressão [*Artes plásticas]',
	'Expressão [Instrumento musical]',
	'Expressão [Teatro]']

lista_de_especializacoes['Intimidação'] = [\
	'Intimidação [Ameaças físicas]',
	'Intimidação [Ameaças veladas]',
	'Intimidação [Olhar ameaçador]',
	'Intimidação [Tortura]',
	'Intimidação [Vociferar]']

lista_de_especializacoes['Manha'] = [\
	'Manha [Boatos]',
	'Manha [Gangues]',
	'Manha [Mercado negro]',
	'Manha [Operações secretas]']

lista_de_especializacoes['Persuasão'] = [\
	'Persuasão [Discursos motivacionais]',
	'Persuasão [Engambelação]',
	'Persuasão [Inspirar tropas]',
	'Persuasão [Papo de vendedor]',
	'Persuasão [Sedução]']

lista_de_especializacoes['Socialização'] = [\
	'Socialização [Bailes de gala]',
	'Socialização [Bares]',
	'Socialização [Eventos formais]',
	'Socialização [Festas universitárias]',
	'Socialização [Jantares de gala]']

lista_de_especializacoes['Trato com animais'] = [\
	'Trato com animais [Adestramento]',
	'Trato com animais [Ataque iminente]',
	'Trato com animais [Necessidade dos animais]',
	'Trato com animais [Tipo específico de animal]']

custo_vantagens = OrderedDict()
custo_vantagens['Alfabetização (●)'] = 1
custo_vantagens['Bom senso (●●●●)'] = 4
custo_vantagens['Cinismo ante ao sobrenatural (●●)'] = 2
custo_vantagens['Conhecimento enciclopédico (●●●●)'] = 4
custo_vantagens['Consciência holística (●●●)'] = 3
custo_vantagens['Legado ocultista (●●●)'] = 3
custo_vantagens['Memória eidética (●●)'] = 2
custo_vantagens['Mente meditativa (●)'] = 1
custo_vantagens['Senso do perigo (●●)'] = 2
custo_vantagens['Marcado pelo sobrenatural (●●●)'] = 3
custo_vantagens['Sexto sentido (●●●)'] = 3
custo_vantagens['Idiomas (● por idioma)'] = 0
custo_vantagens['Ambidestria (●●)'] = 2
custo_vantagens['Ás do volante (●●)'] = 2
custo_vantagens['Costas fortes (●)'] = 1
custo_vantagens['Desarme (●●)'] = 2
custo_vantagens['Esquiva [Armamento] (●)'] = 1
custo_vantagens['Esquiva [Briga] (●)'] = 1
custo_vantagens['Estômago de avestruz (●●)'] = 2
custo_vantagens['Gigante (●●)'] = 2
custo_vantagens['Imunidade natural (●)'] = 1
custo_vantagens['Pistoleiro (●●●)'] = 3
custo_vantagens['Pulmões fortes (●●●)'] = 3
custo_vantagens['Recuperação rápida (●)'] = 1
custo_vantagens['Refinamento em combate [Facas] (●●)'] = 2
custo_vantagens['Refinamento em combate [Espadas] (●●)'] = 2
custo_vantagens['Refinamento em combate [Bastões] (●●)'] = 2
custo_vantagens['Refinamento em combate [Armas de corrente] (●●)'] = 2
custo_vantagens['Resistência a toxinas (●●)'] = 2
custo_vantagens['Saque rápido [Armas brancas] (●)'] = 1
custo_vantagens['Saque rápido [Armas de projétil] (●)'] = 1
custo_vantagens['Saque rápido [Arqueirismo] (●)'] = 1
custo_vantagens['Senso de direção (●)'] = 1
custo_vantagens['Segunda chance (●)'] = 1
custo_vantagens['Estilo de luta [Boxe] (● até ●●●●●)'] = 0
custo_vantagens['Estilo de luta [Duas armas] (● até ●●●●)'] = 0
custo_vantagens['Estilo de luta [Kung Fu] (● até ●●●●●)'] = 0
custo_vantagens['Estilo de luta [Manobras defensivas] (● até ●●●●●)'] = 0
custo_vantagens['Ligeiro (● até ●●●)'] = 0
custo_vantagens['Reflexos rápidos (● até ●●)'] = 0
custo_vantagens['Resistência férrea (● até ●●●)'] = 0
custo_vantagens['Recursos (● até ●●●●●)'] = 0
custo_vantagens['Status (● até ●●●●●)'] = 0
custo_vantagens['Aliados [Contexto] (● até ●●●●●)'] = 0
custo_vantagens['Contatos [Contexto] (● até ●●●●●)'] = 0
custo_vantagens['Mentor (● até ●●●●●)'] = 0
custo_vantagens['Servo/Assistente (● até ●●●●●)'] = 0
custo_vantagens['Aparência surpreendente (●● ou ●●●●)'] = 0
custo_vantagens['Fama (● até ●●●)'] = 0
custo_vantagens['Fonte de inspiração (●●●●)'] = 4
custo_vantagens['Habitué (●)'] = 1
custo_vantagens['Maestria [Ciências exatas] (● até ●●●●●●●●●●)'] = 0
custo_vantagens['Maestria [Erudição] (● até ●●●●●●●●●●)'] = 0
custo_vantagens['Maestria [Informática] (● até ●●●●●●●●●●)'] = 0
custo_vantagens['Maestria [Investigação] (● até ●●●●●●●●●●)'] = 0
custo_vantagens['Maestria [Medicina] (● até ●●●●●●●●●●)'] = 0
custo_vantagens['Maestria [Ocultismo] (● até ●●●●●●●●●●)'] = 0
custo_vantagens['Maestria [Ofícios] (● até ●●●●●●●●●●)'] = 0
custo_vantagens['Maestria [Política] (● até ●●●●●●●●●●)'] = 0
custo_vantagens['Maestria [Armas brancas] (● até ●●●●●●●●●●)'] = 0
custo_vantagens['Maestria [Armas de projétil] (● até ●●●●●●●●●●)'] = 0
custo_vantagens['Maestria [Arqueirismo] (● até ●●●●●●●●●●)'] = 0
custo_vantagens['Maestria [Briga] (● até ●●●●●●●●●●)'] = 0
custo_vantagens['Maestria [Condução] (● até ●●●●●●●●●●)'] = 0
custo_vantagens['Maestria [Dissimulação] (● até ●●●●●●●●●●)'] = 0
custo_vantagens['Maestria [Esportes] (● até ●●●●●●●●●●)'] = 0
custo_vantagens['Maestria [Furto] (● até ●●●●●●●●●●)'] = 0
custo_vantagens['Maestria [Sobrevivência] (● até ●●●●●●●●●●)'] = 0
custo_vantagens['Maestria [Astúcia] (● até ●●●●●●●●●●)'] = 0
custo_vantagens['Maestria [Empatia] (● até ●●●●●●●●●●)'] = 0
custo_vantagens['Maestria [Expressão] (● até ●●●●●●●●●●)'] = 0
custo_vantagens['Maestria [Intimidação] (● até ●●●●●●●●●●)'] = 0
custo_vantagens['Maestria [Manha] (● até ●●●●●●●●●●)'] = 0
custo_vantagens['Maestria [Persuasão] (● até ●●●●●●●●●●)'] = 0
custo_vantagens['Maestria [Socialização] (● até ●●●●●●●●●●)'] = 0
custo_vantagens['Maestria [Trato com animais] (● até ●●●●●●●●●●)'] = 0


metatipolist = []

proflist =[]

# acoes = '''\
# [1] Atacar/Preparar
# [2] Defender-se
# [3] Esperar
# '''

# armas='''\

# [1] Sem armas
# [2] Faca
# [3] Espada
# [4] Machado
# '''


# moves = OrderedDict()
# moves[1] = (3,'soco')
# moves[2] = (3,'faca')
# moves[3] = (4,'espada')
# moves[4] = (5,'machado')
