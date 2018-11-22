class Logger:
    def __init__(self,filename):
        self.filename = filename

    def __call__(self, func):
        with open(self.filename, 'a') as f:
            f.write('Oh Danny boy...\n')
        return func

logger = Logger('log.txt')

@logger
def completly_useless_function():
    pass


completly_useless_function()

with open('log.txt') as f:
    print(f.read())