a=int(input('Number1: '))
b=int(input('Number2: '))

if a<b:
    while a<=b:
        if a%7==0:
            print(a)
        a+=1
else:    
    while b<=a:
        if b%7==0:
            print(b)
        b+=1
