import sys
import print_usage #local
from os import path

#from .classmodule import MyClass
#from .funcmodule import my_function

def main():
    args = sys.argv[1:]

    if len(args) == 0: #no args supplied
        print_usage.name()
        print_usage.usage()
        print_usage.description()
        exit()

    if ("-h" in args) or ("--help" in args):
        print_usage.all()
        exit()

    if path.exists(sys.argv[1]):
        print("file exists")
    else:
        print("file doesnt exist")

    print('count of args :: {}'.format(len(args)))
    for arg in args:
        print('passed argument :: {}'.format(arg))

if __name__ == '__main__':
    main()
