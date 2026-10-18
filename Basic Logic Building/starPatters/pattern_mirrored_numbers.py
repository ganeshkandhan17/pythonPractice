userInput = int(input("Enter the number: "))
number = 1
for i in range(1, userInput + 1):
    for j in range(1, userInput + 1):
        if j <= i:
            print(number, end="  ")
            if number == 9:
                number = 0
            else:
                number += 1
    print()
