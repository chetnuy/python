#!/bin/python

#Обработка аргументов запуска
import sys
import getopt

def usage():
    print ('Help!!!')

# стоит обратить внимание на формат передачи некоторые ключи требуют key=value
try:
    options, args = getopt.getopt(sys.argv[1:], 'd:o:h', ['debug=', 'option=', 'help'])
except getopt.GetoptError:
    usage()
    sys.exit(2)

for opt, value in options:
    if opt in ('-h', '--help'):
        usage()
        sys.exit(0)
    elif opt in ('-d', '--debug'):
        debug_flag = value
        print ('debug flag: ', debug_flag)
    elif opt in ('-o', '--option'):
        option = value
        print ('option: ', option)
    else:
        print('Hhelp')
