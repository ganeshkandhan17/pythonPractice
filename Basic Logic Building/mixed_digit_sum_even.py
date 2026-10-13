for i in range(1, 101):
    sum = 0
    digit = i
    while digit > 0:
        lastDigit = digit % 10
        sum += lastDigit
        digit = int(digit / 10)
    if sum % 2 == 0:
        print(i , end=' ')
