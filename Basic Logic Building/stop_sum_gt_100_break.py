sum = 0
for i in range(1, 101):
    if sum > 100:
        print(f"last sum value: {i}")
        break
    sum += i

print(sum)
