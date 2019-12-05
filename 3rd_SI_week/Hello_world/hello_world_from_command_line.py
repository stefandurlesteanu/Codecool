import sys


if len(sys.argv) == 1:
    print ("Hello World!")
else:
    for arg in sys.argv[1:]:
        print ("Hello" + ' ' + arg + '!')


