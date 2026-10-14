userInput = int(input("Enter the value: "))
for i in range(1, userInput + 1):
    digit = i
    binary = ""
    while digit > 0:
        binary = str(digit % 2) + binary
        digit = int(digit / 2)
    count = 0
    for j in binary:
        if j == "1":
            count += 1
    if count % 2 == 0:
        print(i)
