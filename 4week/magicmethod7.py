class Ignorant:
    def __setattr__(self,name,value):
        print('Not found set{}!'.format(name))

obj=Ignorant()
obj.math = True

print(obj.math)