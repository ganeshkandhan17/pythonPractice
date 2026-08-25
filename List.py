cities = ['erode', 'salem' , 'dharmapuri', 'krishnagiri' , '']

cities.append('hosur')

print(cities)

cities.append('bengaluru')

print(cities)

# Print all
print(cities[:])

# Print particular index
print(cities[2:])
print(cities[:3])

# Print step
print(cities[2::2])

# Print reverse
print(cities[::-1])

# pop
print(cities.pop(2))
print(cities)

# delete
del cities[1]
print(cities)

# Remove
cities.remove("")
print(cities)

# Sorting
print(sorted(cities))  # this will not change the original list
alpha = [10,9,22,3,5673,2243,2346,7]
alpha.sort() # this will change the original list
print(alpha)
