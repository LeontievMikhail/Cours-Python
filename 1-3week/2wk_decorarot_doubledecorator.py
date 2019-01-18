def first_decorator(func):
    def wrapped():
        print('Inside first_decotarot product')
        return  func()
    return wrapped

def second_decorator(func):
    def wrapped():
        print('Inside second_decorator product')
        return func()
    return wrapped

@first_decorator
@second_decorator

def decorated():
    print('Finally called...')

#decorated = first_decorator(second_decorator(decorated))

decorated()