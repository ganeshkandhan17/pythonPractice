userInput = int(input('Enter the number: '))
product = 1
while userInput > 0:
    lastDigit = userInput%10
    product*=lastDigit
    userInput = int(userInput/10)

print(product)