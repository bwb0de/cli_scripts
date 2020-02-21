#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def indexseek(x,str):
	result = []
	#strOB = str
	strOB = str.replace('a','#').replace('e','#').replace('i','#').replace('o','#').replace('u','#')
	print strOB
	while True:
		if strOB.find(x) == -1:
			result.append(strOB)
			return result
		pos = strOB.index(x)
		#t = (pos, p[pos:pos+len(x)])
		strOB1 = strOB[:pos]
		strOB2 = strOB[pos+len(x):]
		strOB = strOB1+('*'*len(x))+strOB2
		result.append(pos)
		
def birseek(x,str):
	l = indexseek(x,str)
	r = []
	for i in l:
		try:
			if i == 0:
				print str[i]
			elif i == len(str)-1:
				#try:
				#	if l[len(l)-1][i+1] == '#':
				#		print str[i-1] + str[i] + str[i+1]
				#	else:
				print str[i-1] + str[i]
			else:
				if l[len(l)-1][i+1] == '#':
					print str[i-1] + str[i] + str[i+1]
					l.remove(l[l.index(i)+1])
				else:
					print str[i-1] + str[i]
				#except:
				#	try:
				#		print str[i-1] + str[i]
				#	except:
				#		print str[i]
		except:
			
			print '\n' + 'Done!'
