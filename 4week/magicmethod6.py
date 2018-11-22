class Researcher:
    def __getattr__(self,name):
        return 'Nothing found :()\n'

    def __getattribute__(self,name):
        print('Looking for {}'.format(name))
        return object.__getattribute__(self,name)

obj = Researcher()

print(obj.attr)
print(obj.method)
print(obj.SFSFSAFASFASF)