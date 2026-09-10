with open('D:\Coding Practice\PythonPractice\files\file.txt') as f:
    content = f.read()
    print(content)

with open("D:\\Coding Practice\\PythonPractice\\files\\file.txt", 'a') as f:
    f.write("new content added")

with open("D:\\Coding Practice\\PythonPractice\\files\\file.txt",'w') as f:
    f.write("New write")