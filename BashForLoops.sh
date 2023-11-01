#!/bin/bash

# C++ Style for loops:
for (( i=0; i<$1 ; i++ ))
do
  echo "C++ style for loop: " $i 
done

# For in list style:
for i in {1..12}
do 
  echo "Bash isn't python for ith time: " $i
done

#Looping a List
for thing in  "One" "Two" "Three" "Four" "Five"
do
  echo "Spit back a number:" $thing
done

# Getting things from the arguement list:
echo "The second thing after the script name is: " $2
echo "We are running the script: " $0


StringStuff =" I like cheese, cheese is good!"
for i in $StringStuff
do
 echo "The contents of String stuff are: " $i
done

