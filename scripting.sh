#!/bin/bash
echo "Enter the path:"
read path
if [ -f "$path" ]; then
    echo "It is a file."
elif [ -d "$path" ]; then
    echo "Itis a directory."
else
    echo "The path does not exist."
fi