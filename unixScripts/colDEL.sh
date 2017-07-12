#!/bin/bash

#The purpose of this code is to delete columns in catalogs with empty values in
#in them, some rows might have values in these "extra" columns but this code
#blanket removes the whole column 
#    HOW TO USE: this code is an example of what to type into the command line
#You have to put the filename of the catalog and specify which columns you want
#to keep

awk '{print $1,$2,$3,$4,$7}' pantest.txt > pantesty.txt

#This line removes the 6th column
