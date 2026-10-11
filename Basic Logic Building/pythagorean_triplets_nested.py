userInput = int(input("Enter the value: "))
for a in range(1, userInput + 1):
    for b in range(a + 1, userInput + 1):
        for c in range(b + 1, userInput + 1):
            if a * a + b * b == c * c:
                print(a, b, c)
