userInput = int(input("Enter the number: "))
number = 0
for i in range(1, userInput + 1):
    for j in range(1, userInput + 1):
        if j <= i:
            if number % 2 == 0:
                print(1, end="")
            else:
                print(0, end="")
            number += 1
    print()
