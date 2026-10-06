def isPrime(num):
    flag = True
    for i in range(2,num):
        if num%i==0:
            flag = False
    return flag

for i in range(2,101):
    if isPrime(i):
        print(i, end=', ')