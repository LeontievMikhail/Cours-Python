import urllib
from urllib import request
from urllib.parse import quote
import re, os,sys

def findyoutube(x):
    mas=[]
    sq='http://youtube.com/results?search_query='+quote(x)
    doc=urllib.request.urlopen(sq).read().decode('cp1251',errors='ignore')
    match=re.findall("\?v\=(.+?)\"", doc)
    if not(match is None):
        for ii in match:
            if(len(ii)<25):
                mas.append(ii)
    mas=dict(zip(mas,mas)).values()
    mas2=[]
    for y in mas:mas2.append('http://www.youtube.com/watch?v='+y)
    return mas2

mmm=findyoutube('сливки+шоу')
for i in mmm:
    print(i)

