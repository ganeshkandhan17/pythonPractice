userInput = input("Enter the number = ")

try :
    num = int(userInput)
    for i in range(num):
        for j in range(num):
            if i>=j:
                print("*", end=" ")       
        print("\n")
except Exception as e :
    print("Only number is allowed")

