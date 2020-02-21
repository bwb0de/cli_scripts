#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os, shutil, sys, glob, time

dectmp = '/tmp/frqtmp'
decout = '/home/bwbode/Área de trabalho'
decdat = '/tmp/frqdat'
model = "/home/bwbode/NMP/2012/Modelos/memoFRQ.odt"
datatable = "/home/bwbode/NMP/2012/DADOS_EDU_INTEGRAL-DREP_2012.ods"

initidir = os.getcwd()

mes = sys.argv[1]
ddmmaa = ('%s de %s de %s' % (time.localtime()[2],mes,time.localtime()[0]))

tagdata = ddmmaa
tagmsg1 = ""
tagmsg2 = ""

try:
	os.mkdir(dectmp)
	os.mkdir(decout)
	os.mkdir(decdat)
except:
	pass

shutil.copy(datatable, dectmp+os.sep+'dat.ods')
os.chdir(dectmp)

#Gerar arquivo lista
os.system("unzip dat.ods > /dev/null")
os.remove('dat.ods')
f = open("content.xml",'r')
ddd = f.read().replace("¬",os.linesep+"¬").replace("»",os.linesep+"»").replace('"><text:p>',"¢"+os.linesep) #.replace('/>',os.linesep).replace('<',os.linesep)
f.close()

f = open("gerallista",'w')
f.write(ddd)
f.close()

os.system("cat < gerallista | grep '¬' | grep 'æ¢' > listafr")
os.system("cat < gerallista | grep '»' | grep 'æ¢' > listaq")

#Limpar listas

f = open("listafr",'r')
lstfr = f.read().replace("¬","").replace("æ¢","").replace("&apos;", "'").replace(", ", ",")
f.close()
f = open("listafr",'w')
f.write(lstfr)
f.close()

f = open("listaq",'r')
lstq = f.read().replace("»","").replace("æ¢","").replace("&apos;", "'")
f.close()
f = open("listaq",'w')
f.write(lstq)
f.close()

#Construindo texto do memorando

f = open("listafr",'r')
lstfr = f.readlines()
iez = ''
bol = ''

for i in lstfr:
	iez = iez + i.split('|')[0] + ', '
	boltmp = i.split('|')[1].split(',')
	for ii in boltmp:
		bol = bol + ii.replace(os.linesep, "") + ", "

bol = bol[0:len(bol)-2]

if len(iez) < 1:
	tagmsg1 = ""

tagmsg1 = """Seguem, em anexo, as folhas de frequência e relatórios de desempenho para o mês de %s da(s) instituição(ões) educacional(is) %s referente ao(s) bolsista(s): %s.""" % (mes, iez, bol)

f = open("listaq",'r')
lstq = f.readlines()
iez = ''

for i in lstq:
	iez = iez + i.replace(os.linesep, "") + ', '
	
iez = iez[0:len(iez)-2]

tagmsg2 = """Seguem, também, o(s) quadro(s) de frequência para o mês de %s da(s) instituição(ões) educacional(is) %s.""" % (mes, iez)

if len(iez) < 1:
	tagmsg2 = ""

os.chdir(dectmp)
os.system("rm -R *")

#Montando memorando.

shutil.copy(model, dectmp+os.sep+'sk.odt')
os.system("unzip sk.odt > /dev/null")
os.remove('sk.odt')
f = open('content.xml','r')
content = f.read()
f.close()
content = content.replace('TAGDATA',tagdata).replace('TAGMSG1',tagmsg1).replace('TAGMSG2',tagmsg2)
f = open('content.xml','w')
f.write(content)
f.close()
memoname = str(time.localtime()[0])+"-"+str(time.localtime()[1]).zfill(2)+"-"+str(time.localtime()[2]).zfill(2)+"_[0000]_"+"frq2CEINT"
os.system('zip -r -0 "%s" * > /dev/null' % str(memoname+".zip"))
shutil.copy(str(memoname+".zip"), decout+os.sep+str(memoname+".odt"))
os.system("""libreoffice '%s'""" % decout+os.sep+str(memoname+".odt"))
os.chdir(dectmp)
os.system("rm -R *")
exit()
