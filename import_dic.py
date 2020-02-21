#!/usr/bin/env python
#
# Python script to import dictionary data from plain txt files...
# It may be a function...
#

mail = addr = name = nick = dict()

def import_dic(x):
      """Import dictionary data from plain text file"""

      file = x
      f = open(file, 'ra+')
      fh = f.read()
      loop = first = fh.count(':')

      #Preparing text file to drag off data
      while loop != 0:
            if loop == first:
                  dicSTARTchar = fh.index('{')
                  dicENDchar = fh.index('}')
                  dicKEYchar = fh.index(':')
                  f.seek(dicSTARTchar)
                  f.write('[')
                  f.seek(dicKEYchar)
                  f.write(']')
                  f.seek(dicENDchar)
                  f.write(';')
                  f.close()
                  f = open(file, 'ra+')
                  fh = f.read()
                  loop = loop -1
            else:
                  dicKEYchar = fh.index(':')
                  dicVALUEchar = fh.index(',')
                  f.seek(dicKEYchar)
                  f.write(']')
                  f.seek(dicVALUEchar)
                  f.write(';[')
                  f.close()
                  f = open(file, 'ra+')
                  fh = f.read()
                  loop = loop -1

      #Redefining looping var...
      f = open(file, 'ra+')
      fh = f.read()
      loop = first

      #Copying data from text file...
      while loop != 0:
            if loop == first:
                  initKEY = fh.index('[')
                  endKEY = fh.index(']')
                  endVALUE = fh.index(';')
                  key = fh[initKEY+2:endKEY-1]
                  value = fh[endKEY+3:endVALUE-1]
                  f.seek(initKEY)
                  f.write('{')
                  f.seek(endKEY)
                  f.write(':')
                  f.seek(endVALUE)
                  f.write(',')
                  f.close()
                  f = open(file, 'ra+')
                  fh = f.read()
                  print key, value
                  mail[key] = value
		  loop = loop - 1
            elif loop == 1:
                  initKEY = fh.index('[')
                  endKEY = fh.index(']')
                  endVALUE = fh.index(';')
                  key = fh[initKEY+2:endKEY-1]
                  value = fh[endKEY+3:endVALUE-1]
                  f.seek(initKEY)
                  f.write(' ')
                  f.seek(endKEY)
                  f.write(':')
                  f.seek(endVALUE)
                  f.write('}')
                  f.close()
                  f = open(file, 'ra+')
                  fh = f.read()
                  print key, value
                  mail[key] = value
		  loop = loop - 1
            else:
                  initKEY = fh.index('[')
                  endKEY = fh.index(']')
                  endVALUE = fh.index(';')
                  key = fh[initKEY+2:endKEY-1]
                  value = fh[endKEY+3:endVALUE-1]
                  f.seek(initKEY)
                  f.write(' ')
                  f.seek(endKEY)
                  f.write(':')
                  f.seek(endVALUE)
                  f.write(',')
                  f.close()
                  f = open(file, 'ra+')
                  fh = f.read()
                  print key, value
                  mail[key] = value
                  loop = loop - 1
      f.close()

import_dic('newlista')