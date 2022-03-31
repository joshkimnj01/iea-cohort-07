#!/bin/bash
echo 'Enter the file name to find'
filename=
   while [[ $filename = '' ]]; do
      read filename
      if [ $filename = "" ]; then
         echo 'No entry made, please try again'
      fi
   done

if test -e $filename ; then  # note spaces around [ ]
    echo # found the file $filename
else
    echo +++ no file found +++
fi
echo
