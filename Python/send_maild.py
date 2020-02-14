#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""

@author: bwb0de
"""

#Base python modules import...
from time import sleep
from sys import platform
from os import sep, system, linesep
from telnetlib import Telnet

#App personal modules import
from modules.config.pathc import *
from modules.config.mail_e_whats import *
from modules.config.sps_var import *
from modules.config.unb_sigra import *
from modules.var_translation import *
from modules.db_skell import *


HOST='www.google.com'

while True:
	try:
		tn=Telnet(HOST,80)
		connection = True
	except: connection = False
	if connection == True:
		try: fila = dict(engine.execute(select(mail_outbox_q.c)).fetchone())
		except: fila = None
		if fila == None:
			pass
		else:
			send_email_op(fila['dest'], fila['subject'].encode('utf-8'), fila['msg'].encode('utf-8'), fila['sender'], fila['pwd'], fila['smtpserver'], int(fila['smtpport']))
			engine.execute(mail_outbox_q.delete().where(mail_outbox_q.c.id == fila['id']))
			engine.execute(mail_outbox.insert().values({'uid': fila['uid'], 'timestamp': make_timestamp(), 'dest': fila['dest'], 'subject': fila['subject'].encode('utf-8'), 'msg': fila['msg'].split('---')[0].encode('utf-8'), 'semestre': semestre}))
			#print "   - Mensagem de email encaminhada para %s..." % fila['dest']
		try: fila_whats = dict(engine.execute(select(whatsapp_outbox_q.c)).fetchone())
		except: fila_whats = None
		if fila_whats == None:
			pass
		else:
			if platform == 'win32':
				cmd = ['python', yowsroot+sep+'yowsup-cli', 'demos', '-s', unicode(fila_whats['dest']), fila_whats['msg'], '-c', spsroot+sep+'whatsapp.conf', '-M']
			else:
				cmd = [yowsroot+sep+'yowsup-cli', 'demos', '-s', unicode(fila_whats['dest']), fila_whats['msg'], '-c', spsroot+sep+'whatsapp.conf', '-M']
			system(' '.join(cmd).encode("utf8"))
			engine.execute(whatsapp_outbox_q.delete().where(whatsapp_outbox_q.c.id == fila_whats['id']))
			engine.execute(whatsapp_outbox.insert().values({'uid': fila_whats['uid'], 'timestamp': make_timestamp(), 'dest': fila_whats['dest'], 'msg': fila_whats['msg'].replace(msg_alerta_whatsout,''), 'semestre': semestre}))
			#print linesep + unicode("   - Mensagem WhatsApp encaminhada para %s..." % fila_whats['dest']).encode("utf8")
	else:
		pass
		#print "Sem conexão com a internet..."
	sleep(20)
