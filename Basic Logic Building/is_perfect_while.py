userInput = int(input('Enter the number: '))
temp1=userInput
divisor =[]
while temp1 > 0:    
    if userInput%temp1==0 and userInput!=temp1:
        divisor.append(temp1)
    temp1-=1

sum=0 

for div in divisor:
    sum+=div

if sum==userInput:
    print('Its a perfect number')
else:
    print('Its not a perfect number')