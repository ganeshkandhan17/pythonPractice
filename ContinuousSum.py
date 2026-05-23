sum = 0

while True:
    userInput = input(f"Enter number to sum (exit to stop) = ")    
    if userInput == "exit":
        print(f"Total Sum Value : {sum}")
        break

    try:
        sum+=int(userInput)
        print(f"Current Sum value : {sum}" )       
    except Exception as e:    
        print(f"Number in only allowed")
   
    

else :
    print("Loop ended")
