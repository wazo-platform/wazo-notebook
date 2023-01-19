#!/bin/bash

while read file ; do
    cat update.txt | while read name old new ; do
        sed -i -e "s/^$name==$old/$name==$new/g" $file
    done
done
