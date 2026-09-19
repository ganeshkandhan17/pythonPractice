students = [("maths","Anitha",180),("biology","Anand",182),("biology","Balaji",170),("maths","Chandru",190)]

formattedStudents = list(map(lambda stud : (stud[1], stud[2], '{} %'.format((stud[2]/200)*100)), students))
print(formattedStudents)

val = [72,78,99,12,56]
result = list(map(lambda val: 'even' if val%2==0 else 'odd', val))
print(result)

temp = [102,99,89,70,103]
fTemp = list(map(lambda x: float('{:.2f}'.format((9/5)*x+32)), temp))
print(fTemp)