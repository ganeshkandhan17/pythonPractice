dbList = [1,2,3,4,5]
userInput = int(input('Enter the number to search: '))
for i in dbList:
    print(i)
    if userInput == i:
        print('Found in list')
        break
