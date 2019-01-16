class parent(object):
    def __init__(self):
        self.__f=2

    def get(self):
        return self.__f

class child(parent):
    def __init__(self):
        self.__f=1
        parent.__init__(self)
    def get(self):
        return self.__f

c=child()
print(c.get())
print(c.get())
