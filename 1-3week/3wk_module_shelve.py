import shelve
s = shelve.open("somefile.db")
s['myobject']=[1,2,3,4,5,6,7,'свечка']
s['ourobjeck']={1:1,2:2,3:3,4:4}
s.close()

s1=shelve.open("somefile.db")
print(s1['myobject'])
print(s1['ourobjeck'])

print('___')
print(s1.items())

