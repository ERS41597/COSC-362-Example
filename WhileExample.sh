#!/bin/bash
# A basic while loop for counting in bash
clear
counter=1
while [ $counter -le 19 ]
do 
echo $counter
sleep 1
clear
((counter++))
done
echo "Wasn't that special!"
