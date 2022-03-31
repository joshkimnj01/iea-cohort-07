read -p "Enter file name: " filename

if ls $filename; then  # note spaces around [ ]
   echo "found file $filename"
else
    echo "==no file found=="
fi