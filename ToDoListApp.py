todo_list = []

def add_task(task):
    todo_list.append(task)
    print("Task added: ", task)

def remove_task(task):
    todo_list.remove(task)
    print("Task removed: ", task)

def view_tasks():
    print("Current Tasks: ")
    for task in todo_list:
        print("- ", task)

print("Welcome to the To-Do Application!")
print("Enter 'add' to add a task.")
print("Enter 'remove' to remove a task.")
print("Enter 'view' to view all tasks.")
print("Enter 'exit' to exit the application.")

while True:
    user_input = input("What would you like to do? ")
    if user_input == 'exit':
        break
    elif user_input == 'add':
        task = input("Enter task: ")
        add_task(task)
    elif user_input == 'remove':
        task = input("Enter task to remove: ")
        remove_task(task)
    elif user_input == 'view':
        view_tasks()
    else:
        print("Invalid input. Please try again.")
