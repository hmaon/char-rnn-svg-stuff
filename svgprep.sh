#!/bin/bash

rm input.txt
rm preinput.txt
rm *.t7

for i in *.svg
do
echo $i
svgo -i "$i" -o - >> preinput.txt
done

../../xmlstupify.py < preinput.txt > input.txt 
rm preinput.txt
