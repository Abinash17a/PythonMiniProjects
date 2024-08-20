# task_manager.py

import os
import json

def load_tasks():
   if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
   else:
        tasks = []
   return tasks

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

def add_task(tasks):
   description = input("Enter the task description: ")
   due_date = input("Enter the due date (optional): ")
   task = {
        "description": description,
        "due_date": due_date,
        "completed": False
    }
   tasks.append(task)
   print("Task added successfully!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    
    for i, task in enumerate(tasks, 1):
        status = "Completed" if task["completed"] else "Pending"
        due_date = task["due_date"] if task["due_date"] else "No due date"
        print(f"{i}. {task['description']} (Due: {due_date}) - {status}")

def mark_task_completed(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter the task number to mark as completed: "))
    
    if 1 <= task_num <= len(tasks):
        tasks[task_num - 1]["completed"] = True
        print("Task marked as completed!")
    else:
        print("Invalid task number!")

def delete_task(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter the task number to delete: "))
    
    if 1 <= task_num <= len(tasks):
        deleted_task = tasks.pop(task_num - 1)
        print(f"Deleted task: {deleted_task['description']}")
    else:
        print("Invalid task number!")

def main():
    tasks = load_tasks()
    while True:
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_completed(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
