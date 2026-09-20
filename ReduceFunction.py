
from functools import reduce
nums = [1, 2, 3, 4]
'''
Step 1: add(1, 2) → 3
Step 2: add(3, 3) → 6
Step 3: add(6, 4) → 10
Final Result → 10
'''
sum = reduce(lambda x,y :x+y,nums)
print(sum)


chars = ['g','a','n','e','s','h']
joined = reduce(lambda f,s: f+s, chars)
print(joined)


