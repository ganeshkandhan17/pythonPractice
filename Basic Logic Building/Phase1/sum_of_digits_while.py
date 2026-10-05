userInput = int(input('Enter the  number: '))
sum=0
while userInput>0:
    lastDigit = userInput%10
    sum+=lastDigit
    userInput=int(userInput/10)
print(sum)