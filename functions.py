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

# default argument or optional argument
def defaultArgument(fname, lname=''):
    print(f"Welcome {fname} {lname}")

defaultArgument('Ganesh', 'kandhan')

# passing list

def printList(list):
    for i in range(0, len(list)):
        list[i] = list[i].title()
        print(list[i], end=' ')

list1= ['Ganesh', 'kandhan', 'v', 'm']
printList(list1.copy())
print(list1)
