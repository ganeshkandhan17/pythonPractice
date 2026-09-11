class User:
    users = 0 # Class variable

    def __init__(self, name, password):
        self.name = name #  Instance variable
        self.password = password
        User.users+=1

    def register(self):
        print(f'{self.name} is registering...')

    def login(self):
        print(f'{self.name} is logging in...')