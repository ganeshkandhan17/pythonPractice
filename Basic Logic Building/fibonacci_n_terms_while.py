userInput= int(input('Enter the number: '))
first  = 0 
second = 1
third = first + second
sum = first + second
print(f'{first}, {second}, ', end='')
for i in range (userInput-2):  
    sum += third 
    print(f'{third}, ', end="")
    first = second
    second = third
    third = first + second

print(f'\n{sum}')

