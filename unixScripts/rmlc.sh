#!/bin/bash
# this is not my code got it from 
#http://stackoverflow.com/questions/935251/linux-delete-files-that-dont-contain-specific-number-of-lines
# this deletes files that have less or more than a certain number of lines
# it shows you what to type into cmd line don't run this
find -name '*.txt' | xargs  wc -l | awk '{if($1 > 1000 && index($2, "txt")>0 ) print $2}' | xargs rm

# in the example above files greater than 1000 lines are delted choose > 
# and < and number of lines accordingly 
