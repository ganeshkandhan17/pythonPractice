userInput = int(input('Enter the number : '))
sum=0
while userInput > 0:
    if userInput%2!=0:
        sum+=userInput
    userInput-=1
print(sum)
