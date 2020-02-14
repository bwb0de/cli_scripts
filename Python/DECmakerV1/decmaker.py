#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os, shutil, sys, glob, time

dectmp = '/tmp/dectmp'
decout = '/tmp/decout'
model = "/home/bwb0de/Área de Trabalho/skell1.odt"
initidir = os.getcwd()

#REVER
if time.localtime()[1] == 0:
	mes = 'janeiro'
elif time.localtime()[1] == 1:
	mes = 'fevereiro'
elif time.localtime()[1] == 2:
	mes = 'março'
elif time.localtime()[1] == 3:
	mes = 'março'
elif time.localtime()[1] == 4:
	mes = 'maio'
elif time.localtime()[1] == 5:
	mes = 'junho'
elif time.localtime()[1] == 6:
	mes = 'julho'
elif time.localtime()[1] == 7:
	mes = 'agosto'
elif time.localtime()[1] == 8:
	mes = 'setembro'
elif time.localtime()[1] == 9:
	mes = 'outubro'
elif time.localtime()[1] == 10:
	mes = 'novembro'
elif time.localtime()[1] == 11:
	mes = 'dezembro'

ddmmaa = ('%s de %s de %s' % (time.localtime()[2],mes,time.localtime()[0]))

os.mkdir(dectmp)
os.mkdir(decout)

lista = sys.argv[1]

f = open(lista,'r')
lines = f.readlines()
f.close()

for i in lines:
	col = i.split(',')
	os.chdir(dectmp)
	shutil.copy(model, dectmp+os.sep+'sk.odt')
	os.system("unzip sk.odt")
	os.remove('sk.odt')
	f = open('content.xml','r')
	content = f.read()
	f.close()
	
	if col[3].replace(os.linesep,'') == '12':
		var1 = 'integralmente'
	else:
		var1 = 'parcialmente'
	
	if (col[1] != '0') and (col[2] == '0'):
		periodo = 'com frequência integral no período matutino'
	elif (col[1] == '0') and (col[2] != '0'):
		periodo = 'com frequência integral no período vespertino'
	else:
		periodo = 'com frequência de %sh no período matutino e %sh no período vespertino' % (col[1],col[2])
		
		
	content = content.replace('[§NOME§]',col[0]).replace('[§STATUS§]',var1).replace('[§PERIODO§]',periodo).replace('[§TEMPO§]',col[3].replace(os.linesep,'')).replace('[§DATA§]',ddmmaa)
	
	f = open('content.xml','w')
	f.write(content)
	f.close()
	
	os.system('zip -r -0 "%s" *' % str(col[0]+".zip"))
	shutil.copy(str(col[0]+".zip"), decout+os.sep+str(col[0]+".odt"))
	
	shutil.rmtree(dectmp)
	os.mkdir(dectmp)

os.chdir(decout)
files = glob.glob('*.*')
try:
	os.mkdir(initidir+os.sep+'Decz')
except:
	pass

for i in files:
	shutil.move(i, initidir+os.sep+'Decz'+os.sep+i)

try:
	shutil.rmtree(dectmp)
except:
	pass
	
try:
	shutil.rmtree(decout)
except:
	pass

print ''
print "Feito!"

