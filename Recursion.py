# Factorial

def rec(num):
    if num==0:
        return 1
    return num * rec(num-1)

print(rec(4))

# Fibonacci Series

# series = ''
# def fibonacci(num):
#     global series
#     if num <= 1:
#         return str(1)
#     return series +  str(fibonacci(num-1) + fibonacci(num-2))

# print(fibonacci(10))