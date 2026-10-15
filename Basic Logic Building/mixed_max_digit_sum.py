userInput = int(input("Enter the value: "))
largestSum = 0
number = 0
for i in range(1, userInput + 1):
    sum = 0
    digit = i
    while digit > 0:
        lastDigit = digit % 10
        sum += lastDigit
        digit = int(digit / 10)
    if largestSum < sum:
        largestSum = sum
        number = i
print(f"{number} = {largestSum}")
