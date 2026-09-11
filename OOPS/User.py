class User:
    # name = None
    # password = None

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def register(self):
        print(f'{self.name} is registering...')

    def login(self):
        print(f'{self.name} is logging in...')