#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def indexseek(x,str):
	result = []
	strOB = str.replace('a','#').replace('e','#').replace('i','#').replace('o','#').replace('u','#')
	print strOB
	while True:
		if strOB.find(x) == -1:
			result.append(strOB)
			return result
		pos = strOB.index(x)
		strOB1 = strOB[:pos]
		strOB2 = strOB[pos+len(x):]
		strOB = strOB1+('*'*len(x))+strOB2
		result.append(pos)

def char_class(x):
	if (x == 'a') or (x == 'e') or (x == 'i') or (x == 'o') or (x == 'u'):
		return 'Vogal'
	else:
		if x == ' ':
			return 'White space'
		else:
			return 'Consoante'
		
def char_seek(str):
	n = len(str)
	c = 0
	swich = 'off'
	resp = ''
	while c != n-1:
		r = char_class(str[c])
		if r == 'Consoante' and swich == 'off':
			pass
		elif r == 'Consoante' and swich == 'on':
			if ((str[c] == 's') or (str[c] == 'n') or (str[c] == 'm')):
				if char_class(str[c+1]) == 'Consoante':
					swich = 'off'
					print ' ------------ silabend'
			else:
				swich = 'off'
				print ' ------------ silabend'
		elif r == 'White space':
			swich = 'on'
			print ' ------------ silabend'
		elif r == 'Vogal':
			swich = 'on'
		else:
			pass
		print str[c]
		c = c + 1

def birseek(x,y):
	str = y
	l = indexseek(x,str)
	r = []
	for i in l:
		try:
			if i == 0:
				print str[i]
			elif i == len(str)-1:
				print str[i-1] + str[i]
			else:
				if char_class(str[i+1]) == 'V':
					if char_class(str[i+2]) == 'V':
						if str[i-1] == ' ':
							print str[i] + str[i+1] + str[i+2]
							l.remove(l[l.index(i)+1])
							l.remove(l[l.index(i)+2])
						'''elif char_class(str[i-1]) == 'C':
							if (str[i-1] == 'r') or (str[i-1] == 'R'):
								if char_class(str[i-2]) == 'C':
									print str[i-2] + str[i-1] + str[i] + str[i+1] + str[i+2]'''
						
						else:
							print str[i-2] + str[i-1] + str[i] + str[i+1] + str[i+2]
							l.remove(l[l.index(i)+1])
							l.remove(l[l.index(i)+2])
					else:
						'''if char_class(str[i-1]) == 'C':
							if (str[i-1] == 'r') or (str[i-1] == 'R'):
								if char_class(str[i-2]) == 'C':'''
									'''print str[i-2] + str[i-1] + str[i] + str[i+1]'''
								else:
									print str[i-1] + str[i] + str[i+1]
									
				else:
					if char_class(str[i-1]) == 'C':
						if (str[i-1] == 'r') or (str[i-1] == 'R'):
							if char_class(str[i-2]) == 'C':
								print str[i-2] + str[i-1] + str[i]
							else:
								print str[i-1] + str[i]
		except:
			pass 
