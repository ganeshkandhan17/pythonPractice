userInput = input("Enter the number: ")
numberArray = list(map(lambda num: int(num), userInput))
sum = 0
for i in numberArray:
    if i == 0:
        continue
    sum += i
print(sum)
