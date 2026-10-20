userInput = int(input("Enter the number: "))
for i in range(1, userInput + 1):
    for j in range(1, userInput + 1):
        if j <= i:
            print("*", end="")
    print()
for i in range(1, userInput):
    for j in range(userInput, 1, -1):
        if j > i:
            print("*", end="")
    print()
