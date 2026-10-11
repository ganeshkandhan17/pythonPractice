userInput = int(input("Enter the number: "))

a = 0
b = 1


def getNextFabSeries():
    global a, b
    a, b = b, a + b
    return a


for i in range(userInput):
    for k in range(userInput - i):
        print(" ", end="")
    for j in range(userInput * 2):
        if i * 2 < j:
            continue
        print(getNextFabSeries(), end="")
    print()
