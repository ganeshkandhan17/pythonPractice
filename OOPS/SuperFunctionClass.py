class User:
    users = 0 # Class variable

    def __init__(self, name, password):
        self.name = name #  Instance variable
        self.password = password
        User.users+=1

    def register(self):
        print(f'{self.name} is registering...')
        return self

    def login(self):
        print(f'{self.name} is logging in...')
        return self

class Student(User):
    def __init__(self, name, password, course, fee):
        super().__init__(name, password)
        self.course = course
        self.fee = fee
    
    def greet(self):
        print("Greet student...")

class Faculty(User):
    def greet(self):
        print("Greet faculty...")

class TempFacutly(Faculty):
    def greet(self):
        print("Greet temp facutly")

class StudentFaculty(Student,Faculty):
    def greet(self):
        print('Greet as both student and facutly')