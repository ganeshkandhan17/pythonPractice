userInput= int(input('Enter the number: '))
for i  in range(1, userInput+1):
    for j in range(1,11):
        print(f'{i} * {j} = {i*j}')
    print('')