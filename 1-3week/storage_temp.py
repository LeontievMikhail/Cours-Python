import json
import random
import os

storage_file = os.path.join(os.path.dirname(__file__), 'temp_storage.data')
data={'a':[1,2,3]}

if os.path.exists(storage_file):
    with open(storage_file, 'r') as w:
        data=json.load(w)
        w.close

print(data)
key='a'
val=random.randint(111,122)
if str(key) in data:
    data[key].append(val)
else:
    data[key]=val
print(data)

with open(storage_file, 'w') as f:
    json.dump(data, f)
    f.close()

print(type([1]))