userInput = int(input('Enter a number: '))
sum = 0
while userInput > 0:
    sum+=userInput
    userInput-=1
print(sum)