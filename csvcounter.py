# -*- coding: utf-8 -*-
"""
@author: bwb0de
@email: dftdcruz@gmail.com
"""

from os import path, getcwd
from csv import DictReader
from csv import writer as w2csv
from csv import reader, QUOTE_NONE
from sys import argv

try: csvfile = argv[1]
except:
	print u'Nome do arquivo csv não fornecido ou arquivo csv não encontrado.'
	exit()

try:
	if argv[2] == '-c':
		if argv[3].find('|') != -1:
			cross_analisis_fields_list = argv[3].split('|')
		else:
			cross_analisis_fields_list = argv[3].split(',')
			print cross_analisis_fields_list
except: cross_analisis_fields_list = False

def check_item_list(item, lista):
	try:
		lista.index(item)
		return True
	except:
		return False

def read_csv(csvfile):
	'''Acessa o conteúdo do arquivo CSV e o armazena na memória.'''
	o = []
	with open(path.join(getcwd(), csvfile)) as csvfileobj:
		rd = DictReader(csvfileobj)
		for row in rd:
			o.append(row)
	return o

def read_csv_col(col, csvfile):
	fd = read_csv(csvfile)
	o = []
	for i in fd:
		o.append(i[col])
	o.sort()
	return o

def count_values_in_csv_col(col, csvfile):
	'''Retorna os diferentes valores existentes na coluna 'col' para a 'tabela' do mysql selecionada junto com suas respectivas quantidades.'''
	r = read_csv_col(col, csvfile)
	tmp_lst = []
	for i in r:
		tmp_lst.append(i)
	tmp_lst.sort()
	tmp_lst_entries = set(tmp_lst)
	output = {}
	for i in tmp_lst_entries:
		output[i] = [tmp_lst.count(i)]
	return output

def count_relative_values_in_csv_col(col, csvfile):
	f = open(path.join(getcwd(), csvfile), 'r')
	n = int(len(f.readlines())-1)
	r = count_values_in_csv_col(col, csvfile)
	for i in r.keys():
		r[i] = [r[i][0], (float(r[i][0])/n)*100]
	return r

def get_csv_cols(csvfile):
	'''Retorna os nomes das colunas do arquivo CSV alvo... Depende do módulo 'csv'.'''
	with open(path.join(getcwd(), csvfile)) as csvfileobj:
		reader = DictReader(csvfileobj)
		cols = reader.fieldnames
	return cols

def write_csv(d, outcsvfile, header=None):
	''' DESC '''
	if header == None:
		print str(d)
		fields = d[0].keys()
		fields.sort()
	else:
		fields = header
	content = []
  	for row in d:
  		data = []
  		for col in fields:
  			try:
  				data.append(row[col].encode('utf-8'))
  			except:
  				data.append(row[col])
  		content.append(data)
	with open(path.join(getcwd(), outcsvfile), 'wb') as csvfile:
		spamwriter = w2csv(csvfile, dialect='excel')
		spamwriter.writerow(fields)
		for l in content:
			spamwriter.writerow(l)

def make_complete_stat_from_csv(csvfile):
	output = {}
	csv_cols = get_csv_cols(csvfile)
	for c in csv_cols:
		output[c] = count_relative_values_in_csv_col(c, csvfile)

	if cross_analisis_fields_list != False:
		csv_content = read_csv(csvfile)
		tmp_csv_cross_values = []
		tmp_csv_line = {}
		tmp_csv_line_fa_total = {}
		cross_key_list = []
		cross_analisis_list = []
		if argv[3].find('|') != -1:
			for list_of_cols in cross_analisis_fields_list:
				mk_tmp_cross_key = list_of_cols.split(',')
				mk_tmp_cross_key.append(mk_tmp_cross_key[len(mk_tmp_cross_key)-1])
				cross_analisis_list.append(mk_tmp_cross_key)
		else:
			mk_tmp_cross_key = cross_analisis_fields_list
			mk_tmp_cross_key.append(mk_tmp_cross_key[len(mk_tmp_cross_key)-1])
			cross_analisis_list.append(mk_tmp_cross_key)
		
		for list_of_cols in cross_analisis_list:
			list_of_cols.sort()
			list_len = len(list_of_cols)-1
			list_of_cols.pop(list_len)
			list_of_cols_label = ' e '.join(list_of_cols)
			if check_item_list(list_of_cols_label, cross_key_list) == False:
				cross_key = list_of_cols
				tmp_csv_line[list_of_cols_label] = {}
				colanalisis = []
				for lines in csv_content:
					if list_len < 2:
						print u'É necessário haver mais de duas colunas para o processamento cruzado.'
						return None
					elif list_len >= 11:
						print u'Processamento máximo suportado é de 10 colunas.'
						return None
					else:
						if list_len == 2:
							line_cross_value = ' e '.join([lines[cross_key[0]],lines[cross_key[1]]])
						elif list_len == 3:
							line_cross_value = ' e '.join([lines[cross_key[0]],lines[cross_key[1]],lines[cross_key[2]]])
						elif list_len == 4:
							line_cross_value = ' e '.join([lines[cross_key[0]],lines[cross_key[1]],lines[cross_key[2]],lines[cross_key[3]]])
						elif list_len == 5:
							line_cross_value = ' e '.join([lines[cross_key[0]],lines[cross_key[1]],lines[cross_key[2]],lines[cross_key[3]],lines[cross_key[4]]])
						elif list_len == 6:
							line_cross_value = ' e '.join([lines[cross_key[0]],lines[cross_key[1]],lines[cross_key[2]],lines[cross_key[3]],lines[cross_key[4]],lines[cross_key[5]]])
						elif list_len == 7:
							line_cross_value = ' e '.join([lines[cross_key[0]],lines[cross_key[1]],lines[cross_key[2]],lines[cross_key[3]],lines[cross_key[4]],lines[cross_key[5]],lines[cross_key[6]]])
						elif list_len == 8:
							line_cross_value = ' e '.join([lines[cross_key[0]],lines[cross_key[1]],lines[cross_key[2]],lines[cross_key[3]],lines[cross_key[4]],lines[cross_key[5]],lines[cross_key[6]],lines[cross_key[7]]])
						elif list_len == 9:
							line_cross_value = ' e '.join([lines[cross_key[0]],lines[cross_key[1]],lines[cross_key[2]],lines[cross_key[3]],lines[cross_key[4]],lines[cross_key[5]],lines[cross_key[6]],lines[cross_key[7]],lines[cross_key[8]]])
						elif list_len == 10:
							line_cross_value = ' e '.join([lines[cross_key[0]],lines[cross_key[1]],lines[cross_key[2]],lines[cross_key[3]],lines[cross_key[4]],lines[cross_key[5]],lines[cross_key[6]],lines[cross_key[7]],lines[cross_key[8]],lines[cross_key[9]]])
					colanalisis.append(line_cross_value)
				cros_col_total = 0
				for unic_line in set(colanalisis):
					tmp_csv_line[list_of_cols_label][unic_line] = [colanalisis.count(unic_line)]
					cros_col_total += colanalisis.count(unic_line)
				tmp_csv_line_fa_total[list_of_cols_label] = cros_col_total

		for c in sorted(tmp_csv_line.keys()):
			for v in tmp_csv_line[c].keys():
				tmp_csv_line[c][v].append((float(tmp_csv_line[c][v][0])/tmp_csv_line_fa_total[c])*100)
	else:
		tmp_csv_line = None
	return [output,tmp_csv_line]


def map_values_in_csv_col(col, csvfile):
	'''Retorna os diferentes valores existentes na coluna 'col' para a 'tabela' do mysql selecionada.'''
	output = count_values_in_csv_col(col, csvfile)
	output = output.keys()
	return output
	
def show_dict_data(d, ofname):
	'''Apenas retorna as chaves e os valores de um dicionário no formato de lista, obedecendo o layout "KEY » VALUE". '''
	o = u''
	for i in sorted(d.keys()):
		o = o + u"Coluna/Variável: "+i.decode('utf-8')+u'\n'
		for ii in sorted(d[i].keys()):
			o = o + u"  --> %s:" % ii.decode('utf-8') + unicode(d[i][ii]) +'\n'
		o = o + '\n'
	f = open(ofname,'w')
	f.write(o.encode('utf-8'))
	f.close()

o = make_complete_stat_from_csv(csvfile)
show_dict_data(o[0], 'simple_tab')
show_dict_data(o[1], 'cross_tab')
