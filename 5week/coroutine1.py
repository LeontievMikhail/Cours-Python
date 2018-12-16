def grep(pattern):
    print("start grep")
    while True:
        line = yield
        if pattern in line:
            print(line)

g=grep("python")
next(g) #g.send(None)

g.send("12312312313123")
g.send("python in simple!")
g.send("python is not simple")
g.send("it is not python")