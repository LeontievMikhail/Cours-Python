import json,os,tempfile,argparse

def read_data(storage_file):
    if os.path.exists(storage_file):
        #print('file finded', storage_file)
        with open(storage_file, 'r') as f:
            data=json.load(f)
            f.close()
            return data

if __name__ == '__main__':
    data={'a':[1,2,3]}
    storage_file = os.path.join(tempfile.gettempdir(), 'storage.data')
    #print(storage_file)
    #storage_file = os.path.join(os.path.dirname(__file__), 'storage.data')
    parser = argparse.ArgumentParser()
    parser.add_argument('--key')
    parser.add_argument('--val')
    p = parser.parse_args()
    key=p.key
    val=p.val
    #------ читаем данные из файла и добавляем новые
    if p.key and p.val:
        if os.path.exists(storage_file):
            rd = read_data(storage_file)

            if key in rd:
                  rd[key].append(val)
            else:
                data[key]=[]
                data[key].append(val)
        else:
            data[key] = []
            data[key].append(val)


        if os.path.exists(storage_file): data.update(rd)

        with open(storage_file, 'w') as w:
            #print(data)
            json.dump(data, w)
            w.close()

    if p.key and not p.val:
        rd=read_data(storage_file)
        try:
            print(rd[p.key])
        except:
            pass