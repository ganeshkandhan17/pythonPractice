userInput = int(input("Enter the number: "))
binary = ""
while userInput > 0:
    binary = str(userInput % 2) + binary
    userInput = int(userInput / 2)
print(binary)
