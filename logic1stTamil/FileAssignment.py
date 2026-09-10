content=''
with open('D:\\Coding Practice\\PythonPractice\\logic1stTamil\\FileSystem.txt', 'r') as f:
    content = f.read()

replace1 = content.replace('cows', 'ducks')
replace2 = replace1.replace('moo', 'quack')

with open('D:\\Coding Practice\\PythonPractice\\logic1stTamil\\FileSystem.txt','a')as f1:
    f1.write(replace2)
