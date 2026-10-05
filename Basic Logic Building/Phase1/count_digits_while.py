userInput = int(input('Enter the number: '))
count = 0
while userInput > 0:
    lastDigit = userInput%10
    count+=1
    userInput = int(userInput/10)
print(count)
    