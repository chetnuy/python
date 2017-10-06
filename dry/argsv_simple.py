#!/bin/python
#простой способ получить доступ к параметрам запуска срипта, без разбора параметров
# import sys
# print ("This is the name of the script: ", sys.argv[0])
# print ("Number of arguments: ", len(sys.argv))
# print ("The arguments are: " , str(sys.argv))

import argparse
parser = argparse.ArgumentParser(description='Anda - Simple diary for live')
# The -- indicates that it is optional
parser.add_argument('-v', '--verbose', help='verbose about programm', action='store_true')
args = parser.parse_args()

if args.verbose:
    print ("verbosity turned on")
else:
    print ("Default option")