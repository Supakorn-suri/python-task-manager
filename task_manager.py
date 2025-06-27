# Python Task Manager
# Features:
# 1. Add New Task
# 2. View All Tasks
# 3. Mark Task as Complete
# 4. Delete Task
# 5. Save and Load Tasks
# 6. Search Tasks

import uuid
from datetime import datetime

class Task:
    def __init__(self, title, description, due_date):
        self.id = str(uuid.uuid4())[:6]
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False

    def print_task(self):
        status = "✅ Completed" if self.completed else "📋 Pending"
        print(f"- ID: {self.id}\n  Title: {self.title}\n  Description: {self.description}\n  Due Date: {self.due_date}\n  Status: {status}\n")


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, due_date):
        if not title.strip():
            print("❌ Title cannot be empty.")
            return
        try:
            datetime.strptime(due_date, "%Y-%m-%d")
        except ValueError:
            print("❌ Invalid date format. Use YYYY-MM-DD.")
            return
        task = Task(title, description, due_date)
        self.tasks.append(task)
        print("✅ Task added successfully.")

    def view_tasks(self):
        print("\n📋 Pending Tasks:")
        for task in self.tasks:
            if not task.completed:
                task.print_task()

        print("\n✅ Completed Tasks:")
        for task in self.tasks:
            if task.completed:
                task.print_task()

    def mark_completed(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.completed = True
                print("✅ Task marked as completed.")
                return
        print("❌ Task not found.")

    def delete_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                print("🗑️ Task deleted.")
                return
        print("❌ Task not found.")


def main():
    manager = TaskManager()

    while True:
        print("\n--------------------------------------------")
        print("📌 Menu")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Mark task as completed")
        print("4. Delete a task")
        print("5. Exit")

        choice = input("Select an option (1–5): ")

        if choice == "1":
            title = input("Title: ")
            description = input("Description: ")
            due_date = input("Due date (YYYY-MM-DD): ")
            manager.add_task(title, description, due_date)

        elif choice == "2":
            manager.view_tasks()

        elif choice == "3":
            task_id = input("Enter task ID to mark as completed: ")
            manager.mark_completed(task_id)

        elif choice == "4":
            task_id = input("Enter task ID to delete: ")
            manager.delete_task(task_id)

        elif choice == "5":
            print("🔚 Exiting program.")
            break

        else:
            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
