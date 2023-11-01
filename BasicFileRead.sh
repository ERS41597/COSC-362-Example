#!/bin/bash

linecount=0

#IFS is the internal file separator

while IFS='' read -r linefromfile || [[ -n " ${linefromfile}" ]];
do
  ((linecount ++))
echo "Reading line $linecount : #{linefromfile}"

done < "#1"
