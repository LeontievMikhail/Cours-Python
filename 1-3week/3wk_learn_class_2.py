import shelve
s=shelve.open('myshelve.bin')
s['abc']=[1,2,3]
s.close()

s1=shelve.open('myshelve.bin')
print(s1['abc'])

