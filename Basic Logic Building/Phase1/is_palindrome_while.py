userInput = int(input('Enter the number: '))
value = userInput
reversed = 0
while userInput > 0:
    lastDigit = userInput%10
    reversed=(reversed*10)+lastDigit
    userInput=int(userInput/10)

if reversed == value:
    print('Its palindrome')
else:
    print('Its not a palindrome')