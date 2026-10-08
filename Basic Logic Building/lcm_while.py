userInput = int(input('Enter number 1: '))
userInput1= int(input('Enter number 2: '))
init = 1
lcm = init
product = userInput*userInput1
while init <= product:
    if init%userInput1==0 and init%userInput==0:
        lcm=init
        break
    init+=1
print(lcm)

