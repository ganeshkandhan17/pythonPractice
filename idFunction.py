a=10
b=11
c=10
# ID function will return the unique reference number for each variable
print(id(a))
print(id(a)==id(b)) # False
print(id(a)==id(c)) # True