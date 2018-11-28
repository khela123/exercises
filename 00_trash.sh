#!/bin/bash

function funcEmpty()
{
	read -p "Are you sure you want to empty the trash?[Y/N]" answer

	case $answer in 
	[yY])

		rm -r .mytrash/*
		echo "Emptying Trash"
		echo "Trash is empty"
		;;

	[nN]) exit;;

	esac
}

case $1 in -e)

    funcEmpty
    # empty the trash
;;  
 *) 

for var in $@; 
    do
            mkdir -p ~/.mytrash/
            mv "$var" ~/.mytrash/
done
	echo "Trashing files"
;;

esac
exit 0

