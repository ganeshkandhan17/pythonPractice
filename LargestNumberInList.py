numbers = [1,2,3,4,55,6,7,8,9]
max=numbers[0]
for num in numbers:
    if max<num:
        max=num

print(max)