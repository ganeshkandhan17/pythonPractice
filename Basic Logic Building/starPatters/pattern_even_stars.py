userInput = int(input("Enter the value= "))
for i in range(1, userInput + 1):
    for j in range(1, (userInput + 1) * 2):
        if i * 2 >= j:
            print("*", end="")
    print()
