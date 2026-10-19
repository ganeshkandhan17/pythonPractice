userInput = int(input("Enter the value: "))
num = 64
for i in range(1, userInput + 1):
    for j in range(1, userInput + 1):
        if j <= i:
            print(chr(num + i), end="")
    print()
