#!/bin/bash

MSG=$1

git add --all

if [ "$#" = "0" ]; then
	git commit
elif [ "$#" = "1" ]; then
	git commit -m "$MSG"
fi

git push
