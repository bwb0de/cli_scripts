# -*- coding: utf-8 -*-

NOME = 'Email'

from multiprocess_prog import *
from smtplib import SMTP

def enviar_email(destlist, subject, msg, sender, pwd, smtpserver='mail.unb.br', smtpport=587):
	smtpserver = SMTP(smtpserver, smtpport)
	smtpserver.ehlo()
	smtpserver.starttls()
	smtpserver.ehlo
	smtpserver.login(sender, pwd)
	targets = destlist.replace(' ', '').split(',')
	o = []
	for i in targets:
		header = 'To:' + i + os.linesep + 'From: ' + sender + os.linesep + 'Subject:' + subject + os.linesep
		msgcorpus = header + os.linesep + msg + os.linesep*2
		smtpserver.sendmail(sender, i, msgcorpus.encode('utf-8'))
		smtpserver.sendmail(sender, sender, msgcorpus.encode('latin1'))
		o.append((i,subject,msg))
	smtpserver.close()
	return o


class this_process(subprocess_instance):
	def __init__(self, NOME):
		subprocess_instance.__init__(self, NOME)
		self.NOME = NOME
		
	def run(self, m):
		lock_main()
		m.destlist = 'danielc@unb.br'
		m.subject = input('Assunto: ')
		m.msg = input('Mensagem: ')
		m.sender = 'danielc@unb.br'
		m.pwd = 'bwb0de'
		enviar_email(m.destlist, m.subject, m.msg, m.sender, m.pwd)
		remove(path.join(proc_msg, m.idx))
		unlock_main()

subproc = this_process(NOME)
subproc.routine_check()
