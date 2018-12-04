#файлы в родительскоми дочернем процессе

import os
f = open("ex4.txt")
foo = f.readline()

if os.fork() ==0:
    #child process
    foo = f.readline()
    print("child: ", foo)
else:
    #parent process
    foo=f.readline()
    print("parent: ", foo)

