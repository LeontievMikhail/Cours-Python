import json
import functools


def to_json(f):
    @functools.wraps(f)
    def wrapper(*args, **kwds):
        return json.dumps(f(*args, **kwds))

    return wrapper


@to_json
def get_data():
    return {'data': 42}


print(get_data())