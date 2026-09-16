# walrus operator
# If I need to do some operations while assign value to variable

# Normal method
list1  = []
while True:
    num = int(input())
    if num ==-1:
        break
    list1.append(num)
print(list1)

# Using walrus method
list2 = []
while (num:=int(input())) !=-1:
    list2.append(num)
print(list2)