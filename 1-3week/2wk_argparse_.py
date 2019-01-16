import argparse
import sys

def createParser():
    parser=argparse.ArgumentParser()
    parser.add_argument('-n', '--name', nargs='+', default=['Миша'])
    return parser

if __name__=='__main__':
    parser=createParser()
    namespace=parser.parse_args(sys.argv[1:])
    print(namespace)
    for name in namespace.name:
        print(str(name))



