userInput = int(input("Enter  the number: "))
for i in range(1, userInput + 1):
    for j in range(userInput + 1, 1, -1):
        if i < j:
            print(" ", end="")
    for k in range(1, i * 2):
        print("*", end="")
    print()
