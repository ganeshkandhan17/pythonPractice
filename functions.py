def greet():
    print("Welcome")

greet()


def greet(name):
    print(f"Welcome {name}")
greet("Ganesh")

def greet(fname, lname):
    print(f"Welcome {fname} {lname}")
greet(fname='Ganesh', lname='Kandhan')
greet(lname='Kandhan', fname='Ganesh')

def sum(num):
    temp=0
    for i in range(1, num+1):
        temp+=i

    return temp

print(sum(5))