import json
import os


def parse_args():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--key', dest='key_name')
    parser.add_argument('--val', dest='value')

    return parser.parse_args()

def read_storage(file_name):
    with open(file_name) as f:
        storage = json.load(f)
        f.close()
    return storage


def save_storage(storage, file_name):
    with open(file_name, 'a') as f:
        json.dump(storage, f)
        f.close()


if __name__ == '__main__':
    args = parse_args()

    storage = dict()
    storage_file_name = os.path.join(os.path.dirname(__file__), 'storage.data')
    print('Storage:', storage_file_name)

    key = args.key_name
    val = args.value

    if os.path.exists(storage_file_name):
        if key and val:
            storage[key] = val
            print('Key "{}" = {}'.format(key, val))
            save_storage(storage, storage_file_name)

    else:
        save_storage(storage, storage_file_name)
        print(storage)

