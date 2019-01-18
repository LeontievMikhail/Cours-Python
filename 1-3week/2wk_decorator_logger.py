import functools

def logger(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        result=func(*args, **kwargs)
        with open('log.txt','w') as f:
            f.write(str(result))
        return result
    return wrapped

@logger
def summator(num_list):
    return sum(num_list)

summator([1,2,3,4,5])

with open('log.txt', 'r') as f:
    print('log.txt: {}'.format(f.read()))

print(summator.__name__)
