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

removeSpace = testString.replace(" ", "")
print(f'space removed: {removeSpace}')

replaced = testString.replace("This", "that")
print(f'this replaced to that: {replaced}')

array = ['ganesh','kandhan','v','m']
joined = ' '.join(array)
joined = joined.title()
print(f'Joined string : {joined}')

splittingString="ganesh kandhan"
split = splittingString.split(" ")
print(f"split string {split}")

digit = 'ganesh'
print(digit.isdigit())
