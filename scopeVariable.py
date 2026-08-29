def greet(name):
    print(f'welcome {name}')

greet("ganesh")
print(name) # Throw error because not name in this scope

# Global keyword
num = 10

def increaseNumValue():
    global num
    num=20

increaseNumValue()
print(num)