#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os, sys

### Configurando variáveis
#Usuário do mySQL
mySQLid=''
#Senha do mySQL
mySQLpw=''
#IP do servidor
sIP='localhost'
#Pasta do servidor HTML
server_folder='/var/www'
#Pasta com arquivos do WordPress
server_folder_wdp='/var/www/wdp'
#Subpasta com temas do WordPress
src = '/var/www/wdp-themes'

### Variáveis internas
server_folder_newwdp = server_folder_wdp + '/' + nickname + '/wp-content/themes'
nickname = sys.argv[1]



def mkdirstruct(y, x):#, tag):
	os.chdir(y)
	lista = os.listdir('.')
	for i in lista:
		result = os.system('test -d "%s"' % i)
		if result == 0:
			newfold = i
			newdest = x + '/' + i
			os.mkdir(newdest)
			mkdirstruct(newfold, newdest)
	os.chdir('..')
	
def mkhardlinks(y, x):
	os.chdir(y)
	lista = os.listdir('.')
	for i in lista:
		result = os.system('test -d "%s"' % i)
		if result == 0:
			newfold = i
			newdest = x + '/' + i
			mkhardlinks(newfold, newdest)
		else:
			newdest = x + '/' + i
			os.link(i, newdest)
	os.chdir('..')


def wdp_install(nick, mySQLuser=mySQLid, mySQLpass=mySQLpw, serverIP=sIP):
	#Cria banco de dados no servidor MySQL via shell nickname é definido pelas: 3 primeiras do nome +; 3 primeiras letras último nome +; turma a que o aluno pertence...
	mysql_exec='mysql -u%s -p%s -e "CREATE DATABASE dbedu_wdp_%s"' % (mySQLuser, mySQLpass, nick)
	os.system(mysql_exec)

	#Copia o arquivo com o wordpress para a pasta do servidor de mesmo nome que o nickname
	f = open('wdp.tar.bz2', 'r')
	fd = f.read()
	f.close()
	dbedu_dir = os.getcwd()
	os.chdir(server_folder_wdp)
	os.mkdir(nick)
	os.chdir(nick)
	f = open('wdp.tar.bz2', 'w')
	f.write(fd)
	f.close()
	
	#Descompacta o arquivo e criar hardlinks para os templates
	wdp_decomp='tar -xjf wdp.tar.bz2; rm -f wdp.tar.bz2'
	os.system(wdp_decomp)
		
	#Configura a cópia do blog de acordo com o nickname
	wdp_conf='''<?php
/** 
 * As configurações básicas do WordPress.
 *
 * Esse arquivo contém as seguintes configurações: configurações de MySQL, Prefixo de Tabelas,
 * Chaves secretas, Idioma do WordPress, e ABSPATH. Você pode encontrar mais informações
 * visitando {@link http://codex.wordpress.org/Editing_wp-config.php Editing
 * wp-config.php} Codex page. Você pode obter as configuraçções de MySQL de seu servidor de hospedagem.
 *
 * Esse arquivo é usado pelo script ed criação wp-config.php durante a
 * instalação. Você não precisa usar o site, você pode apenas salvar esse arquivo
 * como "wp-config.php" e preencher os valores.
 *
 * @package WordPress
 */

// ** Configurações do MySQL - Você pode pegar essas informações com o serviço de hospedagem ** //
/** O nome do banco de dados do WordPress */
define('DB_NAME', 'dbedu_wdp_%s');

/** Usuário do banco de dados MySQL */
define('DB_USER', '%s');

/** Senha do banco de dados MySQL */
define('DB_PASSWORD', '%s');

/** nome do host do MySQL */
define('DB_HOST', '%s');

/** Conjunto de caracteres do banco de dados a ser usado na criação das tabelas. */
define('DB_CHARSET', 'utf8');

/** O tipo de collate do banco de dados. Não altere isso se tiver dúvidas. */
define('DB_COLLATE', '');

/**#@+
 * Chaves únicas de autenticação.
 *
 * Altere cada chave para um frase única!
 * Você pode gerá-las usando {@link http://api.wordpress.org/secret-key/1.1/ WordPress.org secret-key service}
 * Você pode alterá-las a qualquer momento para desvalidar quaisquer cookies existentes. Isto irá forçar todos os usuários a fazer login novamente.
 *
 * @since 2.6.0
 */
define('AUTH_KEY', 'coloque sua frase única aqui');
define('SECURE_AUTH_KEY', 'coloque sua frase única aqui');
define('LOGGED_IN_KEY', 'coloque sua frase única aqui');
define('NONCE_KEY', 'coloque sua frase única aqui');
/**#@-*/

/**
 * Prefixo da tabela do banco de dados do WordPress.
 *
 * Você pode ter várias instalações em um único banco de dados se você der para cada um um único
 * prefixo. Somente números, letras e sublinhados!
 */
$table_prefix  = 'wp_';

/**
 * O idioma localizado do WordPress é o inglês por padrão.
 *
 * Altere esta definição para localizar o WordPress. Um arquivo MO correspondente a
 * língua escolhida deve ser instalado em wp-content/languages. Por exemplo, instale
 * pt_BR.mo em wp-content/languages e altere WPLANG para 'pt_BR' para habilitar o suporte
 * ao português do Brasil.
 */
define ('WPLANG', 'pt_BR');

/* Isto é tudo, pode parar de editar! :) */

/** Caminho absoluto para o diretório Wordpress. */
if ( !defined('ABSPATH') )
	define('ABSPATH', dirname(__FILE__) . '/');
	
/** Configura as variáveis do WordPress e arquivos inclusos. */
require_once(ABSPATH . 'wp-settings.php');
?>''' % (nick, mySQLuser, mySQLpass, serverIP)
	
	f = open('wp-config.php','w')
	f.write(wdp_conf)
	f.close()
	
	#Adiciona endereço do blog à lista de blogs...
	'''blog_link = 'http://%s/wdp/%s/' (serverIP, nick)
	import dbwdplist
	blog_list = dbwdplist.blog_list
	blog_list[turma][num][nome] = blog_link
	f = open('dbwdplist.py','w')
	f.write('blog_list='+str(blog_list))
	f.close()'''

print 'Criando blog...'
wdp_install(nickname)
print 'Criando estruturas de diretórios para templates...'
mkdirstruct(src, server_folder_newwdp)
print 'Gerando hardlinks para temas...'
mkhardlinks(src, server_folder_newwdp)
