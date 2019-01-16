def even_range(stard, end):
    current = start
    while current < end:
        yield current
        current += 2

def list_generator(list_obj):
    for item in list_obj:
        yield item
        print('After yieldin {}'.format(item))

generator = list_generator([1,2])

next(generator)

next(generator)
