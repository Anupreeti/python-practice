# Create a command-line Python app that lets you:
# Add a task with title, description, and due date
# View all tasks
# Mark a task as completed
# Delete a task
# Save everything into a tasks.json file

import argparse
import json

def load_tasks():
    try:
        with open("tasks.json","r+") as f:
            return json.load(f)
    except Exception as e:
        return []

def save_tasks(tasks):
    with open("tasks.json","w") as f:
        json.dump(tasks, f , indent=2)

def add_task(task, description, date):
    tasks = load_tasks()
    task_id =tasks[-1]["id"] +1 if tasks else 1
    task_data = {"id":task_id, "title": task, "Description": description, "Due_Date": date,"completed": False}
    tasks.append(task_data)
    save_tasks(tasks)
    print("Task addedd")

def view_task():
    tasks = load_tasks()
    if not tasks:
        print("No Tasks")
        return
    for task in tasks:
        print(task)


def mark_completed(title):
    tasks = load_tasks()
    updated = False
    for task in tasks:
        if task["title"] == title:
            task["completed"] = True
            updated = True
            break
    if updated:
        save_tasks(tasks)
        print("Task has been marked as completed")
    else:
        print("Task not found")

def delete_task(title):
    tasks = load_tasks()
    tasks = [task for task in tasks if task["title"] != title]
    save_tasks(tasks)
    print("Task is deleted")

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Task Tracker")
    parser.add_argument("choice", choices=["1","2","3","4"], help="Choose: 1-Add, 2-View, 3-Mark Done, 4-Delete")
    parser.add_argument("--title", required = False, help="Task name")
    parser.add_argument("--description", required=False, help="Add Description for task")
    parser.add_argument("--duedate", required=False, help="The Due date for the task")

    args = parser.parse_args()

    if args.choice == "1":
        if args.title and args.description and args.duedate:
            add_task(args.title, args.description, args.duedate)
        else:
            print("Please provide --tile, --description and --duedate")
    elif args.choice =="2":
        view_task()
    elif args.choice == "3":
        if args.title:
            mark_completed(args.title)
        else:
            print("Please provide --title to mark as complete")
    elif args.choice == "4":
        if args.title:
            delete_task(args.title)
        else:
            print("Please provide --title to be deleted")
