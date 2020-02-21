#!/bin/bash
#
# Slide wallpapaer for fluxbox...
#

cd /users/Dani/.fluxbox/backgrounds
look=1
while [ "$look" = "1" ] ; do
	for i in * ; do
	fbsetbg -f $i
	sleep 90
	done
done