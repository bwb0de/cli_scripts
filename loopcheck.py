#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import MySQLdb, glob, os, random
import db2010

dbedupydb = db2010.db

db = MySQLdb.connect('localhost','root','m@r1anell4','dbedudb')
dbc = db.cursor()
try:
	dbc.execute("CREATE TABLE T000000000 (IDNUM TEXT, TURMA TEXT, NUM INT, NOME TEXT)")
except:
	pass


l = []
for i in dbedupydb:
	#Definindo ID do aluno
	while True:
		n = 'T' + str(random.randint(1,100000000))
		try:
			t = l.index(n)
			#print "Lista 'l' já possui o número %s" % n
		except:
			l.append(n)
			#print "Adicionando %s à lista 'l'" % n
			break
		#if len(l) == 100000000:
		#	break
	
	#Inserindo dados na meta-tabela
	dbc.execute("INSERT INTO T000000000(IDNUM, TURMA, NUM, NOME) VALUES('%s', '%s', '%s', '%s')" % (n, d[i]['loc'][0], d[i]['loc'][1], d[i]['nfo'][0]))
	
	#Criando tabela ID para inserção de dados dos alunos
	mats = ['EDF', 'POR', 'MAT', 'CNA', 'HIS', 'LEM']
	bims = ['1B', '2B', '3B', '4B', 'RF']
	rstr = ''
	
	for j in mats:
		for jj in bims:
			s = j + jj + ' TEXT, '
			rstr = rstr + s
		
	dbc.execute("CREATE TABLE %s (%s)" % (n, rstr))
	
	#Inserindo dados dos alunos em sua respectiva tabela ID


			
