#!/bin/bash
#This is testing taking all the files in a directory and for loop outputting
#under a different name and changing the commas in the file to spaces

LIST="$(ls ~/Projects/Work/testFiles/*.txt)"

for i in "$LIST"; do
#	echo "$i"
	sed -e "s/banana/5/g" $i;   
done
