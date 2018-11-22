import random
class NoisyInt:
    def __init__(self, value):
        self.value = value

    def __add__(self,obj):
        noise=random.uniform(-1,1)
        return self.value + obj.value + noise

a = NoisyInt(10)
b = NoisyInt(20)

for _ in range(22):
    print(a+b)
