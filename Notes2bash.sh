#!/bin/bash
#Simple Menued interface
names = ' Alice Bob Carol Quit '
PS3 = 'Select a Character'
select name in $names
do 
if [#name =='Quit']
then
break
fi
echo Hello $name
done
echo "Bye"
