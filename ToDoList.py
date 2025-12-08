import json
import os

TASKS_FILE = "todo_data.json"

# Load existing data
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []

# Save data
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def display_menu():
    print("\n=== TO-DO LIST MENU ===")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Mark Task Complete")
    print("5. Exit")

def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks yet. Start adding some.")
        return
    print("\nYour Tasks:")
    for idx, task in enumerate(tasks, start=1):
        status = "✅" if task["done"] else "❌"
        print(f"{idx}. {task['title']} [{status}]")

def add_task(tasks):
    title = input("Enter task: ").strip()
    if not title:
        print("Task cannot be empty.")
        return
    task = {"title": title, "done": False}
    tasks.append(task)
    save_tasks(tasks)
    print(f"✅ Added: {title}")

def remove_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Enter task number to remove: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"🗑️ Removed: {removed['title']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Enter a valid number.")

def mark_complete(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Enter task number to mark complete: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["done"] = True
            save_tasks(tasks)
            print("✅ Task marked complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Enter a valid number.")

def main():
    tasks = load_tasks()
    print("Welcome to Your To-Do List App!")
    while True:
        display_menu()
        choice = input("Choose (1–5): ").strip()
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            mark_complete(tasks)
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
