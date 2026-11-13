# Add a new task
def add_task(tasks):
    new_task = input("Enter task: ").strip()
    if not new_task:
        print("Task must not be empty")
        return
    tasks.append({"name": new_task, "completed": False})
    print("Task added!")


# Display all tasks
def show_tasks(tasks):
    if not tasks:
        print("Your list is empty. Add a task first!")
    else:
        print("Your tasks:")
        for index, task in enumerate(tasks, start=1):
            if task["completed"]:
                print(f"{index}. {task['name']} ✓")
            else:
                print(f"{index}. {task['name']}")


# Delete a task
def delete_task(tasks):
    try:
        task_number = int(input("Enter task number: "))
        if not 1 <= task_number <= len(tasks):
            print("Invalid task number. Please try again.")
            return
        task_remove = tasks.pop(task_number - 1)
        print(f"'{task_remove['name']}' deleted.")

    except ValueError:
        print("You must enter a NUMBER")


# Mark a task as completed
def complete_task(tasks):
    try:
        task_number = int(input("Enter task number: "))
        if not 1 <= task_number <= len(tasks):
            print("Invalid task number. Please try again.")
            return
        task_number -= 1
        if not tasks[task_number]["completed"]:
            print(f"'{tasks[task_number]['name']}' marked as completed!")
            tasks[task_number]["completed"] = True
        else:
            print("This task is already completed!")

    except ValueError:
        print("You must enter a NUMBER")

# Undo task completion
def undo_task(tasks):
    try:
        task_number = int(input("Enter task number: "))
        if not 1 <= task_number <= len(tasks):
            print("Invalid task number. Please try again.")
            return
        task_number -= 1

        if tasks[task_number]["completed"]:
            print(f"'{tasks[task_number]['name']}' marked as uncompleted!")
            tasks[task_number]["completed"] = False
        else:
            print("This task is not completed yet!")

    except ValueError:
        print("You must enter a NUMBER")





tasks=[]

# Main program loop
while True:
    print("""===== TO-DO LIST =====
1. Add task
2. Show tasks
3. Delete task
4. Complete task
5. Undo task completion
6. Exit
    """)
    option = input("Choose an option:")

    if option=="1":
        add_task(tasks)

    elif option=="2":
        show_tasks(tasks)

    elif option=="3":
        delete_task(tasks)

    elif option=="4":
        complete_task(tasks)

    elif option=="5":
        undo_task(tasks)

    elif option=="6":
        print("Goodbye!")
        break
    else:
        print("Please choose a number between 1-6")

