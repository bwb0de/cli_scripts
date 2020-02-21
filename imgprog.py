#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys, os, pygtk, gtk, gtk.glade, string
pygtk.require('2.0')

imglist = os.listdir(os.curdir)
imgfiles = []
for i in imglist:
	if i.find('.jpg')
		imgfiles.append(i)

lastitem = len(imgfiles)-1
pos=0

class imgprog:
	def __init__(self):
		self.gladefile = "imgprog.glade"
		self.xml = gtk.glade.XML(self.gladefile)
		
		self.image1 = self.xml.get_widget('image1')
		self.label1 = self.xml.get_widget('label1')
		self.button1 = self.xml.get_widget('button1')
		
		#Conecta os sinais do ambiente gráfico ao script						
		self.xml.signal_autoconnect(self)
		
		#Configura o botão fechar para sair do processo, extinguindo PID...
		if (self.window1):
			self.window1.connect("destroy", gtk.main_quit)
			
		self.image1.set_from_file(imgitem[0])
		
		#Exibe toda interface
		self.window1.show_all()
		
		#Inicia o loop principal de eventos (GTK MainLoop)
		gtk.main()
		
	def sair(self, widget):
		gtk.main_quit()
		
	def next_img(self, widget):
		pos+=1
		if pos > lastitem:
			pos=0
		self.image1.set_from_file(imgitem[pos])
		
	
	def prev_img(self, widget):
		pos-=1
		if pos < 0:
			pos=0
		self.image1.set_from_file(imgitem[pos])

if __name__ == "__main__":
	imgprog()
