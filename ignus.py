def get_obs_from(x,y):
	r=[]
	for i in y:
	  if i.find(r'%s' % x) != -1:
	   if i[0] == ' ':
		s = i[1:]+'.'
		r.append(s)
	   else:
		s = i+'.'
		r.append(s)
	return r



