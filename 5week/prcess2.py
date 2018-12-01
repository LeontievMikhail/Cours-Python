import time
import os

pid = os.fork()
if pid == 0:
    while True:
        print("child: ", os.getpid())
        time.sleep(5)
else:
    print("parrent: ", os.getpid())
    os.wait()