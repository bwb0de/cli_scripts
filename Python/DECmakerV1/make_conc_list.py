#!/usr/bin/env python
#
#

from os import remove

f = open('opa', 'r')
backup = open('original', 'w')
fh = f.read()
backup.write(str(fh))
backup.close()
f.close()

f = open('opa', 'ra+')
fh = f.read()
output = open('output', 'w+')
loop = fh.count('\n')
while loop != 0:
	pox1 = fh.index('\n')
	f.seek(pox1)
	f.write(';')
	f.close()
	f = open('opa', 'ra+')
	fh = f.read()
	loop = loop - 1

loop = fh.count('/')
pox1 = 0
while loop != 0:
	f.seek(pox1)
	if pox1 != 0:
		f.write('|')
	f.close()
	f = open('opa', 'ra+')
	fh = f.read()
	pox2 = fh.index('/')
	sig = fh[pox1:pox2]
	output.write(sig)
	output.write('\n')
	if pox1 == 0:
		pox1 = fh.index('/')
	else:
		pox1 = pox2
	loop = loop - 1
f.close()
output.close()

f = open('opa', 'w')
backup = open('original', 'r')
backup_content = backup.read()
f.write(str(backup_content))
backup.close()
f.close()

del f, fh, output, pox1, pox2, loop, sig, backup

f = open('output', 'r+')
saida = open('saida', 'w')
saida.close()
saida = open('saida', 'ra+')
fh = f.readlines()
num = len(fh) - 1
while num != 0:
	line = fh[num]
	end = line.index('\n')
	ini = line.index('|')
	saida.write(line[ini+2:end])
	saida.write('\n')
	num = num -1
saida.close()
saida = open('saida', 'ra+')
saida_handle = saida.read()
num = saida_handle.count(';')
while num != 0:
	pox = saida_handle.index(';')
	saida.seek(pox)
	saida.write(' ')
	saida.close()
	saida = open('saida', 'ra+')
	saida_handle = saida.read()
	num = num - 1
saida.close()

remove('original')
remove('output')