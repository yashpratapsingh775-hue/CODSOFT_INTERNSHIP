tasks = []


def show_tasks():
    if len(tasks) == 0:
        print("\nNo tasks found.")
        return

    print("\n===== YOUR TASKS =====")

    for i, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{i}. {task['title']} - {status}")


while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Complete Task")
    print("5. Delete Task")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Add a task
    if choice == "1":
        title = input("Enter task: ")

        task = {
            "title": title,
            "completed": False
        }

        tasks.append(task)
        print("Task added successfully!")

    # View tasks
    elif choice == "2":
        show_tasks()

    # Update a task
    elif choice == "3":
        show_tasks()

        if len(tasks) > 0:
            number = int(input("Enter task number to update: "))

            if 1 <= number <= len(tasks):
                new_title = input("Enter new task: ")
                tasks[number - 1]["title"] = new_title
                print("Task updated successfully!")
            else:
                print("Invalid task number.")

    # Complete a task
    elif choice == "4":
        show_tasks()

        if len(tasks) > 0:
            number = int(input("Enter task number to complete: "))

            if 1 <= number <= len(tasks):
                tasks[number - 1]["completed"] = True
                print("Task marked as completed!")
            else:
                print("Invalid task number.")

    # Delete a task
    elif choice == "5":
        show_tasks()

        if len(tasks) > 0:
            number = int(input("Enter task number to delete: "))

            if 1 <= number <= len(tasks):
                tasks.pop(number - 1)
                print("Task deleted successfully!")
            else:
                print("Invalid task number.")

    # Exit
    elif choice == "6":
        print("Thank you for using the To-Do List!")
        break

    else:
        print("Invalid choice. Please try again.")
