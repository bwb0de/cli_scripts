#!/usr/bin/env python
# -*- coding: UTF-8 -*-

server_folder='/var/www'
server_folder_wdp='/var/www/wdp'

def wdp_install(nickname, mySQLuser, mySQLpass, serverIP):
	#Cria banco de dados no servidor MySQL via shell nickname é definido pelas: 3 primeiras do nome +; 3 primeiras letras último nome +; turma a que o aluno pertence...
	mysql_exec='mysql -u%s -p%s -e "CREATE DATABASE dbedu_wdp_%s"' % (nickname, mySQLuser, mySQLpass)
	os.system(mysql_exec)

	#Copia o arquivo com o wordpress para a pasta do servidor de mesmo nome que o nickname
	f = open('wdp.tar.bz2', 'r')
	fd = f.read()
	f.close()
	dbedu_dir = os.getcwd()
	os.chdir(server_folder_wdp)
	os.mkdir(nickname)
	os.chdir(nickname)
	f = open('wdp.tar.bz2', 'w')
	f.write(fd)
	f.close()
	
	#Descompacta o arquivo e criar hardlinks para os templates
	wdp_decomp='tar -xjf wdp.tar.bz2; rm -f wdp.tar.bz2'
	os.system(wdp_decomp)
	#criar os hardlinks...
	os.link(src, dst)
	
	#Configura a cópia do blog de acordo com o nickname
	wdp_conf='''<?php
	/** 
	 * The base configurations of the WordPress.
	 *
	 * This file has the following configurations: MySQL settings, Table Prefix,
	 * Secret Keys, WordPress Language, and ABSPATH. You can find more information by
	 * visiting {@link http://codex.wordpress.org/Editing_wp-config.php Editing
	 * wp-config.php} Codex page. You can get the MySQL settings from your web host.
	 *
	 * This file is used by the wp-config.php creation script during the
	 * installation. You don't have to use the web site, you can just copy this file
	 * to "wp-config.php" and fill in the values.
	 *
	 * @package WordPress
	 */

	// ** MySQL settings - You can get this info from your web host ** //
	/** The name of the database for WordPress */
	define('DB_NAME', '%s');

	/** MySQL database username */
	define('DB_USER', '%s');

	/** MySQL database password */
	define('DB_PASSWORD', '%s');

	/** MySQL hostname */
	define('DB_HOST', '%s');

	/** Database Charset to use in creating database tables. */
	define('DB_CHARSET', 'utf8');

	/** The Database Collate type. Don't change this if in doubt. */
	define('DB_COLLATE', '');

	/**#@+
	 * Authentication Unique Keys.
	 *
	 * Change these to different unique phrases!
	 * You can generate these using the {@link https://api.wordpress.org/secret-key/1.1/ WordPress.org secret-key service}
	 *
	 * @since 2.6.0
	 */
	define('AUTH_KEY', 'put your unique phrase here');
	define('SECURE_AUTH_KEY', 'put your unique phrase here');
	define('LOGGED_IN_KEY', 'put your unique phrase here');
	define('NONCE_KEY', 'put your unique phrase here');
	/**#@-*/

	/**
	 * WordPress Database Table prefix.
	 *
	 * You can have multiple installations in one database if you give each a unique
	 * prefix. Only numbers, letters, and underscores please!
	 */
	$table_prefix  = 'wp_';

	/**
	 * WordPress Localized Language, defaults to English.
	 *
	 * Change this to localize WordPress.  A corresponding MO file for the chosen
	 * language must be installed to wp-content/languages. For example, install
	 * de.mo to wp-content/languages and set WPLANG to 'de' to enable German
	 * language support.
	 */
	define ('WPLANG', '');

	/* That's all, stop editing! Happy blogging. */

	/** WordPress absolute path to the Wordpress directory. */
	if ( !defined('ABSPATH') )
		define('ABSPATH', dirname(__FILE__) . '/');

	/** Sets up WordPress vars and included files. */
	require_once(ABSPATH . 'wp-settings.php');
	?>''' % (nickname, mySQLuser, mySQLpass, serverIP)
	
	f = open('wp-config.php','w')
	f.write(wdp_conf)
	f.close()
	
	#Adiciona endereço do blog à lista de blogs...
	blog_link = 'http://%s/wdp/%s/' (serverIP, nickname)
	import dbwdplist
	blog_list = dbwdplist.blog_list
	blog_list[turma][num][nome] = blog_link
	f = open('dbwdplist.py','w')
	f.write('blog_list='+str(blog_list))
	f.close()
