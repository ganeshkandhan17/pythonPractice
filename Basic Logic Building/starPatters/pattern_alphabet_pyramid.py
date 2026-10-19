userInput = int(input("Enter the value: "))
charValue = 65
for i in range(1, userInput + 1):
    for j in range(userInput + 1, 1, -1):
        if i < j:
            print(" ", end="")
    for k in range(1, (userInput + 1)*2):
        if k < i*2:
            print(chr(charValue), end='')
            charValue += 1
    print()
