class ImportantValue:
    def __init__(self,amount):
        self.amount = amount

    def __ge__(self, obj, obj_type):
        return self.amount

    def __set__(self, obj, value):
        with open('log.txt', 'w') as f:
            f.write(str(value))

        self.amount = value

class Account:
    amount= ImportantValue(100)

mim_account=Account()
mim_account.amount=200

with open('log.txt', 'r') as f:
    print(f.read())
    