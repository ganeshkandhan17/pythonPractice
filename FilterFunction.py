items = [(3456,"shoe",780),(3566,"phone",25300),(2587,"book",450),(5412,"pen",75)]

#In the items list above, filter item numbers between 3000 and 4000
filter1 = list(filter(lambda item: item[0] >= 3000 and item[0] <=4000, items))
print(filter1)

students = [("maths","Anitha",180),("biology","Anand",182),("biology","Balaji",170),("maths","Chandru",190)]

# In students list, filter 1. Name starts with "A" . 2. Marks>=180
filter2 = list(filter(lambda stu: stu[1][0] == 'A' and stu[2] >=180, students) )
print(filter2)
