tasks = []

def show_menu():
    print("\n--- To-Do Menu ---")
    print("1. Add task")
    print("2. View / Update status")
    print("3. Delete task")
    print("4. Mark task as done")
    print("5. Exit")

def add_task():
    task_input = input("Enter task: ")
    tasks.append({"task": task_input, "done": False})
    print(f"Task added: {task_input}")

def view_tasks():
    if not tasks:
        print("No tasks available.")
        return
    print("\nYour tasks:")
    for index, task in enumerate(tasks, start=1):
        status = "[Done]" if task["done"] else "[Pending]"
        print(f"{index}. {task['task']} {status}")

def update_task_status():
    if not tasks:
        print("Koi task nathi update karva mate.")
        return

    print("\nTamara Tasks:")
    for index, item in enumerate(tasks, start=1):
        status = "[Done]" if item["done"] else "[Pending]"
        print(f"{index}. {item['task']} {status}")

    try:
        task_num = int(input("\nKaya number no task update karvo che? ")) - 1

        if 0 <= task_num < len(tasks):
            new_text = input("Navo task lakho: ")
            tasks[task_num]["task"] = new_text
            print(f"Task #{task_num + 1} update thai gyo!")
        else:
            print("Invalid number! Aa number no task nathi.")


    except ValueError:
        print("Krupa kari ne number lakho (letters nahi).")
  
def mark_task_done():
    view_tasks()
    if not tasks:
        return 
    try:
        index = int(input("Enter the task number to mark done: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            print("Task marked as done!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    if not tasks:
        print("No tasks to delete.")
        return
    try:
        index = int(input("Enter the task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            deleted_task = tasks.pop(index)
            print(f"Task deleted: {deleted_task['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

while True:
    show_menu()
    choice = input("Choose an option (1-5): ")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        mark_task_done()
    elif choice == "5":
        update_task_status()
    elif choice == "6":
        print("Exiting... Have a good day!")
        break
    else:
        print("Invalid option. Please choose 1 to 6.")
        