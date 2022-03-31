#!/bin/bash
for file in "$@"; do
         if test -s $file; then
	     echo FOUND a file $file  -inspected by JK
	 elif test -e $file ; then 
             echo DELETING as this Zero file $file
	     rm -f $file
         else 	
	     echo No files FOUND for $file

	 fi
done
