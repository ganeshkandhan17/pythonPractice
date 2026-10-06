userInput = int(input(''))
factorial = 1

while userInput > 0:
    factorial*=userInput
    userInput-=1
print(factorial)