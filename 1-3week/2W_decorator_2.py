def bread(func):
    def wrapper():
        print("+++++++++++++++++")
        func()
        print("______________")
    return wrapper

def ingredients(func):
    def wrapper():
        print("#помидорный")
        func()
        print("салат")
    return wrapper

#@bread
@ingredients
def sandwich(food="ветчина"):
    print(food)

sandwich()
