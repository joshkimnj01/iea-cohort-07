#!/bin/bash
set -e

if [ $# = 0 ]; then
    echo "Script was run with no arguments, Try again."
    exit 1
fi
#echo $1
filename=$1
if [ ! -e $filename ]; then
    echo "File does not exit"
    exit 1
fi

#if [ -e $filename ]; then
#    echo "File does exit">/dev/null
#else
#    echo "File does not exit"
#    exit 1
#fi