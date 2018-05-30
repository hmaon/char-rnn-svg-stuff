#!/bin/bash

rm input.txt
rm *.t7

for i in *.svg
do
echo $i
svgo -i $i -o - >> input.txt
done

