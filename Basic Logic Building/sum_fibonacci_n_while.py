userInput = int(input('Enter the value: '))
first = 0
second = 1
third = first
print(f'{first}, {second}, ')
for i in range(userInput):
    print(f'{first + second}, ')
    first = second
    second = first + second
