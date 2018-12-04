#thread creation

from threading import Thread

def f(name):
    print("hello", name)

th=Thread(target=f, args=("Dod",))
th.start()
th.join()

