numerator = int(input('Enter numerator : '))
denominator = int(input('Enter denominator : '))
try:
    result = numerator/denominator
except ZeroDivisionError as e:
    print("denominator can't be 0")
except ValueError as e:
    print('Numerator and denominator must be a number')
else:
     print('{:.2f}'.format(result))
finally:
    print('completed')
