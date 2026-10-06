userInput = int(input('Enter the number: '))
isPrime=True
start=2
while start < userInput:
    if userInput%start==0:
        isPrime=False
        break
    start+=1

if isPrime:
    print('Its a prime number')
else:
    print('Its not a prime number')
