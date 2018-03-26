from sys import argv

filename = argv[1]
txt = open(filename)

list = []

flag = 1

while flag == 1:
    task = txt.readline()
    if len(task) != 0:
        list.append(task)
    else :
        flag = 0

txt.close()

flag = 1

while flag == 1:

    choice = input("\nInsert the number corresponding to the action you want to perform:\n\n1. insert a new task;\n2. remove a task;\n3. show all the tasks, sorted;\n4. close the program.\n\nYour choice: ")
    if choice == "1":
        newtask = input("Which task do you want to insert: ")
        list.append(newtask + "\n")
    elif choice == "2":
        remtask = input("Which task do you want to remove? ")
        list.remove(remtask + "\n")
    elif choice == "3":
        print(sorted(list))
#       txt = open(filename)
#       print(txt.read())
#       txt.close()
    else:
        flag = 0
        print("Goodbye!")

    txt = open(filename, "w")
    for task in list:
        txt.write(task)
    txt.close()