testString='logic first tamil'

"""
# String:           'l   o   g   i   c   f   i   r   s   t       t   a   m   i   l'
# Positive Index:    0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15
# Negative Index:  -16 -15 -14 -13 -12 -11 -10  -9  -8  -7  -6  -5  -4  -3  -2  -1
"""


substring1 = testString[0:4]
print(f'sustring1: {substring1}')

substring2 = testString[:4]
print(f'Susstring2: {substring2}')

substring3 = testString[5:]
print(f'susstring3: {substring3}')

substring4 = testString[-3:]
print(f'substring4 (last 3): {substring4}')

print(testString[-9:])

# step
print(testString[0::2])

reversed = testString[::-1]
print(reversed)