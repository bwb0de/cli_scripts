def check_item_list(i,l):
	try:
		l.index(i)
		return True
	except:
		return False

def acess_control(view_function):
	#@login_required
	def wrapper(*args, **kargs):
		print('Test if page is allowed for user')
		allowed = ['daniella', 'julia', 'mara']
		if check_item_list(kargs['user'], allowed) == True:
			print('Ok!')
			view_function(*args, **kargs)
		else:
			print('Not ok!!!')
			print('FORBIDDEN!!!')
	return wrapper


@acess_control
def add_new_form(user=None):
	print('Conteúdo restrito apresentado')

