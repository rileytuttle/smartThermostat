#!/bin/bash
if [ $# == 2 ] ; then 
	rm -f schedule.txt;
	let endIndex=1440/$2-1;
	for i in `seq 0 $endIndex`; do
		echo "$1" >> schedule.txt
	done
elif [ $# == 3 ] ; then
	let startIndex=$1;
	let endIndex=$2;
	for i in `seq $startIndex $endIndex`; do
		sed -i "${i}s/.*/$3/" schedule.txt
	done
else
	echo "invalid arguments"
fi
