#!/bin/bash


# for var in "$@"
# 	do 
# 		[ ! -d ~/.mytrash/ ] && mkdir ~/.mytrash/
# 		mv "$var" ~/.mytrash/
#         echo "Trashing files"

# done



function funcEmpty()
{
	read -p "Are you sure you want to empty the trash?[Y/N]" answer

	case $answer in 
	[yY])

		rm -r .mytrash/*
		echo "Trash is already empty"
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
            [ ! -d ~/.mytrash/ ] && mkdir ~/.mytrash/
            mv "$var" ~/.mytrash/
    echo "Trashing files"
done
;;

esac
 exit 0

