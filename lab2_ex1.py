flag = 1
tasks = []

while flag == 1:
    choice = input("\nInsert the number corresponding to the action you want to perform:\n\n1. insert a new task;\n2. remove a task;\n3. show all the tasks, sorted;\n4. close the program.\n\nYour choice: ")
    if choice == "1":
        newtask = input("Which task do you want to insert: ")
        tasks.append(newtask)
    elif choice == "2":
        remtask = input("Which task do you want to remove? ")
        tasks.remove(remtask)
    elif choice == "3":
        print(sorted(tasks))
    else:
        flag = 0
        print("Goodbye!")