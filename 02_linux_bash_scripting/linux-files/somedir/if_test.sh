#!/bin/bash

echo 'Enter the file name to find'
filename=
   while [[ $filename = '' ]]; do
      read filename
      echo 'No entry was made try again'
   done
      if  test -e $filename; then
        echo   # found the file $filename
      else    # note spaces around [ ]    
        echo ==no file found==
      fi

echo
#ls -l $filename

