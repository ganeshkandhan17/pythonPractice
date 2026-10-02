continuousLoop= True
while continuousLoop:
    try:
        userInput = int(input('Enter number : '))
        num = 1
        while num <=10:
            print(f'{userInput} x {num} = {userInput*num}')
            num+=1   
        continuousLoop = False     
    except Exception as e:
        print('Please Enter valid Number')
    