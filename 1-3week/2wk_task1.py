import json,os,tempfile,argparse

def read_data(storage_file):
    if os.path.exists(storage_file):
        print('file finded', storage_file)
        with open(storage_file, 'r') as f:
            data=json.load(f)
            f.close()
            return data


if __name__ == '__main__':
    data={'name':(1,3)}
    storage_file = os.path.join(tempfile.gettempdir(), 'storage.data')
    #storage_file = os.path.join(os.path.dirname(__file__), 'storage.data')
    parser = argparse.ArgumentParser()
    parser.add_argument('--key')
    parser.add_argument('--val')
    p = parser.parse_args()
    data[p.key]=p.val
    if p.key and p.val:
        #print('insert data', data)
        rd = read_data(storage_file)
        #print('data on file', rd)
        if os.path.exists(storage_file): data.update(rd)

        with open(storage_file, 'w') as w:
            #print(data)
            json.dump(data, w)
            w.close()

    if p.key and not p.val:
        rd=read_data(storage_file)
        print(rd[p.key])