userInput = int(input("Enter the number: "))
for i in range(1, userInput + 1):
    for j in range(1, userInput + 1):
        if i >= j:
            print("*", end="")
    print()
