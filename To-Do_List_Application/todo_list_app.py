# Initialize an empty to-do list
todo_list = []

# Function to add a new todo
def add_todo():
    todo_description = input("Enter the task: ")
    todo_list.append({"task": todo_description, "completed": False})
    print("Task added successfully.")

# Function to view remaining todos
def view_todos():
    print("Remaining Tasks:")
    for i, todo in enumerate(todo_list, start=1):
        task_status = "Completed" if todo["completed"] else "Not Completed"
        print(f"{i}. {todo['task']} ({task_status})")

# Function to mark a todo as completed
def complete_todo():
    view_todos()
    try:
        todo_index = int(input("Enter the number of the task you want to mark as completed: ")) - 1
        if 0 <= todo_index < len(todo_list):
            todo_list[todo_index]["completed"] = True
            print(f"Task '{todo_list[todo_index]['task']}' marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Function to remove a todo
def remove_todo():
    view_todos()
    try:
        todo_index = int(input("Enter the number of the task you want to remove: ")) - 1
        if 0 <= todo_index < len(todo_list):
            removed_task = todo_list.pop(todo_index)
            print(f"Task '{removed_task['task']}' removed successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Function to show statistics of todo
def show_statistics():
    total_tasks = len(todo_list)
    completed_tasks = sum(1 for todo in todo_list if todo["completed"])
    remaining_tasks = total_tasks - completed_tasks

    print(f"Total Tasks: {total_tasks}")
    print(f"Completed Tasks: {completed_tasks}")
    print(f"Remaining Tasks: {remaining_tasks}")

# Main menu
while True:
    print("\nTodo List Menu:")
    print("1. Add Todo")
    print("2. View Todos")
    print("3. Mark Todo as Completed")
    print("4. Remove Todo")
    print("5. Show Statistics")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_todo()
    elif choice == "2":
        view_todos()
    elif choice == "3":
        complete_todo()
    elif choice == "4":
        remove_todo()
    elif choice == "5":
        show_statistics()
    elif choice == "6":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
