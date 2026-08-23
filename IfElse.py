age = 18
if age >= 18:
    print("Your are an adult")
else:
    print("Your a minor") 

indiaScore = int(input("current score of indian team : "))
if indiaScore >= 250: 
    print("india will win")
elif indiaScore >= 200 and indiaScore < 250 : 
    print("india can win")
elif indiaScore < 200  and indiaScore >= 150 : 
    print("india might win")
elif indiaScore <= 100:
    print("india will lose")
else :
    print("prediction is  waste of time")
