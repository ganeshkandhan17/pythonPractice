import math

userInput = int(input("Enter the value: "))
for i in range(1, userInput + 1):
    for j in range(userInput + 1, 1, -1):
        if i < j:
            print(" ", end="")
    num = 1
    for k in range(1, (userInput + 1) * 2):
        if k < i * 2:
            print(num, end="")
            if i > k:
                num += 1
            else:
                num -= 1
    print()
