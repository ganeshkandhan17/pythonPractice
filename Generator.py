# Square number function

def sqr_num(num):
    l = []
    for i in range(num+1):
        l.append(i*i)
    return l

print(sqr_num(10))

# Same square number using generator, 
# normal function will consume more RAM resources if we generate more than lakhs of value
# in those cases generator using yield keyword will reduce the consumption

def sqr_number_gen(num):
    for i in range(num+1):
        yield i*i

print(sqr_number_gen(10))
for i in sqr_number_gen(10):
    print(i)