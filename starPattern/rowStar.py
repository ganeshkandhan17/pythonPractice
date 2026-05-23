try : 
    rows = int(input(f"Enter number of rows = "))
    for num in range(rows):
        print("*")
except Exception as e:
    print(f"Enter only numbers")
