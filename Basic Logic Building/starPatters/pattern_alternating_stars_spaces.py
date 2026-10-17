userInput = int(input("Enter the value: "))
for i in range(1, userInput + 1):
    for j in range(userInput + 1, 1, -1):
        if j > i:
            print(" ", end="")
    for k in range(1, i * 2):
        if k % 2 == 0:
            print(" ", end="")
        else:
            print("*", end="")
    print()
