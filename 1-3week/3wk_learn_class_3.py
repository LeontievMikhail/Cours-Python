class Pet:
    pass

class Dog(Pet):
    pass

class ExportJSON(Pet):
    pass

class ExDog(Dog, ExportJSON):
    pass

print(isinstance(Dog(),Pet))

print(issubclass(Pet, Dog))