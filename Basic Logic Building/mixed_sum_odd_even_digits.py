userInput = input("Enter the value: ")
oddSum = 0
evenSum = 0
for i in userInput:
    number = int(i)
    if number % 2 == 0:
        evenSum += number
    else:
        oddSum += number
print(f"odd sum = {oddSum}\neven sum = {evenSum}")
