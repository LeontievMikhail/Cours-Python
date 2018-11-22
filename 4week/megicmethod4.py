class User:
    def __init__(self, name, email):
        self.name=name
        self.email=email

    def __hash__(self):
        return hash(self.email)

    def __eq__(self,obj):
        return self.email == obj.email


jane = User('Jane Doe', 'jdoe@ex.com')
joe = User('Joe Doe','jdoe@ex.com')

print(jane==joe)

print(hash(jane))
print(hash(joe))

user_email_map={user: user.name for user in [jane, joe]}
print(user_email_map)