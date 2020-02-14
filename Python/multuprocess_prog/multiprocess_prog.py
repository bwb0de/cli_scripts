# -*- coding: utf-8 -*-

from os import getcwd, path, remove, listdir
from subprocess import check_output, Popen
from signal import SIGTERM

import time
import io
import os
import pickle


#NOME, INITSTATUS
daemons=[\
('maild.py', True),
('msgagent.py', True)]



app_root_folder = getcwd()
proc_folder= path.join(app_root_folder, 'proc')
scripts_folder= path.join(app_root_folder, 'scripts')
proc_msg= path.join(proc_folder, 'msg')

class process_msg:
	def __init__(self, NOME):
		self.idx = str(time.time()).replace('.','').zfill(20)
		self.nome = NOME

class subprocess_instance:
	def __init__(self, NOME):
		self.NOME = NOME
		
	def run(self):
		pass
		
	def routine_check(self):
		while True:
			time.sleep(2.5)
			procs_msg = listdir(proc_msg)
			for msg in procs_msg:
				m = check_msg(msg, self.NOME)
				if m != False:
					self.run(m)

def check_msg(msg, NOME):
	m = read_pickle(msg, proc_msg)
	if m.nome == NOME:
		return m
	else:
		return False

def read_pickle(obj_file, folder):
	obj_file_io = io.open(os.path.join(folder, obj_file),'rb')
	OBJ = pickle.load(obj_file_io)
	return OBJ


def write_pickle(OBJ, folder, filename=None):
	if filename == None:
		obj_file = io.open(os.path.join(folder, str(OBJ.idx).zfill(3)),'wb')
	else:
		obj_file = io.open(os.path.join(folder, filename),'wb')
	pickle.dump(OBJ, obj_file)
	obj_file.close()


def lock_main():
	main_init_status = process_msg('main')
	main_init_status.idx = 'main'
	main_init_status.lock_status = True
	write_pickle(main_init_status, proc_msg)

def unlock_main():
	main_init_status = process_msg('main')
	main_init_status.idx = 'main'
	main_init_status.lock_status = False
	write_pickle(main_init_status, proc_msg)	

def exit_app():
	procs = listdir(proc_folder)
	for proc in procs:
		try: remove(path.join(proc_folder, proc))
		except: pass
	exit()
	

def main():
	while True:
		try: 
			lock_main = read_pickle('main', proc_msg)
		except: 
			unlock_main()
			lock_main = read_pickle('main', proc_msg)
		if lock_main.lock_status == False:
			NOME = input('Indique o ID do processo:')
			if NOME == 'exit':
				exit_app()
			else:
				msg = process_msg(NOME)
				write_pickle(msg, proc_msg)
				time.sleep(2.6)
				
		else:
			time.sleep(2.5)
			
	

def start_app_subprocess():
	for i in daemons:
		if i[1] == True:
			print(u" * Starting script-daemon {}...".format(i[0]))
			cmd = ['python', path.join(app_root_folder, i[0])]
			daemon = Popen(cmd)
			f = open(path.join(proc_folder, i[0].split('.')[0]),'w')
			f.write(str(daemon.pid))
			f.close()
		else:
			print(u" * Skipping script-daemon {}...".format(i[0]))



if __name__ == '__main__':
	start_app_subprocess()
	time.sleep(1)
	print(u" * Starting main app multiprocess controller...")
	main()
