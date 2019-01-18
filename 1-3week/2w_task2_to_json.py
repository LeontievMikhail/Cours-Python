import json
import functools

def to_json(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        return json.dumps(func(*args, **kwargs))
    return wrapped


@to_json
def get_data(parm):
    return {
        'data': parm
    }

get_data(45454)
print(get_data(45))