userInput = int(input('Enter the number: '))
temp1 = userInput
temp2 = userInput
count=0
while userInput>0:
    count+=1
    userInput=int(userInput/10)

armstrongValue = 0
while temp1>0:
    lastDigit = temp1%10
    armstrongValue+=lastDigit**count
    temp1=int(temp1/10)

if armstrongValue == temp2:
    print('its armstrong number')
else:
    print('its not a armstrong number')


