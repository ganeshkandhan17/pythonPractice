bioData = {'name' : 'Ganesh', 'age' : 22, 'state' : 'TN', 'country' : 'IN'}
print(bioData)

#add
bioData['dob'] ='17/03/2004'
print(bioData)

#access
print(bioData['age'])

#modify
bioData['state'] = 'Tamil Nadu'
print(bioData)

#delete
del bioData['age']
print(bioData)

# Iterate
for key,value in bioData.items():
    print(f"{key} : {value}")

for key in bioData.keys():
    print(key)

for value in bioData.values():
    print(value)

print((bioData.keys()))

# Dictionary in list
array=[]

array.append(bioData)
print(array[0]['name'])

people_food = [
    {"name": "Arjun", "favourite_food": "Biryani"},
    {"name": "Meera", "favourite_food": "Pasta"},
    {"name": "Ravi", "favourite_food": "Dosa"},
    {"name": "Sneha", "favourite_food": "Pizza"},
    {"name": "Karthik", "favourite_food": "Idli"},
    {"name": "Priya", "favourite_food": "Burger"},
    {"name": "Vikram", "favourite_food": "Fried Rice"},
    {"name": "Anjali", "favourite_food": "Paneer Butter Masala"},
    {"name": "Suresh", "favourite_food": "Sushi"},
    {"name": "Lakshmi", "favourite_food": "Chole Bhature"}
]

foodList =[]
for dic in people_food:
    print(dic)
    for key,value in dic.items():
        if key=='favourite_food':
            foodList.append(value)

print(sorted(foodList, reverse=True))
