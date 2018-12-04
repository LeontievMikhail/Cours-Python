import os
foo = "bar"

if os.fork() == 0:
    #child process
    foo = "bax"
    print('child: ', foo)
else:
    #Parental process
    print("parent: ", foo)
    os.wait()

