#!/bin/bash

dir_path="./md"
dirs=`find $dir_path -type f`

for file in $dirs;
do
    echo $file
    basename $file .md | python3 convert.py
done
