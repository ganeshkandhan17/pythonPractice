import random

generatedNumber = random.randint(1,20)

print(generatedNumber)
userInput = int(input('Enter the number, guess that is less than 20: '))

while generatedNumber!=userInput:
    if userInput<=generatedNumber:
        print('Higher')
    else:
        print("Lower")
    userInput = int(input("Try again : "))

print("You guess is right and u won")