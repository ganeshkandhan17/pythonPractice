userInput = input(f"Enter number of columns = ")

try:
    column = int(userInput)
except Exception as e:
    print(f"Please enter only numbers")

for col in range(column):
    print("*", end=" ")