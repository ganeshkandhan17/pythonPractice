def isPrimeNumber(num):
    isPrime = True
    for i in range(2,num):
        if num%i==0 :
            isPrime = False
    return isPrime

count = 0
num = int(input('Enter number : '))
i=2
print(isPrimeNumber(i))
primeList=[]
while count !=num:
    if isPrimeNumber(i):
        primeList.append(i)
        count+=1
    i=i+1
print(primeList)
