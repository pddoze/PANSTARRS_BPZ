#!/bin/bash
#New version of Script2 originally Script3 to test using sed to  find to replace parts of a file
#and change the ending extension on file name and also change the output location
# ${FILENAME%.txt}bat.txt the % gets rid of .txt and bat.txt is added onto the result
#Doing find '*.txt' with the path in front of it doesnt just read in the
#file name it reads in the whole path
#The | takes the output of the find as the input for the while loop

#HOW TO USE THIS
#You need to specify where the files are coming from (find line) and where they are going to
# which is the (sed line) Then change the sed to replace what you want in the file

find ~/Projects/panstarCSV/ -name '*.csv' |  while read FILENAME; do #FILENAME still has path
#	echo "$FILENAME"
	NEWFILENAME=$(basename $FILENAME)  #takes path out, only file name left
#	echo "$NEWFILENAME"
	sed -e "s/,/ /g" <$FILENAME >~/Projects/panstarSSV/${NEWFILENAME%.csv}SSV.txt 
done 
