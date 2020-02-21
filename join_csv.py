from csv import DictReader
from csv import writer as w2csv
from csv import reader, QUOTE_NONE
from os import listdir, curdir, walk, mkdir, path, getcwd, chdir, remove, removedirs, kill
from os import linesep as nl

def test():
	join_csv('ppase.csv','sae.csv','matricula','out.csv')

def read_csv(csvfile):
	'''Acessa o conteúdo do arquivo CSV e o armazena na memória.'''
	o = []
	with open(path.join(getcwd(), csvfile)) as csvfileobj:
		rd = DictReader(csvfileobj)
		for row in rd:
			o.append(row)
	return o

def write_csv(d, outcsvfile, header=None):
	''' DESC '''
	if header == None:
		print(str(d))
		fields = []
		for k in d[0].keys():
			print(k)
			fields.append(k)
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
				print(row[col])
				data.append(row[col])
		print(data)
		content.append(data)
	with open(path.join(getcwd(), outcsvfile), 'wb') as csvfile:
		spamwriter = w2csv(csvfile, dialect='excel')
		spamwriter.writerow(fields)
		for l in content:
			spamwriter.writerow(l)

def join_csv(csvfile1, csvfile2, col, output_file):
	'''Realiza a junção de dois dicionários distintos que compartilhem uma mesma chave/col. Retorna as linhas em que os valores da chave selecionada correspondem nos dois dicionários.'''
	output = []
	tmpdict = {}
	csvdata1 = read_csv(csvfile1)
	csvdata2 = read_csv(csvfile2)
	for row in csvdata1:
		tmpdict[row[col]] = row
	csvdata2_cols = csvdata2[0].keys()
	for other_row in csvdata2:
		if other_row[col] in tmpdict:
			joined_row = tmpdict[other_row[col]]
			for colz in csvdata2_cols:
				if colz != col:
					joined_row[colz] = other_row[colz]
			output.append(joined_row)
	write_csv(output, output_file)
	return output
