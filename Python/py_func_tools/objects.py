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

from modules.decorators import limpar_a_tela
from modules.db import profissao, metatipo, moralidade, select_op_pull, custo_vantagens, equipamentos
from modules.siur_funcs import verificar_tipo_de_atributo, verificar_tipo_de_habilidade, verificar_tipo_de_info
from modules.functools import *

from os import system as sh
import copy
#from os import listdir as ls
from subprocess import check_output as sh2

class Marcadores:
	def __init__(self):
		self.sangue = 0
		self.ferimentos_contundentes = 0
		self.ferimentos_letais = 0
		self.ferimentos_agravados = 0
		self.forca_de_vontade = 0
		self.fome = 0
		self.sede = 0
		self.pavor = 0
		self.melancolia = 0
		self.sono = 0
		self.fadiga_mental = 0
		self.fadiga_fisica = 0
		self.vitalidade = 0
		self.experiencia = 0
		self.estado = 'Normal'
		self.velocidade = 0
		self.estado = 'Normal'

class Carga:
	def __init__(self, forca, vigor):
		self.n0 = (forca + vigor + 2) * 1
		self.n1 = (forca + vigor + 2) * 2
		self.n2 = (forca + vigor + 2) * 4
		self.n3 = (forca + vigor + 2) * 6
		self.n4 = (forca + vigor + 2) * 8
		self.n5 = (forca + vigor + 2) * 10

class Player:
	def __init__(self):
		self.marcador = Marcadores()
		print(rosa('Definindo informações gerais...'))
		try: self.jogador = Info('Autor', self.jogador.valor)
		except: self.jogador = Info('Autor')
		try: self.tipo = Info('Tipo de personagem', self.tipo.valor)
		except: self.tipo = Info('Tipo de personagem')
		try: self.metatipo = Info('Metatipo', self.metatipo.valor)
		except: self.metatipo = Info('Metatipo')
		if self.tipo.valor != "Extras":
			self.areas_interesse = []
			self.especialidades = []
			self.vantagens = []
			self.equipamentos = []
			self.equipamentos_perdidos = []
			self.habilidades_especiais = []
			self.desenvolvimento_enredo = ''
			self.editar_informacoes_basicas()
			self.editar_preludio()
			self.editar_atributos()
			self.editar_habilidades()
			self.editar_especialidades()
			self.editar_vantagens()
			self.editar_equipamentos()
			self.definir_parametros_de_defesa()
			#self.editar_desvantagens(self) #Definir
			#self.editar_habilidades_sobrenaturais(self) #Definir
		else:
			try: self.nome = Info('Classe ou grupo', self.nome.valor)
			except: self.nome = Info('Classe ou grupo')
			try: self.profissao = Info('Profissão', self.profissao.valor)
			except: self.profissao = Info('Profissão')
			self.escolaridade = Info('Escolaridade')
			try: self.altura = Info('Altura [m]', self.altura.valor)
			except: self.altura = Info('Altura [m]')
			try: self.peso = Info('Peso [kg]', self.peso.valor)
			except: self.peso = Info('Peso [kg]')
			try: self.sexo = Info('Sexo predominante na classe ou grupo', self.sexo.valor)
			except: self.sexo = Info('Sexo predominante na classe ou grupo')
			self.descricao_equipamentos = Info('Descrição dos esquipamentos')

			self.areas_interesse = []
			self.especialidades = []
			self.vantagens = []
			self.equipamentos = []
			self.equipamentos_perdidos = []
			self.habilidades_especiais = []

			self.editar_atributos()
			self.editar_habilidades()
			self.editar_especialidades()
			self.editar_vantagens()
			self.editar_equipamentos()
			self.definir_parametros_de_defesa()

		self.forca_base = self.forca.nivel
		self.destreza_base = self.destreza.nivel
		self.agilidade_base = self.agilidade.nivel
		self.vigor_base = self.vigor.nivel
		self.presenca_base = self.presenca.nivel
		self.manipulacao_base = self.manipulacao.nivel
		self.compostura_base = self.compostura.nivel
		self.inteligencia_base = self.inteligencia.nivel
		self.raciocinio_base = self.raciocinio.nivel
		self.sagacidade_base = self.sagacidade.nivel
		self.determinacao_base = self.determinacao.nivel

		self.armas_brancas_base = self.armas_brancas.nivel
		self.armas_de_projetil_base = self.armas_de_projetil.nivel
		self.briga_base = self.briga.nivel
		self.conducao_base = self.conducao.nivel
		self.dissimulacao_base = self.dissimulacao.nivel
		self.esportes_base = self.esportes.nivel
		self.furto_base = self.furto.nivel
		self.sobrevivencia_base = self.sobrevivencia.nivel
		self.astucia_base = self.astucia.nivel
		self.empatia_base = self.empatia.nivel
		self.expressao_base = self.expressao.nivel
		self.intimidacao_base = self.intimidacao.nivel
		self.manha_base = self.manha.nivel
		self.persuasao_base = self.persuasao.nivel
		self.socializacao_base = self.socializacao.nivel
		self.trato_com_animais_base = self.trato_com_animais.nivel
		self.ciencias_base = self.ciencias.nivel
		self.erudicao_base = self.erudicao.nivel
		self.informatica_base = self.informatica.nivel
		self.investigacao_base = self.investigacao.nivel
		self.medicina_base = self.medicina.nivel
		self.ocultismo_base = self.ocultismo.nivel
		self.oficios_base = self.oficios.nivel
		self.politica_base = self.politica.nivel


	#Inserir dados
	def editar_vinculacao_com_enredo(self):
		self.escolaridade = Info('Escolaridade')
		self.afiliacao_politica = Info('Afiliação política')
		self.aparencia_fisica = Info('Descrição da aparência')
		self.descricao_equipamentos = Info('Descrição dos esquipamentos')
		self.humor = Info('Humor')
		try: self.motivacao = edit_textfield('Qual a motivação deste personagem?', self.motivacao)
		except: self.motivacao = edit_textfield('Qual a motivação deste personagem?')
		try: self.vinculos = edit_textfield('Quem são os familiares ou aliados deste personagem?', self.vinculos)
		except: self.vinculos = edit_textfield('Quem são os familiares ou aliados deste personagem?')
		try: self.na_trama = edit_textfield('Como este personagem se envolve na trama?', self.na_trama)
		except: self.na_trama = edit_textfield('Como este personagem se envolve na trama?')
		try: self.conflitos = edit_textfield('Quais são os conflitos pessoais do personagem?', self.conflitos)
		except: self.conflitos = edit_textfield('Quais são os conflitos pessoais do personagem?')
		try: self.climax = edit_textfield('Como se desenvolve o climax do conflito atual do personagem?', self.climax)
		except: self.climax = edit_textfield('Como se desenvolve o climax do conflito atual do personagem?')
		self.caracteristicas_vocais = Info('Características vocais')


	@limpar_a_tela
	def editar_informacoes_basicas(self):
		try: self.sexo = Info('Sexo', self.sexo.valor)
		except: self.sexo = Info('Sexo')
		try: self.personalidade = Info('Personalidade', self.personalidade.valor)
		except: self.personalidade = Info('Personalidade')
		try: self.moralidade = Info('Moralidade', self.moralidade.valor)
		except: self.moralidade = Info('Moralidade')
		try: self.profissao = Info('Profissão', self.profissao.valor)
		except: self.profissao = Info('Profissão')
		try: self.conceito = Info('Conceito', self.conceito.valor)
		except: self.conceito = Info('Conceito')
		try: self.etnia = Info('Etinia', self.etnia.valor)
		except: self.etnia = Info('Etinia')
		try: self.genero = Info('Gênero', self.genero.valor)
		except: self.genero = Info('Gênero')
		try: self.idade = Info('Idade', self.idade.valor)
		except: self.idade = Info('Idade')
		try: self.altura = Info('Altura [m]', self.altura.valor)
		except: self.altura = Info('Altura [m]')
		try: self.peso = Info('Peso [kg]', self.peso.valor)
		except: self.peso = Info('Peso [kg]')
		try: self.nome = Info('Nome', self.nome.valor)
		except: self.nome = Info('Nome')
		self.definir_atributos_base_profissao()
		self.definir_atributos_base_metatipo()
		self.definir_nivel_moral()
		if self.tipo.valor != 'Protagonistas' or 'Extras':
			self.editar_vinculacao_com_enredo()


	@limpar_a_tela
	def editar_preludio(self):
		try: self.preludio = edit_textfield('Prelúdio', self.preludio)
		except: self.preludio = edit_textfield('Prelúdio')


	@limpar_a_tela
	def editar_atributos(self):
		print(rosa('Definindo atributos...'))
		try: self.forca = Atributo("Força", self, self.forca.nivel)
		except: self.forca = Atributo("Força", self)
		try: self.agilidade = Atributo("Agilidade", self, self.agilidade.nivel)
		except: self.agilidade = Atributo("Agilidade", self)
		try: self.destreza = Atributo("Destreza", self, self.destreza.nivel)
		except: self.destreza = Atributo("Destreza", self)
		try: self.vigor = Atributo("Vigor", self, self.vigor.nivel)
		except: self.vigor = Atributo("Vigor", self)
		try: self.presenca = Atributo("Presença", self, self.presenca.nivel)
		except: self.presenca = Atributo("Presença", self)
		try: self.manipulacao = Atributo("Manipulação", self, self.manipulacao.nivel)
		except: self.manipulacao = Atributo("Manipulação", self)
		try: self.compostura = Atributo("Compostura", self, self.compostura.nivel)
		except: self.compostura = Atributo("Compostura", self)
		try: self.inteligencia = Atributo("Inteligência", self, self.inteligencia.nivel)
		except: self.inteligencia = Atributo("Inteligência", self)
		try: self.sagacidade = Atributo("Sagacidade", self, self.sagacidade.nivel)
		except: self.sagacidade = Atributo("Sagacidade", self)
		try: self.raciocinio = Atributo("Raciocínio", self, self.raciocinio.nivel)
		except: self.raciocinio = Atributo("Raciocínio", self)
		try: self.determinacao = Atributo("Determinação", self, self.determinacao.nivel)
		except: self.determinacao = Atributo("Determinação", self)



	@limpar_a_tela
	def editar_habilidades(self):
		print(rosa('Definindo habilidades...'))
		print(azul_claro('Práticas...'))
		try: self.armas_brancas = Habilidade('Armas brancas', self.armas_brancas.nivel)
		except: self.armas_brancas = Habilidade('Armas brancas')
		try: self.armas_de_projetil = Habilidade('Armas de projétil', self.armas_de_projetil.nivel)
		except: self.armas_de_projetil = Habilidade('Armas de projétil')
		try: self.briga = Habilidade('Briga', self.briga.nivel)
		except: self.briga = Habilidade('Briga')
		try: self.conducao = Habilidade('Condução', self.conducao.nivel)
		except: self.conducao = Habilidade('Condução')
		try: self.dissimulacao = Habilidade('Dissimulação', self.dissimulacao.nivel)
		except: self.dissimulacao = Habilidade('Dissimulação')
		try: self.esportes = Habilidade('Esporte', self.esportes.nivel)
		except: self.esportes = Habilidade('Esporte')
		try: self.furto = Habilidade('Furto', self.furto.nivel)
		except: self.furto = Habilidade('Furto')
		try: self.sobrevivencia = Habilidade('Sobrevivência', self.sobrevivencia.nivel)
		except: self.sobrevivencia = Habilidade('Sobrevivência')

		print(azul_claro('Relacionais...'))
		try: self.astucia = Habilidade('Astúcia', self.astucia.nivel)
		except: self.astucia = Habilidade('Astúcia')
		try: self.empatia = Habilidade('Empatia', self.empatia.nivel)
		except: self.empatia = Habilidade('Empatia')
		try: self.expressao = Habilidade('Expressão', self.expressao.nivel)
		except: self.expressao = Habilidade('Expressão')
		try: self.intimidacao = Habilidade('Intimidação', self.intimidacao.nivel)
		except: self.intimidacao = Habilidade('Intimidação')
		try: self.manha = Habilidade('Manha', self.manha.nivel)
		except: self.manha = Habilidade('Manha')
		try: self.persuasao = Habilidade('Persuasão', self.persuasao.nivel)
		except: self.persuasao = Habilidade('Persuasão')
		try: self.socializacao = Habilidade('Socialização', self.socializacao.nivel)
		except: self.socializacao = Habilidade('Socialização')
		try: self.trato_com_animais = Habilidade('Trato com animais', self.trato_com_animais.nivel)
		except: self.trato_com_animais = Habilidade('Trato com animais')

		print(azul_claro('Mentais...'))
		try: self.ciencias = Habilidade('Ciências exatas', self.ciencias.nivel)
		except: self.ciencias = Habilidade('Ciências exatas')
		try: self.erudicao = Habilidade('Erudição', self.erudicao.nivel)
		except: self.erudicao = Habilidade('Erudição')
		try: self.informatica = Habilidade('Informática', self.informatica.nivel)
		except: self.informatica = Habilidade('Informática')
		try: self.investigacao = Habilidade('Investigação', self.investigacao.nivel)
		except: self.investigacao = Habilidade('Investigação')
		try: self.medicina = Habilidade('Medicina', self.medicina.nivel)
		except: self.medicina = Habilidade('Medicina')
		try: self.ocultismo = Habilidade('Ocultismo', self.ocultismo.nivel)
		except: self.ocultismo = Habilidade('Ocultismo')
		try: self.oficios = Habilidade('Ofícios', self.oficios.nivel)
		except: self.oficios = Habilidade('Ofícios')
		try: self.politica = Habilidade('Política', self.politica.nivel)
		except: self.politica = Habilidade('Política')

	@limpar_a_tela
	def editar_especialidades(self):
		print(rosa('Definindo áreas de interesse e especialidades...'))
		loop = True
		while loop:
			print('Qual tipo de especialidade você deseja registrar?')
			selecao = select_op(select_op_pull["Tipo especialização"], 1)
			if selecao == 'Área de interesse':
				inserir = input('Descreva a área de interesse:\n$: ' )
				self.areas_interesse.append(inserir)
			elif selecao == 'Especialidade':
				inserir = input('Descreva a especialidade:\n$: ' )
				self.especialidades.append(inserir)
			print('')
			if input('Deseja inserir outra? (s/n): ') != 's':
				loop = False
			print('')

	@limpar_a_tela
	def editar_vantagens(self):
		print(rosa('Definindo vantagens...'))
		selecao = select_ops(select_op_pull["Vantagens"], 3, sort_list=True)
		for i in selecao:
			if custo_vantagens[i] == 0:
				print(verde('Quantos pontos você gastará para adquirir a vantagem?'))
				pts = input_num(i)
				bolinhas = '('
				while pts != 0:
					bolinhas += '●'
					pts -= 1
				bolinhas += ')'
				self.vantagens.append(i.split('(')[0] + bolinhas)
			else:
				self.vantagens.append(i)

	def editar_marcadores(self):
		selecao = select_op(select_op_pull["Marcadores"], 3)
		if selecao == 'Vitalidade':
			modificador = input_num('Alterar vitalidade para')
			self.marcador.vitalidade += modificador
			print('Qual o tipo de dano causado?')
			tipo_dano = select_op(['Contundente', 'Letal', 'Agravado'], 1)
			if tipo_dano == 'Contundente':
				self.marcador.ferimentos_contundentes += modificador
			elif tipo_dano == 'Letal':
				self.marcador.ferimentos_letais += modificador
			elif tipo_dano == 'Agravado':
				self.marcador.ferimentos_agravados += modificador

		elif selecao == 'Sangue':
			modificador = input_num('Alterar pontos de sangue em')
			self.marcador.sangue += modificador
		elif selecao == 'Força de vontade':
			modificador = input_num('Alterar pontos de força de vontade em')
			self.marcador.forca_de_vontade += modificador
		elif selecao == 'Fadiga física':
			modificador = input_num('Alterar pontos de fadiga física em')
			self.marcador.fadiga_fisica += modificador
		elif selecao == 'Fadiga mental':
			modificador = input_num('Alterar pontos de fadiga mental em')
			self.marcador.fadiga_mental += modificador
		elif selecao == 'Sede':
			modificador = input_num('Alterar marcadores de sede em')
			self.marcador.sede += modificador
		elif selecao == 'Fome':
			modificador = input_num('Alterar marcadores de fome em')
			self.marcador.fome += modificador
		elif selecao == 'Melancolia':
			modificador = input_num('Alterar marcadores de melancolia em')
			self.marcador.melancolia += modificador
		elif selecao == 'Pavor':
			modificador = input_num('Alterar marcadores de pavor em')
			self.marcador.forca_de_vontade += modificador
			#Assustado -1 (ações mentais e destreza -1)
			#Abalado -2 (ações físicas contra o medo -1; ações mentais e destreza -2)
			#Apavorado -3 (não pode agir contra medo; ações fisicas -2; mentais -4)


	def definir_estado():
		pass

	def adicionar_equipamento(self):
		print(rosa("Selecione os equipamentos que o seu personagem possui..."))
		selecao = select_ops(select_op_pull["Equipamentos"], 3)
		check_list = copy.copy(selecao)
		for i in selecao:
			n = check_list.count(i)
			check_list.remove(i)
			novo_equipamento = copy.copy(equipamentos[i])
			if novo_equipamento.tipo == 'Dinheiro':
				novo_equipamento.quantidade = input_num('Informe a quantidade de {}'.format(novo_equipamento.nome), 1)
				novo_equipamento.peso = novo_equipamento.peso_unitario * novo_equipamento.quantidade
			elif novo_equipamento.tipo == 'Ervas':
				novo_equipamento.quantidade = input_num('Informe a quantidade de {}'.format(novo_equipamento.nome), 1)
				novo_equipamento.peso = novo_equipamento.peso_unitario * novo_equipamento.quantidade
			elif novo_equipamento.tipo == 'Alimentos':
				novo_equipamento.quantidade = input_num('Informe a quantidade de {}'.format(novo_equipamento.nome), 1)
				novo_equipamento.peso = novo_equipamento.peso_unitario * novo_equipamento.quantidade
			else:
				novo_equipamento.nome = novo_equipamento.nome + ' #{}'.format(n)

			self.equipamentos.append(novo_equipamento)
		del(check_list)

	def armas_disponiveis(self):
		lista = []
		for e in self.equipamentos:
			if e.tipo == "Arma":
				lista.append(e.nome)
		return lista

	def usar_arma(self, nome):
		for e in self.equipamentos:
			if e.nome == nome:
				return e

	def remover_equipamento(self):
		print(rosa("Selecione os equipamentos que serão removidos do inventário..."))
		eqs = []
		for i in self.equipamentos:
			eqs.append(i.nome)
		selecao = select_ops(eqs, 3)
		for i in selecao:
			for e in self.equipamentos:
				if e.nome == i:
					self.equipamentos_perdidos.append(self.equipamentos.pop(self.equipamentos.index(e)))

	def recuperar_equipamento(self):
		print(rosa("Selecione os equipamentos recuperados..."))
		eqs = []
		for i in self.equipamentos_perdidos:
			eqs.append(i.nome)
		selecao = select_ops(eqs, 3)
		for i in selecao:
			for e in self.equipamentos_perdidos:
				if e.nome == i:
					self.equipamentos.append(self.equipamentos_perdidos.pop(self.equipamentos_perdidos.index(e)))

	@limpar_a_tela
	def editar_equipamentos(self):
		if self.equipamentos == []:
			self.adicionar_equipamento()
		else:
			print(rosa("Editar equipamentos..."))
			selecao = select_op(['Adicionar', 'Recuperar', 'Remover'], 1)
			if selecao == 'Adicionar':
				self.adicionar_equipamento()
			elif selecao == 'Recuperar':
				self.recuperar_equipamento()
			elif selecao == 'Remover':
				self.remover_equipamento()
		self.definir_atributos_secundarios()

	def ver_equipamento(self):
		lista = []
		for i in self.equipamentos:
			lista.append(i.nome)
		selecao = select_op(lista, 3)

	def ver_equipamentos(self):
		print(azul_claro('Equipamentos...'))
		for i in self.equipamentos:
			if i.tipo == ('Dinheiro' or 'Ervas' or 'Alimentos'):
				print(amarelo('{} (quantidade: {})'.format(i.nome, i.quantidade)))
			else:
				print(verde(i.nome))
		print(vermelho('Peso dos equipamentos: ')+str(self.definir_peso_carregado()))
		print('')

	def sacar_arma(self, arma):
		for v in self.vantagens:
			if (arma.habilidade_base == "Armas brancas") and v.find("Saque rápido [Armas brancas] (●)") != -1:
				return 5
			elif (arma.habilidade_base == "Armas de projétil") and v.find("Saque rápido [Armas de projétil] (●)") != -1:
				return 5
			else:
				return 10

	#Calculos automaticos
	def definir_atributos_base_profissao(self):
		self.forca_base_profissao = profissao[self.profissao.valor]['Força']
		self.agilidade_base_profissao = profissao[self.profissao.valor]['Agilidade']
		self.destreza_base_profissao = profissao[self.profissao.valor]['Destreza']
		self.vigor_base_profissao = profissao[self.profissao.valor]['Vigor']
		self.presenca_base_profissao = profissao[self.profissao.valor]['Presença']
		self.manipulacao_base_profissao = profissao[self.profissao.valor]['Manipulação']
		self.compostura_base_profissao = profissao[self.profissao.valor]['Compostura']
		self.inteligencia_base_profissao = profissao[self.profissao.valor]['Inteligência']
		self.raciocinio_base_profissao = profissao[self.profissao.valor]['Raciocínio']
		self.determinacao_base_profissao = profissao[self.profissao.valor]['Determinação']

	def definir_atributos_base_metatipo(self):
		self.forca_base_metatipo = metatipo[self.metatipo.valor]['Força']
		self.agilidade_base_metatipo = metatipo[self.metatipo.valor]['Agilidade']
		self.destreza_base_metatipo = metatipo[self.metatipo.valor]['Destreza']
		self.vigor_base_metatipo = metatipo[self.metatipo.valor]['Vigor']
		self.presenca_base_metatipo = metatipo[self.metatipo.valor]['Presença']
		self.manipulacao_base_metatipo = metatipo[self.metatipo.valor]['Manipulação']
		self.compostura_base_metatipo = metatipo[self.metatipo.valor]['Compostura']
		self.inteligencia_base_metatipo = metatipo[self.metatipo.valor]['Inteligência']
		self.sagacidade_base_metatipo = metatipo[self.metatipo.valor]['Sagacidade']
		self.raciocinio_base_metatipo = metatipo[self.metatipo.valor]['Raciocínio']
		self.determinacao_base_metatipo = metatipo[self.metatipo.valor]['Determinação']

	def definir_nivel_moral(self):
		self.moralidade_nivel = moralidade[self.moralidade.valor]

	def definir_velocidade_de_reacao(self):
		if check_item_list('Reflexos rápidos (●)', self.vantagens):
			return 1 + self.compostura.nivel + self.agilidade.nivel
		elif check_item_list('Reflexos rápidos (●●)', self.vantagens):
			return 2 + self.compostura.nivel + self.agilidade.nivel
		else:
			return self.compostura.nivel + self.agilidade.nivel

	def definir_peso_carregado(self):
		carga = 0.0
		for e in self.equipamentos:
			carga += e.peso
		return carga


	def definir_deslocamento(self):
		carga = self.definir_peso_carregado()
		if carga <= self.carga.n0:
			redutor_de_carga = 0
		elif (carga > self.carga.n0) and (carga <= self.carga.n1):
			redutor_de_carga = 1
		elif (carga > self.carga.n1) and (carga <= self.carga.n2):
			redutor_de_carga = 2
		elif (carga > self.carga.n2) and (carga <= self.carga.n3):
			redutor_de_carga = 3
		elif (carga > self.carga.n3) and (carga <= self.carga.n4):
			redutor_de_carga = 4
		elif (carga > self.carga.n4) and (carga <= self.carga.n5):
			redutor_de_carga = 5

		ligeiro = 0
		if check_item_list('Ligeiro (●)', self.vantagens):
			ligeiro = 1
		elif check_item_list('Ligeiro (●●)', self.vantagens):
			ligeiro = 2
		elif check_item_list('Ligeiro (●●●)', self.vantagens):
			ligeiro = 3

		return flt(flt(self.forca.nivel)/2.0 + flt(self.agilidade.nivel)/2.0 + 5 + ligeiro)/2.0 - redutor_de_carga

	def definir_envergadura(self):
		if self.sexo.valor == 'Masculino':
			fator = 1.06
		else:
			fator = 1.03
		return flt(flt(self.altura.valor.replace(',','.')) * fator)

	def definir_salto_vertical(self):
		return (flt(self.forca.nivel/self.vigor.nivel) * 0.3) + flt(self.altura.valor) + ((self.definir_envergadura()/6.0)*2.5)

	def definir_deslocamento_por_instante(self):
		if check_item_list('Velocidade sobrenatural (●)', self.habilidades_especiais):
			return flt(self.definir_deslocamento() / (12.0+(2*1)))
		if check_item_list('Velocidade sobrenatural (●●)', self.habilidades_especiais):
			return flt(self.definir_deslocamento() / (12.0+(2*2)))
		if check_item_list('Velocidade sobrenatural (●●●)', self.habilidades_especiais):
			return flt(self.definir_deslocamento() / (12.0+(2*3)))
		else:
			return flt(self.definir_deslocamento() / 10.0)

	def definir_instantes_totais(self):
		if check_item_list('Velocidade sobrenatural (●)', self.habilidades_especiais):
			return float(12)
		elif check_item_list('Velocidade sobrenatural (●●)', self.habilidades_especiais):
			return float(14)
		elif check_item_list('Velocidade sobrenatural (●●●)', self.habilidades_especiais):
			return float(16)
		elif check_item_list('Velocidade sobrenatural (●●●●)', self.habilidades_especiais):
			return float(18)
		elif check_item_list('Velocidade sobrenatural (●●●●●)', self.habilidades_especiais):
			return float(20)
		else:
			return float(15)


	def definir_atributos_secundarios(self):
		self.carga = Carga(self.forca.nivel, self.vigor.nivel)
		self.velocidade_de_reacao = self.definir_velocidade_de_reacao() #Iniciativa combate
		self.velocidade_de_improvisacao = self.sagacidade.nivel + self.raciocinio.nivel + self.compostura.nivel
		self.arremesso = (self.forca.nivel * 2) + 2 + self.esportes.nivel
		self.deslocamento = self.definir_deslocamento()
		self.investida = flt(self.definir_deslocamento()) * 1.5
		self.salto_vertical = self.definir_salto_vertical()
		self.salto_horizontal = ((self.definir_deslocamento()) * 0.75)
		self.deslocamento_por_instante = self.definir_deslocamento_por_instante()
		self.vitalidade = self.vigor.nivel * 3
		self.sangue = (self.vigor.nivel * 3) - 2
		self.fadiga_mental = self.determinacao.nivel * 2
		self.fadiga_fisica = self.vigor.nivel * 2
		self.forca_de_vontade = self.determinacao.nivel + self.compostura.nivel
		self.instantes = self.definir_instantes_totais()
		self.instantes_duracao = float(2.0/self.instantes)

	def definir_defesa_base(self):
		if self.sagacidade.nivel < self.agilidade.nivel:
			return self.sagacidade.nivel
		else:
			return self.agilidade.nivel

	def definir_blindagem(self):
		return input_num('Blindagem')

	def definir_bloqueio(self):
		return self.defesa + self.briga.nivel

	def definir_aparar(self):
		return self.defesa + self.armas_brancas.nivel

	def definir_parametros_de_defesa(self):
		self.defesa = self.definir_defesa_base()
		self.blindagem = self.definir_blindagem()
		self.esquiva = self.definir_defesa_base() * 2
		self.bloqueio = self.definir_bloqueio()
		self.aparar = self.definir_aparar()




	@limpar_a_tela
	def ver_informacoes_gerais(self):
		print(azul_claro('Informações gerais...'))

		lista_de_informacoes_gerais = [\
		self.tipo,
		self.metatipo,
		self.nome,
		self.conceito,
		self.personalidade,
		self.moralidade,
		self.etnia,
		self.profissao,
		self.genero,
		self.idade,
		self.altura,
		self.peso]

		saida = []
		for informacao in lista_de_informacoes_gerais:
			saida.append("{}: {}".format(verde(informacao.nome), informacao.valor))

		render_cols(saida, 3, idx=False)
		print('')



	def ver_preludio(self):
		print(azul_claro('Prelúdio...'))
		print(self.preludio)
		print('')


	def ver_atributos(self):
		print(azul_claro('Atributos...'))

		tamanho_col = 20
		idx = 1

		lista_de_atributos =[\
		self.forca,
		self.presenca,
		self.inteligencia,
		self.agilidade,
		self.manipulacao,
		self.sagacidade,
		self.destreza,
		self.compostura,
		self.raciocinio,
		self.vigor,
		self.vigor,
		self.determinacao]

		saida = []
		for atributo in lista_de_atributos:
			if idx == 11:
				saida.append(''.ljust(tamanho_col))
			else:
				saida.append("{}: {}".ljust(tamanho_col).format(verde(atributo.nome), atributo.nivel))
			idx += 1

		render_cols(saida, 3, idx=False)
		print('')

	def ver_atributos_secundarios(self):
		print(azul_claro('Atributos secundarios...'))
		lista_atributos_secundarios = [\
		('Sem penalidade', self.carga.n0),
		('-1 no deslocamento', self.carga.n1),
		('-2 no deslocamento', self.carga.n2),
		('-3 no deslocamento', self.carga.n3),
		('-4 no deslocamento', self.carga.n4),
		('Iniciativa base (combate)', self.velocidade_de_reacao),
		('Iniciativa embate social', self.velocidade_de_improvisacao),
		('Parâmetro de arremesso', self.arremesso),
		('Deslocamento base', self.deslocamento),
		('Deslocamento por instante', self.deslocamento_por_instante),
		('Deslocamento de investida', self.investida),
		("Altura base, salto vertical (m)", self.salto_vertical),
		('Distância base, salto horizontal (m)', self.salto_horizontal),
		('Vitalidade total', self.vitalidade),
		('Sangue total', self.sangue),
		('Fadiga mental total', self.fadiga_mental),
		('Fadiga física total', self.fadiga_fisica),
		('Força de vontade total', self.forca_de_vontade)]


		for i in lista_atributos_secundarios:
			print('{}: {}'.format(verde(i[0]), i[1]))

		print('')


	def ver_habilidades(self):
		print(azul_claro('Habilidades...'))

		lista_de_habilidades = [\
		self.armas_brancas,
		self.armas_de_projetil,
		self.briga,
		self.conducao,
		self.dissimulacao,
		self.esportes,
		self.furto,
		self.sobrevivencia,
		self.astucia,
		self.empatia,
		self.expressao,
		self.intimidacao,
		self.manha,
		self.persuasao,
		self.socializacao,
		self.trato_com_animais,
		self.ciencias,
		self.erudicao,
		self.informatica,
		self.investigacao,
		self.medicina,
		self.ocultismo,
		self.oficios,
		self.politica]

		saida = []
		for habilidade in lista_de_habilidades:
			if habilidade.nivel != 0:
				saida.append("{}: {}".format(verde(habilidade.nome), habilidade.nivel))

		render_cols(saida, 3, idx=False)
		print('')




	def ver_especializacoes(self):
		print(azul_claro('Áreas de interesse... (+1)'))
		for ai in self.areas_interesse:
			print("{}".format(verde(ai)))
		print('')

		print(azul_claro('Especialidades... (+2)'))
		for e in self.especialidades:
			print("{}".format(verde(e)))
		print('')




	def ver_vantagens(self):
		print(azul_claro('Vantagens...'))

		saida = []
		for vantagem in self.vantagens:
			saida.append("{}".format(verde(vantagem)))

		render_cols(saida, 2, idx=False)
		print('')



	def ver_habilidades_especiais(self):
		pass


	def info_vitalidade(self):

		return


	def info1(self):
		self.fadiga_fisica_efetiva = self.fadiga_fisica + self.marcador.fadiga_fisica
		self.vitalidade_efetiva = self.vitalidade + self.marcador.vitalidade
		o = saida_rosa("Iniciativa base", self.velocidade_de_reacao) + linesep
		o += saida_rosa('Deslocamento', self.definir_deslocamento()) + linesep
		o += saida_verde('Vitalidade', self.vitalidade_efetiva, referencia=self.vitalidade, escalonamento=[self.marcador.ferimentos_contundentes, self.marcador.ferimentos_letais, self.marcador.ferimentos_agravados]) + linesep
		o += saida_verde('Fadiga física', self.fadiga_fisica_efetiva) + linesep
		o += saida_verde('Estado:', self.marcador.estado) + linesep


		return o

	def info2(self):
		self.forca_de_vontade_efetiva = self.forca_de_vontade + self.marcador.forca_de_vontade
		self.sangue_efetivo = self.sangue + self.marcador.sangue
		self.fadiga_mental_efetiva = self.fadiga_mental + self.marcador.fadiga_mental
		o = saida_vermelha('Sangue', self.sangue_efetivo) + linesep
		o += saida_verde('Força de vontade', self.forca_de_vontade_efetiva) + linesep
		o += saida_verde('Fadiga mental', self.fadiga_mental_efetiva) + linesep
		o += saida_verde('Pavor', self.marcador.pavor) + linesep
		o += saida_verde('Estado:', self.marcador.estado) + linesep

		return o




class Info:
	def __init__(self, nome, valor_anterior=None):
		self.nome = nome
		self.tipo = verificar_tipo_de_info(nome)
		if valor_anterior != None:
			if self.tipo == "Fechada":
				print("{} [{}], escolha uma opção.".format(verde(nome), azul_claro(valor_anterior)))
				self.valor = select_op(select_op_pull[nome], 3)
			else:
				self.valor = input(verde(nome)+" [{}]: ".format(valor_anterior))
		else:
			if self.tipo == "Fechada":
				print("{}, escolha uma opção.".format(verde(nome)))
				self.valor = select_op(select_op_pull[nome], 3)
			else:
				self.valor = input(verde(nome)+": ")


class Atributo:
	def __init__(self, nome, obj, valor_anterior=None):
		valor_base = metatipo[obj.metatipo.valor][nome] + profissao[obj.profissao.valor][nome] + 1
		if valor_anterior != None:
			self.nivel = input_num(nome, valor_anterior)
		else:
			self.nivel = input_num(nome, valor_base)
		self.nome = nome
		self.tipo = verificar_tipo_de_atributo(nome)


class Habilidade:
	def __init__(self, nome, valor_anterior=None):
		if valor_anterior != None:
			self.nivel = input_num(nome, valor_anterior)
		else:
			self.nivel = input_num(nome, 0)
		self.nome = nome
		self.tipo = verificar_tipo_de_habilidade(nome)


class Cena:
	def __init__(self):
		self.titulo = input(verde("Título da cena")+': ')
		self.descricao = edit_textfield('O que ocorre na cena?')

	def editar_cena(self):
		novo_titulo = input(verde("Título da cena")+' [{}]: '.format(self.titulo))
		if novo_titulo == '':
			pass
		else:
			self.titulo = novo_titulo
		self.descricao = edit_textfield('O que ocorre na cena?', self.descricao)

	@limpar_a_tela
	def ver_informacoes(self):
		print(verde(self.titulo))
		print(self.descricao)
