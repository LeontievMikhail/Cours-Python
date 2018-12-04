import json, random
filename= "user_settings.txt"


#---------- чтение данных

myfile= open(filename, 'r')
mydata = json.load(myfile)
print(mydata)

#------------ запись данных
myfile = open(filename, 'w')
#mydata={'name':[1,2,3]}
mydata['name'].append(random.randint(0,100))
json.dump(mydata, myfile)
