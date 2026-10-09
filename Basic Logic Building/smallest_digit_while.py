userInput = list(map(lambda num: int(num), input("Enter the numbers: ").split(" ")))
smallest = userInput[0]
i = 0
while i < len(userInput):
    if userInput[i] < smallest:
        smallest = userInput[i]
    i += 1

print(smallest)
