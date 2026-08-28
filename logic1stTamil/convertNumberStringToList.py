str="32,3,4,5,6,7"
numList=[]

split = str.split(",")

for s in split:
    numList.append(int(s))

print(numList)