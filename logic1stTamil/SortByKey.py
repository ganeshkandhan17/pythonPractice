students = [("maths","Anitha",80),("biology","Anand",82),("biology","Balaji",70),("maths","Chandru",90)]

students.sort(key=lambda value : value[2])
print(students)

students.sort(key=lambda value : value[0])
print(students)

students.sort(key=lambda value : value[1])
print(students)

students.sort(key=lambda value : value[1], reverse=True)
print(students)