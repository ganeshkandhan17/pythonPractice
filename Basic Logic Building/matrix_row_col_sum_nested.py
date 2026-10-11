# Sample Matrix (3 Rows × 3 Columns)

matrix = [
    [1, 2, 3],  # Row 1 → [1, 2, 3]
    [4, 5, 6],  # Row 2 → [4, 5, 6]
    [7, 8, 9],  # Row 3 → [7, 8, 9]
]

# Visual representation:
#
#       Column
#        0  1  2
#      ┌─────────┐
# Row 0│ 1  2  3 │
# Row 1│ 4  5  6 │
# Row 2│ 7  8  9 │
#      └─────────┘

for i in range(len(matrix)):
    sum = 0
    for j in range(len(matrix[i])):
        sum += matrix[i][j]
    print(f"sum of row {i+1} = {sum}")

columnSum = []
for i in range(len(matrix)):
    for j in range(0, len(matrix[i])):
        if i == 0:
            columnSum.append(matrix[i][j])
        else:
            columnSum[j] += matrix[i][j]

for i in range(len(columnSum)):
    print(f"sum of column {i+1} = {columnSum[i]}")

