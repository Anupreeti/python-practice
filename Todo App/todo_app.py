# Add task

# View all tasks

# Mark as done

# Delete Task

# Store tasks in a .txt file
FILENAME = "tasks.txt"

def load_tasks():
    try:
        with open(FILENAME,"r", encoding="utf-8") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(FILENAME,"w", encoding="utf-8") as f:
        for task in tasks:
            f.write(task + "\n")


def add_task():
    entry = input("Enter your task: ")
    tasks.append(entry)
    save_tasks(tasks)
    print("Task Added!")

def view_tasks():
    if not tasks:
        print("No tasks yet!")
    print("Your Tasks!")
    for i, task in enumerate(tasks,1):
        print(f"{i}. {task}")

def mark_done():
    view_tasks()
    try:
        task_num = int(input("Enter the task number to be marked as Done: ")) -1
        if 0 <= task_num < len(tasks):
            if not tasks[task_num].startswith("✔"):
                tasks[task_num] = "✔" + tasks[task_num]
                save_tasks(tasks)
                print("Task marked as Done!")
            else:
                print("Task already marked as Done!")
        else:
            print("Invalid task number")
    except ValueError:
        print("Enter a Valid Number!")

def remove_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number you want to remove: "))-1
        if 0<=task_num <len(tasks):
            tasks.remove(tasks[task_num])
            save_tasks(tasks)
            print("Task is removed")
        else:
            print("Task is already removed!")
    except ValueError:
        print("Enter a valid number!")

tasks = load_tasks()
while True:
    print("Enter yout choice: \n")
    print("1.Add Task \n2.View Task \n3.Mard Task as Done \n4.Delete Task \n5.EXIT")
    choice = input("Choice: ")
    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        mark_done()
    elif choice == '4':
        remove_task()
    elif choice == '5':
        break
    else:
        print("Invalid choice!")
