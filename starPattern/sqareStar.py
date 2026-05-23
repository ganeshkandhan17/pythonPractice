userInput = input("Enter the number = ")

try :
    num = int(userInput)
    for i in range(num):
        for j in range(num):
            print("*",end =" ")
        print("\n")
except Exception as e :
    print(f"Error occurs in program {e}")