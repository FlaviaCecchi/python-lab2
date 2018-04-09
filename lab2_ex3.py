from sys import argv

filename = argv[1]
txt = open(filename)

list = []

flag = 1

while flag == 1:
    task = txt.readline()
    if len(task) != 0:
        list.append(task)
    else:
        flag = 0

txt.close()

substr = input("Insert the substring you want to remove: ")
for task in list:
    if substr in task:
        list.remove(task)

txt = open(filename, "w")
for task in list:
    txt.write(task)
txt.close()