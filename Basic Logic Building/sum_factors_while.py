try:
    userInput=int(input('Enter the number: '))
    init=1
    sum=0
    while init<=userInput:
        if userInput%init==0:
            sum+=init
        init+=1
    print(sum)
except KeyboardInterrupt:
    print('\nManual Exit')