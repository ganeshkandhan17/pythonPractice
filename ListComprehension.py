# Square root for 10 natural numbers
sqrt1 = list(map(lambda x : x*x, range(1,11)))
print(sqrt1)
sqrt = [x*x for x in range(1,11)]
print(sqrt)

# Combine with if statement
sqrtGrt30 = [x*x for x in range(1,11) if x*x > 30]
print(sqrtGrt30)

# Combine with else if 
sqrtGrt30Else0 = [x*x if x*x > 30 else 0 for x in range(1,11)]
print(sqrtGrt30Else0)
