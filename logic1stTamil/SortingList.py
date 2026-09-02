list = [55,354,349,16498,31,98,567,963,98,2,9]

def swapPosition(index1, index2):
    temp = list[index1]
    list[index1] = list[index2]
    list[index2] = temp

for i in range(0, len(list)-1):
    for j in range(0, len(list)-1):
        if (list[j] > list[j+1]):
            swapPosition(j, j+1)

print(list)