row = int(input('enter number of rows : '));

for i in range(1, row + 1):
    for j in range (1,row + 1):
        if(i >= j):
            print(i, end='')
    print('')