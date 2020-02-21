#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import MySQLdb
import os

_dbname = 'testdb'
_host='localhost'
_user='root'
_passwd='1234'

def importCVS2mySQL(filename, table, h, u, s, d):
	dbSQL = MySQLdb.connect(_host, _user, _passwd)
	cursor = dbSQL.cursor()
	
	try:
		cursor.execute("""CREATE DATABASE `%s` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;""" % d)
	except:
		pass

	cursor.execute("""USE %s;""" % d)

	fd = """timestamp,mat,nome,renovest,banco,ag,cc,cpf,termo""".split(',')
	ffild = fd[0]
	filename = '''3/27/2015 19:15:35,13/0153214,Luis Fernando Alves Vasconcelos,2/2016,BB,3264-6,42804-3,047.114.901-24,a
3/31/2015 19:17:57,11/0133242,Mayane Alves,2/2016,BB,3264-6,37890-9,030.481.891-73,a
4/10/2015 18:09:07,14/0161031,Rhaeska Lilliane Silva,2/2016,Caixa,973,13,034.411.261-65,a
4/10/2015 18:43:26,15/0021992,Sudário Macedo dos Santos,2/2016,BB,0377-8,42869-8,052.150.421-01,a
4/14/2015 17:46:59,15/0089911,Pedro Dias da Silva Neto,2/2016,BB,1335-8,15301-x,107.497.116-71,a
4/14/2015 19:03:39,10/45385,Ilda Rodrigues da Silva,2/2016,Santander,4290,01048856-1,905.822.091-53,a
4/16/2015 19:41:24,14/0138056,Evandro de Araújo Rocha,2/2016,N/A,N/A,N/A,010.375.401-66,a
4/16/2015 20:21:16,13/0153061,Leonardo Barros de Sousa,2/2016,Caixa,3001,00100024891-8,001.969.291-99,a
4/16/2015 20:23:39,11/0012887,Helen Dias Gomes,2/2016,Santander,970,01000593-2,040.190.261-73,a
4/22/2015 18:19:43,14/0089918,Adriana Batista Amorim Borges,2/2016,Itaú,2302,14968-7,701.531.401-00,a
4/22/2015 18:21:37,14/0172599,Hélen Caroline dos Santos Santiago,2/2016,Caixa,2490,21212-0,027.148.231-14,a
5/8/2015 18:23:23,11/0160649,Cremilce dos Santos Reis,2/2016,Santander,4290,01050784-0,042.842.423-69,a
5/13/2015 10:10:56,12/0186659,Edineia Gonçalves de Brito,1º/2016,Banco do Brasil,3713-3,11.160-0,045.832.651-82,a
5/13/2015 10:21:51,12/0186730,Suzana Fernandes Marinho,1º/2016,Caixa ,973,23.313-6,132.450.656-39,a
5/15/2015 9:03:04,12/0070049,Paula Divina da Cunha,2º/2016,BRB,77,73654,047.065.651-46,a
5/18/2015 14:57:21,140176136,MARCELO  ALVES DA SILVA CHAVES JUNIOR,2,BANCO DO BRASIL,432644,28959,5785879789,a
5/18/2015 15:17:45,15/0022468,THAYANE FERREIRA MOTA,1/2016,CAIXA,973,268479,5749041158,a
5/18/2015 15:25:38,15/0022069,TAINARA MARINHO DUARTE,2/2016,BANCO DO BRASIL,32646,481130,5265336176,a
5/18/2015 15:27:28,15/0089911,PEDRO DIAS DA SILVA NETO,2,BANCO DO BRASIL,13358,15301X,10749711671,a
5/18/2015 15:33:33,15/0013582,JOYCE DA LUZ BRITO,2,BRADESCO,2094,190616,6075313125,a
5/18/2015 15:49:19,140095926,BRUNO ALMEIDA DE SOUZA,2,BANCO DO BRASIL,1004-9,45147-9,4742530152,a
5/18/2015 15:50:44,14/0173382,NAIM VIEIRA MOUHAMAD ABOU,2,BANCO DO BRASIL,1606-3,62308,1656836947,a
5/18/2015 16:03:31,12/0068281,JAQUELINE ALVES RODRIGUES DA SILVA,2,BANCO DO BRASIL,3264-6,24494-5,98756205120,PASeUnB
5/18/2015 16:23:50,11/0083246,RENATO RODRIGO DA COSTA,2,SANTANDER,4290,01050175-8,7396697672,PASeUnB
5/18/2015 16:41:53,15/0079001,DÉBORA FERREIRA DE SALES SILVA,2,CAIXA,972,3918-0,2937139108,PASeUnB'''.split('\n')

	try:
		for i in fd:
			if i == ffild:
				cursor.execute("""CREATE TABLE %s(%s TEXT);""" % (table, i))
			else:
				cursor.execute("""ALTER TABLE %s ADD %s text AFTER %s;""" % (table, i, ffild))
			dbSQL.commit()

	except:
		pass
		
	try:
		for i in filename:
			d = i.split(',')
			for j in d:
				idx = d.index(j)
				col = fd[idx]
				if col == 'timestamp':
					cursor.execute("""INSERT INTO %s(%s) VALUES ("%s");""" % (table,col,j))
				else:
					cursor.execute("""UPDATE %s SET %s = "%s" WHERE %s = "%s";""" % (table,col,j,'timestamp',d[0]))
				dbSQL.commit()
					
	except:
		pass
	
	dbSQL.close()
	
	return filename, str(fd)

def index(req):
	f = importCVS2mySQL('File1.cvs', 'dataew', _host, _user, _passwd, _dbname)
	
	return f
		
	
		
	
