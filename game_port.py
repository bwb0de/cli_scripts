#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def string_try(x,y):
  strtotry = get_let(x)
  strbase = get_let(y)
  for i in strtotry:
   try:
    strbase.pop(strbase.index(i))
   except:
    return 'Error!'
  return 'Ok!'

def get_let(x):
  n = len(x)-1
  l = []
  while n != -1:
   l.append(x[n])
   n = n - 1
  return l
