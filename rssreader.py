#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import urllib, sys, xml.dom.minidom

def readfeed(x):
	document = xml.dom.minidom.parse(urllib.urlopen(x))
	for item in document.getElementsByTagName('item'):
		title = item.getElementsByTagName('title')[0].firstChild.data
		link = item.getElementsByTagName('link')[0].firstChild.data
		cat = item.getElementsByTagName('category')[0].firstChild.data
		print \
		"Título: " + str(title.encode('utf8','replace')) + '\n' +\
		"Ligação: " + str(link.encode('utf8','replace')) + '\n' +\
		"Categorias: " + str(cat.encode('utf8','replace')) + '\n'

#criar uma saída de dados (web) para organizar, visualizar conteúdos dos professores...
 #tal qual postagens de um blog...


def google_translate(from_lang, to_lang, text):
	params = urllib.urlencode({"langpair":"%s|%s" %(from_lang, to_lang), "text":text,"ie":"UTF8", "oe":"UTF8"})
	conn = httplib.HTTPConnection("translate.google.com")
	conn.request("POST", "/translate_t", params)
			
	resp = conn.getresponse()
	s = resp.read()
	conn.close()
			
	match = re.compile('<textarea name=q.*?>(.*?)</textarea>',re.DOTALL).search(s)
	data = match.groups()[0]
	return unicode(data, "utf-8").strip()
