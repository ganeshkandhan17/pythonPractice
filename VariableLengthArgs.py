# it take args a tuple
def sum(*args): 
    sum=0
    for i in args:
        sum +=i
    return sum

print(sum(1,2,3,4,5,6))

# it take args as dictionary
def printAll(**args): 
    for key,value in args.items():
        print(value, end=' ')

printAll(fName='Ganesh Kandhan', lName='V M')

