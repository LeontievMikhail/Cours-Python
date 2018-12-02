import os

foo="bar"

if os.fork() ==0:
    #child process
    foo = "baz"
    print("child: ", foo)

else:
    #parental process
    print("parent: ", foo)
    os.wait()

