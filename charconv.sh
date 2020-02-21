#/bin/bash
#
# Script para converter caracteres de texto e gerar saida de Feed e jddnews
#
# '�' '<'
# '�' '>'
# '�' '/'
# '�' '&ccedil;'

for files in *.txt
	do
	#tem que adicionar o arquivo de modelo, por construir a p�gina.
	cat < [modelo] | head -n +[n] | tail -n +[n] > "/var/www/$files.html" #sa�da da p�gina criada
        cat < $files | head -n +1 | tail -n +1 >> "/var/www/$files.html" #adicionando apenas o t�tulo da p�gina
	cat < [modelo] | head -n +[n] | tail -n +[n] > "/var/www/$files.html" #adicionar prepara��o pro texto.
	cat < $files | head -n +2 >> "/var/www/$files.html" #adicionando o restante do texto...
	if [ -f "$files.jpg" ]
		then
		cat < [modelo] | head -n +[n] | tail -n +[n] > "/var/www/$files.html" #adicionar img (se tiver)
		cat < $files | head -n +2 >> "/var/www/$files.html" #adicionando o restante do texto...
	fi
	#modificando o arquivo XML do feed
	event_numb=`cat < [xmlFEED] | grep '<item>' | wc -w` #verifica o n�mero de not�cias postadas
		#apaga a �ltima not�cia
		#muda o arquivo TXT pro formato RSS [cabe�alho e tags]
		#cria um novo arquivo RSS aproveitando as 9 not�cias mais recentes do antigo
	
	#copia todos os arquivos relevantes para a pasta de upload
		#copia o RSS gerado
		#copia a imagem utilizada
		#copia a p�gina gerada
		
	


