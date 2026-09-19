# Lambda is function is a anonymous function

x= lambda x,y : x*y

print(x(7,2))

y = lambda a,b : a+b
print(y(1,90))

strong_enough = lambda w : 'yes' if w>20  else 'No'
print(strong_enough(19))