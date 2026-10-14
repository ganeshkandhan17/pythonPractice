for i in range(1, 1000):
    digit = i
    count = 0
    while digit > 0:
        count += 1
        digit = int(digit / 10)
    digit = i
    sum = 0
    while digit > 0:
        lastDigit = digit % 10
        sum += lastDigit**count
        digit = int(digit / 10)
    if sum == i:
        print(i)
