userInput = int(input('Enter the value: '))
factor = 0
for i in range(1,userInput+1):
    for j in range(1, i+1):
        if i%j==0:
            factor+=1
    print(f'{i}  => {factor}')
    factor=0