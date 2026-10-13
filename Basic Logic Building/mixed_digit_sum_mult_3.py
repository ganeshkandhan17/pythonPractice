for i in range(1, 100 + 1):
    digit = i
    sum = 0
    while digit > 0:
        lastDigit = digit % 10
        sum += lastDigit
        digit = int(digit / 10)
    if sum % 3 == 0:
        print(i, end=' ')
