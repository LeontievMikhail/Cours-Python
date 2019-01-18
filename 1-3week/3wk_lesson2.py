class Planet:

    count = 0

    def __init__(self, name, population=None):
        self.name = name
        self.population = population or []
        Planet.count += 1


earth = Planet("Earth")

marc= Planet("Mars")

print(Planet.count)
print(marc.count)
print(earth.count)

print(dir(Planet))

class Planet:
    def __new__(cls, *ars, **kwargs):
        print("__new__called")
        obj = super().__new__(cls)
        return obj

    def __init__(self, name):
        print("__init__called")
        self.name

