# Fix decimal points
pi=3.14235432343
text="decimal fixed of pi {pi:.2f}"
print(text.format(pi=pi))

# Print in Binary
num2=10
print("{:b}".format(num2))

# Print in Binary
num2=1000
print("{:x}".format(num2))

# Print octa
num3=3298732048
print("{:o}".format(num3))

# Print E^
num4=54321841398741568484
print("{:e}".format(num4))

# Comma formatted
print("{:,}".format(num4))
print(f"pi : {pi:.2f}")