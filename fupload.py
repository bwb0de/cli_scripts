#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Created on Fri May 15 00:00:04 2015

@author: bwb0de
Telefone: 81882338
e-Mail: dftdcruz@gmail.com

"""

""" Ordenar Resultados mySQL
SELECT cols FROM `tab` ORDER BY `col1` ASC,`col2` DESC;
"""




import os
import MySQLdb
import time
import string

_host='localhost'
_user='root'
_passwd='1234'

_fileitem = ""

def GoogleTS2mySQLDT(s):
	r = time.strftime("%Y-%m-%d %H:%M:%S", time.strptime(s, "%m/%d/%Y %H:%M:%S"))
	return r

def CleanString(s):
	r = s
	for i in string.whitespace+string.punctuation:
		r = r.replace(i,"")
	return r

def ReplaceEnclosed(s):
    '''
    Lê o conteúdo do arquivo CVS e separa as colunas sem romper os campos com texto em parágravo ou virgula (enclosed by '"'). Recebe uma string como argumento e retorna uma lista contendo as colunas.
    '''

    t = s
    while True:
        try:
            idx1 = t.index(',"')
            idx2 = t.index('",')
            sect1 = t[:idx1]+","+t[idx1+1:idx2+1].replace(',','£').replace('"','¹').replace('\n','#')
            t = sect1 + ',' + t[idx2+2:]
        except:
            break
    t = t.replace(',','|').replace('£',',').replace('¹','').split('\n')#('³')
    output = []
    for i in t:
        output.append(i.replace('#',os.linesep))
    return output[0]


def importTVS2mySQL(filename, table, h, u, s, d):
    '''
    Realiza a insersão do conteudo do arquivo TVS no banco de dados.
    '''

    dbSQL = MySQLdb.connect(_host, _user, _passwd)
    cursor = dbSQL.cursor()
    try:
        cursor.execute("""CREATE DATABASE `%s` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;""" % d)
    except:
        pass
    cursor.execute("""USE %s;""" % d)
    fd = filename[0].split('\t')
    ffild = fd[0]
    filename = filename[1:]
    try:
        for i in fd:
            if i == ffild:
                if i.find("INT") != -1:
                    cursor.execute("""CREATE TABLE %s(%s INT);""" % (table, i))
                elif i.find("LG") != -1:
                    cursor.execute("""CREATE TABLE %s(%s LONGTEXT);""" % (table, i))
                elif i.find("TS") != -1:
                    cursor.execute("""CREATE TABLE %s(%s DATETIME);""" % (table, i))
                elif i.find("DT") != -1:
                    cursor.execute("""CREATE TABLE %s(%s DATE);""" % (table, i))
                elif i.find("DC") != -1:
                    cursor.execute("""CREATE TABLE %s(%s DECIMAL(5,2));""" % (table, i))
                else:
                    cursor.execute("""CREATE TABLE %s(%s TEXT);""" % (table, i))
                
            else:
                if i.find("INT") != -1:
                    cursor.execute("""ALTER TABLE %s ADD %s INT AFTER %s;""" % (table, i, ffild))
                elif i.find("LG") != -1:
                    cursor.execute("""ALTER TABLE %s ADD %s LONGTEXT AFTER %s;""" % (table, i, ffild))
                elif i.find("TS") != -1:
                    cursor.execute("""ALTER TABLE %s ADD %s DATETIME AFTER %s;""" % (table, i, ffild))
                elif i.find("DT") != -1:
                    cursor.execute("""ALTER TABLE %s ADD %s DATE AFTER %s;""" % (table, i, ffild))
                elif i.find("DC") != -1:
                    cursor.execute("""ALTER TABLE %s ADD %s DECIMAL(5,2) AFTER %s;""" % (table, i, ffild))
                else:
                    cursor.execute("""ALTER TABLE %s ADD %s TEXT AFTER %s;""" % (table, i, ffild))
                
            dbSQL.commit()
    except:
        erro = 1
    try:
        for i in filename:
            d = i.split('\t')
            for j in d:
                idx = d.index(j)
                col = fd[idx]
                if col == ffild:
                    cursor.execute("""INSERT INTO %s(%s) VALUES ("%s");""" % (table,col,j))
                else:
                    cursor.execute("""UPDATE %s SET %s = "%s" WHERE %s = "%s";""" % (table,col,j,'timestamp',d[0]))
                dbSQL.commit()
    except:
        erro = 2
    dbSQL.close()
    try:
        if erro == 1:
            return "Erro na criação do banco de dados! Talvez o vome das colunas sejam incompatíveis com a sintaxe do mysql. Edite o arquivo CVS e altere o nome das colunas não use ascentos, espaços ou símbolos"
        elif erro == 2:
            return "Erro no registro das informações no banco de dados! É possível que um dos campos possua uma virgula. É necessário uniformizar os campos antes da importação."
    except:
        return "Arquivo importado com sucesso!!"
    

def importCVS2mySQL(filename, table, h, u, s, d):
    '''
    Realiza a insersão do conteudo do arquivo CVS no banco de dados.
    '''

    dbSQL = MySQLdb.connect(_host, _user, _passwd)
    cursor = dbSQL.cursor()
    try:
        cursor.execute("""CREATE DATABASE `%s` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;""" % d)
    except:
        pass
    cursor.execute("""USE %s;""" % d)
    fd = filename[0].split('|')
    ffild = fd[0]
    filename = filename[1:]
    try:
        for i in fd:
            if i == ffild:
                if i.find("INT") != -1:
                    cursor.execute("""CREATE TABLE %s(%s INT) ENGINE = InnoDB DEFAULT CHARACTER SET = utf8;;""" % (table, i))
                elif i.find("TS") != -1:
                    cursor.execute("""CREATE TABLE %s(%s DATETIME) ENGINE = InnoDB DEFAULT CHARACTER SET = utf8;;""" % (table, i))
                elif i.find("DT") != -1:
                    cursor.execute("""CREATE TABLE %s(%s DATE) ENGINE = InnoDB DEFAULT CHARACTER SET = utf8;;""" % (table, i))
                elif i.find("DC") != -1:
                    cursor.execute("""CREATE TABLE %s(%s DECIMAL(5,2) ENGINE = InnoDB DEFAULT CHARACTER SET = utf8;);""" % (table, i))
                else:
                    cursor.execute("""CREATE TABLE %s(%s TEXT) ENGINE = InnoDB DEFAULT CHARACTER SET = utf8;;""" % (table, i))
                
            else:
                if i.find("INT") != -1:
                    cursor.execute("""ALTER TABLE %s ADD %s INT AFTER %s;""" % (table, i, ffild))
                elif i.find("LG") != -1:
                    cursor.execute("""ALTER TABLE %s ADD %s LONGTEXT AFTER %s;""" % (table, i, ffild))
                elif i.find("TS") != -1:
                    cursor.execute("""ALTER TABLE %s ADD %s DATETIME AFTER %s;""" % (table, i, ffild))
                elif i.find("DT") != -1:
                    cursor.execute("""ALTER TABLE %s ADD %s DATE AFTER %s;""" % (table, i, ffild))
                elif i.find("DC") != -1:
                    cursor.execute("""ALTER TABLE %s ADD %s DECIMAL(5,2) AFTER %s;""" % (table, i, ffild))
                else:
                    cursor.execute("""ALTER TABLE %s ADD %s TEXT AFTER %s;""" % (table, i, ffild))
                
            dbSQL.commit()
    except:
        erro = 1
    try:
        for i in filename:
            d = i.split('|')
            for j in d:
                idx = d.index(j)
                col = fd[idx]
                if col == ffild:
                    cursor.execute("""INSERT INTO %s(%s) VALUES ("%s");""" % (table,col,j))
                else:
                    cursor.execute("""UPDATE %s SET %s = "%s" WHERE %s = "%s";""" % (table,col,j,'timestamp',d[0]))
                dbSQL.commit()
    except:
        erro = 2
    dbSQL.close()
    try:
        if erro == 1:
            return "Erro na criação do banco de dados! Talvez o vome das colunas sejam incompatíveis com a sintaxe do mysql. Edite o arquivo CVS e altere o nome das colunas não use ascentos, espaços ou símbolos"
        elif erro == 2:
            return "Erro no registro das informações no banco de dados! É possível que um dos campos possua uma virgula. É necessário uniformizar os campos antes da importação."
    except:
        return "Arquivo importado com sucesso!!"

def index(req):
   return """\
<!DOCTYPE html>
<html>
	<head><meta http-equiv="Content-Type" content="text/html;charset=utf-8"></head>
<body>
<form enctype="multipart/form-data" action="./upload1" method="post">
<p>Arquivo: <input type="file" name="file"></p>
<p>Nome do Banco de Dados: <input type="text" name="db"></p>
<p>Nome da Tabela: <input type="text" name="table"></p>
<p><input type="submit" value="Upload"></p>
</form>
</body></html>
"""

def upload1(req):
    try: # Windows needs stdio set for binary mode.
        import msvcrt
        msvcrt.setmode (0, os.O_BINARY) # stdin  = 0
        msvcrt.setmode (1, os.O_BINARY) # stdout = 1
    except ImportError:
        pass
    
    skell = '''<p>Coluna %s: <input type="text" name="%s" size="30" value="%s">
                    Formato dos dados: <select size="1" name="type%s">
                        <option value="text">Texto curto</option>
                        <option value="longtext">Parárafos</option>
                        <option value="str_num">String numérica sem pontuação</option>
                        <option value="int">Número inteiro</option>
                        <option value="decimal">Númer decimal</option>
                        <option value="datetime">Registo de tempo</option>
                        <option value="date">Data</option>
                    <select></p>'''    
    output = ''
    count = 1
    # A nested FieldStorage instance holds the file
    global _fileitem
    _fileitem = req.form['file']
    
    # Test if the file was uploaded
    if _fileitem.filename:
        for i in ReplaceEnclosed(_fileitem.file.readline()).replace('\n','').split('|'):
            output = output+skell % (count, count, i, count)
            count += 1
    
    return '''<!DOCTYPE html>
<html>
	<head><meta http-equiv="Content-Type" content="text/html;charset=utf-8"></head>
<body><form enctype="multipart/form-data" action="upload3" method="post">
%s
<input type="submit" value="Gravar"></form></body></html>''' % output

def upload3(req):
    o = ReplaceEnclosed(_fileitem.file.readline()).replace('\n','').split('|')
    return str(o)
    

def upload2(req, db, table):
    dbSQL = MySQLdb.connect(_host, _user, _passwd)
    cursor = dbSQL.cursor()
    try:
        cursor.execute("""CREATE DATABASE `%s` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;""" % db)
    except:
        pass
    cursor.execute("""USE %s;""" % db)
    try: # Windows needs stdio set for binary mode.
        import msvcrt
        msvcrt.setmode (0, os.O_BINARY) # stdin  = 0
        msvcrt.setmode (1, os.O_BINARY) # stdout = 1
    except ImportError:
        pass
    # A nested FieldStorage instance holds the file
    fileitem = req.form['file']
    # Test if the file was uploaded
    if fileitem.filename:
        lines = len(fileitem.file.readlines())
        fileitem.file.seek(0)
        cols = ''
        lastcol = ''
        while lines != 0:
            if fileitem.file.tell() == 0:
                cols = ReplaceEnclosed(fileitem.file.readline()).replace('\n','').split('|') #valor de split depende se é cvs ou tvs
                for i in cols:
                    if i == cols[0]:
                        if i.find("INT") != -1:
                            cursor.execute("""CREATE TABLE %s(%s INT) ENGINE = InnoDB DEFAULT CHARACTER SET = utf8;;""" % (table, i))
                        elif i.find("TS") != -1:
                            cursor.execute("""CREATE TABLE %s(%s DATETIME) ENGINE = InnoDB DEFAULT CHARACTER SET = utf8;;""" % (table, i))
                        elif i.find("DT") != -1:
                            cursor.execute("""CREATE TABLE %s(%s DATE) ENGINE = InnoDB DEFAULT CHARACTER SET = utf8;;""" % (table, i))
                        elif i.find("DC") != -1:
                            cursor.execute("""CREATE TABLE %s(%s DECIMAL(10,2) ENGINE = InnoDB DEFAULT CHARACTER SET = utf8;);""" % (table, i))
                        else:
                            cursor.execute("""CREATE TABLE %s(%s TEXT) ENGINE = InnoDB DEFAULT CHARACTER SET = utf8;;""" % (table, i))
                    else:
                        if i.find("INT") != -1:
                            cursor.execute("""ALTER TABLE %s ADD %s INT AFTER %s;""" % (table, i, lastcol))
                        elif i.find("LG") != -1:
                            cursor.execute("""ALTER TABLE %s ADD %s LONGTEXT AFTER %s;""" % (table, i, lastcol))
                        elif i.find("TS") != -1:
                            cursor.execute("""ALTER TABLE %s ADD %s DATETIME AFTER %s;""" % (table, i, lastcol))
                        elif i.find("DT") != -1:
                            cursor.execute("""ALTER TABLE %s ADD %s DATE AFTER %s;""" % (table, i, lastcol))
                        elif i.find("DC") != -1:
                            cursor.execute("""ALTER TABLE %s ADD %s DECIMAL(10,2) AFTER %s;""" % (table, i, lastcol))
                        else:
                            cursor.execute("""ALTER TABLE %s ADD %s TEXT AFTER %s;""" % (table, i, lastcol))
                    lastcol = i
                    dbSQL.commit()
            else:
                data = ReplaceEnclosed(fileitem.file.readline()).replace('\n','').split('|')                    
                for i in data:
                    idx = data.index(i)
                    col = cols[idx]
                    if col == cols[0]:
						if col.find('TS') != -1: #Timestampfix... Goolge2mySQL
							i = GoogleTS2mySQLDT(i)
						cursor.execute("""INSERT INTO %s(%s) VALUES ("%s");""" % (table,col,i))
                    else:
						if col.find('DC') != -1: #Decimal fix; incluir timestampfix...
							i = i.replace(',','.')
							if i == "": 
								cursor.execute("""UPDATE %s SET %s = NULL WHERE %s = "%s";""" % (table,col,cols[0],GoogleTS2mySQLDT(data[0]))) #esse timestamp precisa ser generalizado...
							else:
								cursor.execute("""UPDATE %s SET %s = "%s" WHERE %s = "%s";""" % (table,col,i,cols[0],GoogleTS2mySQLDT(data[0]))) #esse timestamp precisa ser generalizado...
						else:
							cursor.execute("""UPDATE %s SET %s = "%s" WHERE %s = "%s";""" % (table,col,i,cols[0],GoogleTS2mySQLDT(data[0]))) #esse timestamp precisa ser generalizado...
						dbSQL.commit()
            lines = lines - 1
    dbSQL.close()
    return """\
<!DOCTYPE html>
<html>
	<head><meta http-equiv="Content-Type" content="text/html;charset=utf-8"></head>
<body>
%s
</body></html>
""" % "Feito?!"
