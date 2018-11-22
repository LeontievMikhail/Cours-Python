class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_email_data(self):
        return {
            'name': self.name,
            'email': self.email
        }

jane = User ('Jame Doe', 'janedoe@example.com')

print(jane.get_email_data())