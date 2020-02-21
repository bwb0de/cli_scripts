#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#
# 2doList
#
# [ ] ...
#

from datetime import datetime

import time

try:
    import MySQLdb
except:
    pass
	
########################################
### DATA BASE CONFIGURATION          ###
########################################

dbname = 'spsdb'
host='localhost'
user='root'
passwd='1234'

dbSQL = MySQLdb.connect(host=host, user=user, passwd=passwd)
cursor = dbSQL.cursor()

### Estrutura do banco de dados
#
# Caso a estrutura de dados ainda não tenha sido criada pelo banco de dados, 
# o método 'index' irá executar essa ação com base na estrutura definida no
# dicionário 'dbfilds'. Cada chave do dicionário representa uma tabela...
# Os valores vinculados às chaves constituem as colunas da tabela.
#
# Por padrão, as colunas criadas são do tipo texto, elas, contudo, podem ser alteradas
# ao se adicionar as tags definidas abaixo:
#
#  - [nome da coluna]#LG
#  - [nome da coluna]#INT
#

dbfilds = {}
#T00 - METATAB
dbfilds['METATAB'] = ['varvalue', 'varname']

#T01 - Histórico de atendimentos
dbfilds['T01'] = ['tipo', 'publico', 'matrícula', 'timestamp']

#T02 - Histórico de recursos
dbfilds['T02'] = ['justificativa#LG', 'resposta', 'pendente', 'detalhamento#LG', 'assunto', 'fone', 'email', 'nome', 'matrícula', 'timestamp']

#T03 - Histórico de solicitações
dbfilds['T03'] = ['justificativa#LG', 'resposta', 'pendente', 'detalhamento#LG', 'assunto', 'fone', 'email', 'nome', 'matrícula', 'timestamp']

#T04 - Histórico de dúvidas
dbfilds['T04'] = ['justificativa#LG', 'resposta', 'pendente', 'detalhamento#LG', 'assunto', 'fone', 'email', 'nome', 'matrícula', 'timestamp']

#T05 - Histórico de entrega de documentos
dbfilds['T05'] = ['tipo', 'nome', 'matrícula', 'timestamp']

#T06 - Histórico de encaminhamentos
dbfilds['T06'] = ['cprofenc', 'profenc', 'inst_setor', 'oficio', 'data', 'detalhamento#LG', 'nome', 'matricula', 'timestamp']

#T07 - Histórico de assinatura de termos
dbfilds['T07'] = ['cc', 'ag', 'banco', 'renov', 'termos', 'cpf', 'name', 'matricula', 'timestamp']

#T08 - Estudos em curso
dbfilds['T08'] = ['nome', 'matricula', 'timestamp']

#T09 - Estudantes ativos
dbfilds['T09'] = ['renov', 'nome', 'matricula', 'timestamp']

#T10 - Histórico de desligamentos
dbfilds['T10'] = ['motivo', 'nome', 'matrícula', 'timestamp']

#T11 - Estudantes inativos
dbfilds['T11'] = []

#T12 - Histórico de movimentação de pastas
dbfilds['T12'] = []

#T13 - Histórico de estudos socioeconômicos dos usuários
dbfilds['T13'] = []

#T14 - Histórico de entrevistas da moradia estudantil
dbfilds['T14'] = []

#T15 - Histórico de emergenciais
dbfilds['T15'] = []

#T16 - Histórico de monitoramento acadêmico
dbfilds['T16'] = []

#T17 - Usuários do sistema
dbfilds['T17'] = []

#T18 - Histórico de atividades dos usuários
dbfilds['T18'] = []

#T19 - Histórico de casos para observar
dbfilds['T19'] = []


#########################################
### FUNCTIONS                        ####
#########################################

def MySQLdb_DropLine(idn, table, h=host,u=user,s=passwd,d=dbname):
    cursor.execute("""USE %s;""" % d)
    cursor.execute("""DELETE FROM %s WHERE idn = "%s";""" % (table,idn))
    dbSQL.commit()

def MySQLdb_ReadCell(idn,table,col,h=host,u=user,s=passwd,d=dbname):
    cursor.execute("""USE %s;""" % d)
    cursor.execute("""SELECT %s FROM %s WHERE idn = "%s";""" % (col,table,idn))
    l = cursor.fetchall()
    return l

def MySQLdb_ReadCol(col, table, h=host,u=user,s=passwd,d=dbname):
    cursor.execute("""USE %s;""" % d)
    cursor.execute("""SELECT %s FROM %s;""" % (col, table))
    l = cursor.fetchall()
    return l

def MySQLdb_WriteCell(table,col,writedata,input_val_in_col,val,h=host,u=user,s=passwd,d=dbname):
    cursor.execute("""USE %s;""" % d)
    cursor.execute("""UPDATE %s SET %s = "%s" WHERE %s = "%s";""" % (table,col,writedata,input_val_in_col,val))
    dbSQL.commit()

def MySQLdb_CreateLine(table,col,val,h=host,u=user,s=passwd,d=dbname):
    cursor.execute("""USE %s;""" % d)
    cursor.execute("""INSERT INTO %s(%s) VALUES ("%s");""" % (table,col,val))
    dbSQL.commit()

def MySQLdb_CreateDBFilds(dbname):
	try:
		cursor.execute("""CREATE DATABASE %s;""" % dbname)
	except:
		pass
		
	try:
		cursor.execute("""USE %s;""" % dbname)
		for i in dbfilds.keys():
			cursor.execute("""CREATE TABLE %s(IDN INT);""" % i)
			for col in dbfilds[i]:
				if col.find('#LG') != -1:
					cursor.execute("""ALTER TABLE %s ADD %s longtext AFTER IDN;""" % (i, col.replace('#LG','')))
				elif col.find('#INT') != -1:
						cursor.execute("""ALTER TABLE %s ADD %s int AFTER IDN;""" % (i, col.replace('#INT','')))
				else:
					cursor.execute("""ALTER TABLE %s ADD %s text AFTER IDN;""" % (i, col))
				dbSQL.commit()
		MySQLdb_CreateLine('metatab','nome_var','idcount')
		MySQLdb_WriteCell('metatab','valor_var',0,'nome_var','idcount')
	except:
		pass
	
def GetCurrentID():
    cursor.execute("""USE %s;""" % dbname)
    cursor.execute("""SELECT valor_var FROM metatab WHERE nome_var = "idcount";""")
    idn = cursor.fetchall()[0][0]
    return idn

def CreateNewID():
    idn = int(GetCurrentID()) + 1
    idn = str(idn)
    MySQLdb_WriteCell('metatab','valor_var',idn,'nome_var','idcount')
    return idn

def CountDB(col, table, h=host,u=user,s=passwd,d=dbname):
    cursor.execute("""USE %s;""" % d)
    r = MySQLdb_ReadCol(col, table)
    tmp_lst = []
    for i in r:
        tmp_lst.append(i[0])
    tmp_lst.sort()
    tmp_lst_entries = set(tmp_lst)
    output = {}
    for i in tmp_lst_entries:
        output[i] = [tmp_lst.count(i)]
    return output

def FindDuplicateCPF(cpf,tabela,h=host,u=user,s=passwd,d=dbname):
    cursor.execute("""USE %s;""" % d)
    cursor.execute("""SELECT idn FROM %s WHERE cpf = "%s";""" % (tabela,cpf))
    try:    
        r = int(cursor.fetchall()[0][0])
    except:
        r = None
    return r

def TimeStamp():
    r = time.strftime("%Y-%m-%d %H:%M:%S") #Adicionar USERNAME@COMPUTADOR
    return r

#########################################
### WEB TEMPLATES, LAYOUTS & FORMS   ####
#########################################

#Layout principal
main_page = '''
<!DOCTYPE html>
<html>
	<head><meta http-equiv="Content-Type" content="text/html;charset=utf-8" ><title>NRADDB®</title>
		<script type='text/javascript'>				
			function taskDone(msg){alert(msg);}
			function changeEventHandler(event)
				{
				switch(event.target.value)
					{
					case "perfil":
					document.getElementById("form2addquestion").style.display = "block";
					break;
					case "nperfil":
					document.getElementById("form2addquestion").style.display = "none";
					break;
					case "outro":
					document.getElementById("form2addquestion2").style.display = "block";
					break;
					default:
					break
					}
				}
		</script>
		<style type="text/css">
			#header
				{
				background-color: #f60100;
				margin-left: -10px;
				margin-top: -10px;
				margin-right: -8px;
				height: 100px;
				}
			#topleft 
				{
				position:absolute;
				width: 200px;
				height: 200px;
				margin-left: 15px;
				margin-top: -75px;
				background-image: url();
				border: 5px solid;
				border-color: #f3f2f0;
				border-radius: 5px;
				}
			#fastlink 
				{
				position:absolute;
				width: 200px;
				margin-left: 30px;
				margin-top: 140px;
				font-size: 14px;
				}
			#corpus
				{
				position:absolute;
				margin-left: 245px;
				margin-top: 0px;
				margin-right: 0px;
				}
			#pagetitle
				{
				position:absolute;
				margin-left: 245px;
				margin-top: -65px;
				margin-right: -8px;
				font-family: "Verdana";
				font-weight: bold;
				font-size: 40px;
				color: black;
				}
			#form2addquestion
				{
				position:relative;
				display:none;
				}
			#form2addquestion2
				{
				position:relative;
				display:none;
				}				
			#hide
				{
				position:relative;
				display:none;
				}
			#hint
				{
				position:relative;
				font-size: 10px;
				}
			body
				{
				background-color: #00a2ff;
				font-family: "Verdana";
				font-size: 14px;
				color: white;
				}
			table
				{
				font-family: "Verdana";
				font-size: 14px;				
				}
			a{color: white;}
		</style>
	</head>
	<body onLoad="#ERRO#">
		<div id="header"><br></div>
		<div id="pagetitle"><t1>NRADDB</t1></div>
		<div id="corpus">#NFO#</div>
		<div id="topleft"><a href="../index"><img src="https://lh3.googleusercontent.com/-WoCpTiapey8/VUN1dVMtLxI/AAAAAAAABo0/P0OR6QRGfo8/s200-no/nraddb200.jpg"><a></div>
		<div id="fastlink">
			<h2>Links rápidos</h2>
				<li><a href="../#####">#####</a>
				<li><a href="../#####">#####</a>
				<li><a href="../#####">#####</a>
				<li><a href="../#####">#####</a>
				<li><a href="../#####">#####</a>
		</div>
	</body>
</html>'''

#Página inicial
wellcome=''''''

#Tela de login do administrador
form0 = '''
                <form method="POST" action="./%s">
                	<table cellspacing="2" cellpadding="2" border="0">
                		<tr>
                			<td width=180 align=right>Usuário:</td>
                			<td><input type="text" name="user" size="20"></td>
                		</tr>
                		<tr>
                			<td width=180 align=right>Senha:</td>
                			<td><input type="password" name="keyword" size="20"></td>
                		</tr>
                		<tr>
                			<td width=180 align=right></td>
                			<td><input type="submit" value="Login">
                		</tr>
                	</table>
                </form>''' % ('form0_action') #Inserir aqui o nome da função de ação...

#Formulário pré-admissional
form1 = '''
                <form method="POST" action="./%s" onload="#ERRO#">
                	<table cellspacing="2" cellpadding="2" border="0">
                		<tr><h2>TÍTULO DA SEÇÃO</h2></tr>
                		<tr>
                			<td width=180 align=right>Matrícula:</td>
                			<td><input type="text" name="nome" size="20"></td>
                		</tr>
                		<tr>
                			<td width=180 align=right></td>
                			<td><div id="hint">Usar o formato DD/MM/AAAA...</div></td>
                		</tr>
                		<tr>
                			<td width=180 align=right></td>
                			<td><br><input type="submit" value="Registrar">
                		</tr>
                	</table>
                </form>''' % ('form1_action') #Inserir aqui o nome da função de ação...

#Avaliação admissional
lista_de_estudantes = '''
                <table cellspacing="2" cellpadding="2" border="0">
                	<tr><h2>%s</h2></tr>
                	<tr>
                		<td width=90 align=center><strong>Data 1ªVD</strong></td>
                		<td width=220><strong>Paciente</strong></td>
                		<td width=130 align=center><strong>CPF</strong></td>
                	</tr>
                	#LST#
                </table>'''

#Item de lista
item_de_lista_estudante = '''
                <form method="POST" action="../#####">
                	<tr>
                		<td align=center>%s</td>
                		<td>%s</td>
                		<td align=center>%s</td>
                		<td><div id="hide">
							<input type="text" name="idn" size="1" value="%s"></div>
							<input type="submit" value="Registrar avaliação">
						</td>
                	</tr>
                </form>'''


form2 = '''
                <form id="f2" method="POST" action="../form2_action">
                <div id="hide"><input type="text" name="idn" size="1" value="%s"></div>
                <table cellspacing="2" cellpadding="2" border="0">
                	<tr><h2>Registro da avaliação de: %s</h2></tr>
                	<tr>
                		<td align=right><strong>Resultado:</strong></td>
                		<td>
                			<select size="1" onchange="changeEventHandler(event);" name="result">
                				<option value="nperfil">Paciente não adequado à internação domiciliar</option>
                				<option value="perfil">Paciente adequado à internação domiciliar</option>
                			<select>
                		</td>
                	</tr>
                </table>
                
                <div id="form2addquestion">
                <table>
                	<tr>
                		<td width=180 align=right><strong>Data de internação:</strong></td>
                		<td><input type="text" name="data_int"></td>
                	</tr>
                	<tr>
                		<td width=180 align=right><strong>Classificação:</strong></td>
                		<td>
                			<select size="1" name="classific">
                				<option value="pid">PID</option>
                				<option value="pod">POD</option>
                				<option value="pid&pod">PID/POD</option>
                			<select>
                		</td>
                	</tr>
                	<tr>
                		<td width=180 align=right style="vertical-align: text-top"><strong>Equipamentos?</strong></td>
                		<td><input type="checkbox" name="equip" value="maca">Maca<br>
                			<input type="checkbox" name="equip" value="clindrO2">Cilíndro de Oxigênio<br>
                			<input type="checkbox" name="equip" value="soro">Suporte para soro<br>
                			<input type="checkbox" name="equip" value="outro" onchange="changeEventHandler(event);">Outro<div id="form2addquestion2"><input type="text" size="20" name="otherequip">
                			
                		</td>
                	</tr>
                	<tr>
                		<td></td>
                		<td><div id="hint">Deixar em branco se não houver equipamentos emprestados...</div></td>
                </table></div>
                <div><strong>Observações, justificativas ou procedimentos de encaminhamento:</strong></div>
                <div><textarea rows="7" cols="80" name="obs" form="f2"></textarea></div>
                <div align=right><input type="submit" value="Registrar"></div>
                </form>'''


def index(req):
    #Preparação do banco de dados, caso não exista...
    MySQLdb_CreateDBFilds(dbname)
    	
    #Carregando informações estatísticas do banco de dados...
    	
    #Carregando página inicial
    return main_page.replace("#NFO#", wellcome)

def form1_page(req): #Formulário pré-admissional
    return main_page.replace("#NFO#", form1)

def form1_action(req):
    #Recebendo informações do formulário: inputfilds
    $$$ = req.form.getfirst('$$$')
        
    #Verificando a existência de duplicatas
    if FindDuplicateCPF(cpf, 't4') == None:       
        old_idn = FindDuplicateCPF(cpf, 't1')
        if FindDuplicateCPF(cpf, 't1') == None:
            pass
        else:
            #Obtendo informações do banco de dados a partir da variável identificadora old_idn...
            old_nome = MySQLdb_ReadCell(old_idn,'t1','nome')[0][0]
            
            #Registrando informações antigas na tabela 2, para evitar duplicatas...
            MySQLdb_CreateLine('t2','idn',old_idn)
            MySQLdb_WriteCell('t2','nome',old_nome,'idn',old_idn)
            
            #Excluindo informações antigas de t1...
            MySQLdb_DropLine(old_idn, 't1')
        
        idn = CreateNewID()
        timestamp = TimeStamp()
        
        #Registrando no banco de dados em t1, t2, t3...
        MySQLdb_CreateLine('t1','idn',idn)
        MySQLdb_WriteCell('t1','nome',nome,'idn',idn)
        
        MySQLdb_CreateLine('t3','idn',idn)
        MySQLdb_WriteCell('t3','nome',nome,'idn',idn)
        
        #Recarregando o formulário
        return main_page.replace("#NFO#", form1)
    else:
        return main_page.replace("#NFO#", form1).replace("#ERRO#", "taskDone('O paciente já está registrado como ativo! As informações não foram gravadas no Banco de Dados...')")

def form3_page(req):
	idn = req.form.getfirst('idn')
	
	#Obtendo informações do banco de dados a partir da variável identificadora [timestamp]
	$$$ = MySQLdb_ReadCell(idn,'t1','$$$')[0][0]
	
	#Carregando a página de saída com as informações obtidas.
	return main_page.replace("#NFO#", form3 % ($$$))
