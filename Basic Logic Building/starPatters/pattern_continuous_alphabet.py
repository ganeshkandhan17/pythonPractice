userInput = int(input("Enter the number: "))
num = 65
for i in range(1, userInput + 1):
    for j in range(1, userInput + 1):
        if j <= i:
            print(chr(num), end='')
            num+=1
    print()
