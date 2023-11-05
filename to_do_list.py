# creating an empty list to store tasks
tasks = []
# this function is used to display the tasks in the to do list.
def display():
    if not tasks:
        print("No tasks in the to-do list.")
    else:
        print("Your to-do list:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
# this function is used to add task to the to do list.
def add(task):
    tasks.append(task)
    print(f"Task '{task}' added.")
# this function is used to remove task from the to do list.
def remove():
    display()
    if tasks:
        task_number = int(input("Enter the task number to remove: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"Task '{removed_task}' removed.")
        else:
            print("Invalid task number.")
    else:
        print("No tasks in the to-do list.")
# creating options and calling other functions
def main():
    while True:
        print("\nSelect an option:")
        print("1. Show tasks")
        print("2. Add a task")
        print("3. Remove a task")
        print("4. Exit")
        choice = input("Enter your choie (1-4): ")
        # choice 1 is used to display the tasks in the to do list
        if choice == "1":
            display()
        # choice 2 is used to ask the user to enter a task and add it to the list    
        elif choice == "2":
            task = input("Enter the task to add: ")
            add(task)
        # choice 3 is used to remove a task from the to do list  
        elif choice == "3":c
            remove()
        # choice 4 is used to exit the program
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Enter a number between 1 and 4.")
# calling the main function
main()
