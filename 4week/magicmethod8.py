class Polite:
    def __delattr__(self,name):
        value = getattr(self,name)
        print(f'Goodbye{name},you were {value}!')

        object.__delattr__(self,name)

obj = Polite()

obj.attr = 10
del obj.attr

