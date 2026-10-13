count = 0
for i in range(1, 500 + 1):
    if i % 7 == 0 and i % 5 != 0:
        count += 1
print(count)
