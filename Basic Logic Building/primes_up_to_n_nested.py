userInput = int(input("Enter number: "))
init = 2
primeCount = 0

while True:
    if primeCount == userInput:
        break
    isPrimeFlag = True
    for i in range(2, init):
        if init % i == 0:
            isPrimeFlag = False
    if isPrimeFlag:
        print(init, end=', ')
        primeCount+=1
    init += 1
