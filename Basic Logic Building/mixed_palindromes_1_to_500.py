for i in range(1, 500 + 1):
    digit = i
    reversed = ""
    while digit > 0:
        lastDigit = digit % 10
        reversed = reversed + str(lastDigit)
        digit = int(digit / 10)
    if str(i) == reversed:
        print(i, end=' ')
