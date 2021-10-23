#!/usr/local/bin/bash
# Author: Bhaskar Varadaraju
#
# A Shell program to check and print cli arguments passed
# Usage: bash 06_cli_args.sh ab cd ef gh
# Try  : 
#	bash 06_cli_args,sh
# 	bash 06_cli_args.sh ab
# 	bash 06_cli_args.sh ab cd
# 	bash 06_cli_args.sh ab cd ef gh
# 
if [ $# -ge 2 ]
then
	echo “INFO: Received required arguments”
else
	echo “ERROR: Atleast 2 arguments must be passed at cli”
	exit 1
fi
echo “'This scripts name is         :' $0”
echo “'The first argument is        :' $1”
echo “'The number of arguments is   :' $#”
echo “'The list of arguments passed :' $@”

