def shout(word="Yes"):
    return word.capitalize()+"!"

print(shout())

scream=shout()

print(scream)

del shout

try:
    print(shout())
except NameError as e:
    print("Error: ",e)

print(scream)

