#!/bin/bash
#
# Apagador de lista... Confronta duas listas e apaga os items da segunda que estão na primeira...





lines=`wc -l txt | awk -F" " '{ print $1 }'`

while test "$lines" != "0"
	do
	str=`cat < txt | head -n +$lines | tail -n +$lines`
	echo $str
	cat < $1 | sed "s/$str//g" > tmp-$1
	cat < tmp-$1 > $1
	lines=`expr $lines - 1`
	rm -f tmp-$1
	done;