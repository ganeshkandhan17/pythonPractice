userInput = int(input("Enter the number: "))
binary = ""
while userInput > 0:
    binary = binary + str(userInput % 2)
    userInput = int(userInput / 2)
print(binary)
