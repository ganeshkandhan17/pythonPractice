start=True
todoList=[]

while start : 
    print('1. Add task')
    print('2. List all task')
    print('3. Exit')
    stage1 = input('Enter your choice (1 or 2) : ')
    if stage1 == "1":
        newTask = input('Enter task : ')
        todoList.append(newTask)
        print('Task added to the list.')
    elif stage1 == '2':
        for task in todoList:
            print(task)
    elif stage1 =='3':
        break