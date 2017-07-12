#!/bin/bash


tail -n +2 SDSSssv18Col.txt | split -l 200000 - split_
for file in split_*
do
    head -n 2 SDSSssv18Col.txt > tmp_file
    cat $file >> tmp_file
    mv -f tmp_file $file
done
