# -*- coding: utf-8 -*-

NOME = 'MSG Agent 2'

from multiprocess_prog import *

class this_process(subprocess_instance):
	def __init__(self, NOME):
		subprocess_instance.__init__(self, NOME)
		self.NOME = NOME
		
	def run(self, m):
		print(NOME)
		remove(path.join(proc_msg, m.idx))


subproc = this_process(NOME)
subproc.routine_check()

