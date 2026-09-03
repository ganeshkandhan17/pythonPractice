matrix_a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Matrix B
matrix_b = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

matrix_c=[]


for i in range(len(matrix_a)):
    newList = []
    for j in range(len(matrix_a[i])):           
            value = matrix_a[i][j] * matrix_b[i][j]            
            newList.append(value)        
    matrix_c.append(newList)    

print(matrix_c)
