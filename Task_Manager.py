#Task Manager 

print("Welcome to the Task Manager!")

tasks = []

while True:
    print("\nOptions:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit ")

    choice = input("Enter your choice (1-4): ")
    if choice == '1':
        task = input("Enter the task you want to add:")
        tasks.append(task)
        print(("Task added "))

    elif choice == '2':
        task = input("Enter the task you want to remove:")
        if task in tasks:
            tasks.remove(task)
            print(("Task removed "))

        else:
            print("Task not found!")

    elif choice == '3':
        if tasks:
            print("Your Tasks:")
            for idx, task in enumerate(tasks, start=1):
                print(f"{idx}. {task}")
            else:
                print("No tasks available.")
            
    elif choice == '4':
            print("Exiting Task Manager. Byeeeeee!")

            break