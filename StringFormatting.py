name = 'ganesh'
like1 = 'chicken'
like2 = 'chocolate'

text = "{} like {} and {}"
format1 = text.format(name,like1,like2)
print(format1)

text2 = "{0} like {1} and {2}"
print(text2.format("ganesh", "nothing", "ganesh"))

text3 = "{name} like {like1} and {like2}"
print(text3.format(name=name,like1=like1,like2=like2))

text4="this is {name}".format(name='ganesh')
print(text4)

# Padding
padding1 = '*****{:8}*****'
print(padding1.format('Welcome'))

# Padding align
padding1 = '*****{:>8}*****'
print(padding1.format('Welcome'))

padding2 = '*****{:<8}*****'
print(padding2.format('Welcome'))

# Center align
padding3 = '*****{:^20}*****'
print(padding3.format('Welcome'))