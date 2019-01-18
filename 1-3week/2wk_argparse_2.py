import argparse

parser=argparse.ArgumentParser()
parser.add_argument('-a', default='__')
p=parser.parse_args()
print(p.a)

parser1=argparse.ArgumentParser()
parser1.add_argument('-a')
p=parser1.parse_args()
print(p.a)

parser2=argparse.ArgumentParser()
parser2.add_argument('-a')
p=parser2.parse_args()
print(p.a)

parser3=argparse.ArgumentParser()
parser2.add_argument('-a')
p=parser3.parse_args()
print(p.a)