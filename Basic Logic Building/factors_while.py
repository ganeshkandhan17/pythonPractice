userInput = int(input('Enter the value: '))
init = 1
while init<=userInput:
    if userInput%init==0:
        print(init)
    init+=1