userInput1= int(input('Enter number 1: '))
userInput2 = int(input('Enter number 2: '))
init=1
hcf=init
while init <= userInput1 or init <=userInput2:
    if userInput1%init==0 and userInput2%init==0:
        hcf=init
    init+=1
print(hcf)