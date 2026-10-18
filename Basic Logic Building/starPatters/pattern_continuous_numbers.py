userInput = int(input("Enter the value: "))
num = 1
for i in range(1, userInput + 1):
    for j in range(1, userInput + 1):
        if j <= i:
            print(num, end=" ")
            num += 1
    print()
