userInput = int(input('Enter the number: '))
reversed = 0
while userInput > 0:
    lastDigit = userInput%10
    reversed = (reversed*10) + lastDigit
    userInput = int(userInput/10)
print(reversed)