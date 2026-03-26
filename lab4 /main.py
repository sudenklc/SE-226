tasks = {}
execution_order = []
completed_tasks = set()

task_num = int(input("Enter number of tasks: "))

for i in range(task_num):
    task_name = input("Enter task name: ")
    dependency_num = int(input("How many dependencies for " + task_name + "? "))

    dependency_list = []

    for j in range(dependency_num):
        dependency_name = input("Enter dependency " + str(j + 1) + ": ")
        dependency_list.append(dependency_name)

    tasks[task_name] = dependency_list

print("TASK STRUCTURE:")
for task in tasks:
    print(task, "->", tasks[task])

print("INITIAL TASKS (with no dependencies):")

count = 0
for task in tasks:
    if tasks[task] == []:
        print(task)
        count = count + 1

if count == 0:
    print("None")

completed_count = 0

while completed_count != task_num:
    task_found_count = 0

    for task in tasks:
        if task not in completed_tasks:
            execute = 1

            for dependency in tasks[task]:
                if dependency not in completed_tasks:
                    execute = 0

            if execute == 1:
                execution_order.append(task)
                completed_tasks.add(task)
                completed_count = completed_count + 1
                task_found_count = task_found_count + 1

    if task_found_count == 0:
        break

print("EXECUTION ORDER:")

if execution_order == []:
    print("Cannot start tasks.")
else:
    step = 1
    for task in execution_order:
        print("Step", step, ":", task)
        step = step + 1

if completed_count == task_num:
    print("ALL TASKS COMPLETED SUCCESSFULLY")
else:
    print("ERROR: Circular dependency detected!")
    print("These tasks could not be completed:")
    for task in tasks:
        if task not in completed_tasks:
            print(task)
