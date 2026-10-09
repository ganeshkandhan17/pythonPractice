userInput = list(map(lambda num: int(num), input("Enter the numbers: ").split(" ")))
i = 0
largest = userInput[i]
while i < len(userInput):
    if userInput[i] > largest:
        largest = userInput[i]
    i += 1
print(largest)
