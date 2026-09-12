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

class Student(User):
    def greetStudent(self):
        print("Greet student...")

class Faculty(User):
    def greetFacutly(self):
        print("Greet faculty...")

class TempFacutly(Faculty):
    def tempFunction(self):
        print("This is temp function from temp facutly")