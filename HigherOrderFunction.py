def happy():
    print('Jumping...')

def sad():
    print('Crying...')

h = happy
s = sad

print(h) # <function happy at 0x000002B3EB59FAB0>
print(s)

h() # This will call happy function
s()

def happy1(paramFunction,):
    paramFunction()
    return sad

value = happy1(h)
value()

happy1(h)()


