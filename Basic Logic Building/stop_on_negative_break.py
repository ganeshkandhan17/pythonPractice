dbList = [1, 2, 3, 4, 5, -1, 32, 45]
for i in dbList:
    if i < 0:
        print(f"negative  numbers found {i}")
        break
    print(i)
