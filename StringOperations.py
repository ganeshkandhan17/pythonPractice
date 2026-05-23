testString = 'This is text string'

concat = 'this' + 'new this'
print(f'concat string: {concat}')

lowerCase = testString.lower()
print(f'lower case: {lowerCase}')

upperCase = testString.upper()
print(f'upper case: {upperCase}')

titleCase = testString.title()
print(f'each word 1st letter is changed to capital: {titleCase}')

# Trim function
strip = testString.strip()
print(f'Striped test : {strip}')

substring1 = testString[0:4]
print(f'sustring1: {substring1}')

substring2 = testString[:4]
print(f'Susstring2: {substring2}')

substring3 = testString[5:]
print(f'susstring3: {substring3}')

substring4 = testString[-3:]
print(f'substring4 (last 3): {substring4}')

removeSpace = testString.replace(" ", "")
print(f'space removed: {removeSpace}')

replaced = testString.replace("This", "that")
print(f'this replaced to that: {replaced}')

array = ['ganesh','kandhan','v','m']
joined = ' '.join(array)
joined = joined.title()
print(f'Joined string : {joined}')
