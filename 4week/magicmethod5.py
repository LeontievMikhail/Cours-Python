class Researcher:
    def __getattr__(self,name):
        return 'Nothing found :('

    def __getattribute__(self, name):
        return 'nope'

obj = Researcher()

print(obj.attr)
print(obj.method)
print(obj.DFHJHGHJGHJGJH)