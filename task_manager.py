# Python Task Manager
# Features:
# 1. Add New Task
# 2. View All Tasks
# 3. Mark Task as Complete
# 4. Delete Task
# 5. Save and Load Tasks
# 6. Search Tasks

import uuid
import json
from datetime import datetime

class Task:
    def __init__(self, title, description, due_date, task_id=None, completed=False):
        self.id = task_id if task_id else str(uuid.uuid4())[:6]
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = completed

    def print_task(self):
        status = "✅ Completed" if self.completed else "📋 Pending"
        print(f"- ID: {self.id}\n  Title: {self.title}\n  Description: {self.description}\n  Due Date: {self.due_date}\n  Status: {status}\n")

    # Convert object to dictionary for saving to JSON file 
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "completed": self.completed
        }

    # Convert dictionary to object for loading from JSON file 
    @staticmethod
    def from_dict(data):
        return Task(
            title=data["title"],
            description=data["description"],
            due_date=data["due_date"],
            task_id=data["id"],
            completed=data["completed"]
        )


class TaskManager:
    FILE_NAME = "tasks.json"

    def __init__(self):
        self.tasks = []
        self.load_tasks()

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
        self.save_tasks()
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
                self.save_tasks()
                print("✅ Task marked as completed.")
                return
        print("❌ Task not found.")

    def delete_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                self.save_tasks()
                print("🗑️ Task deleted.")
                return
        print("❌ Task not found.")

    def save_tasks(self):
        data = [task.to_dict() for task in self.tasks]
        with open(self.FILE_NAME, "w") as f:
            json.dump(data, f, indent=4)

    def load_tasks(self):
        try:
            with open(self.FILE_NAME, "r") as f:
                data = json.load(f)
                self.tasks = [Task.from_dict(item) for item in data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.tasks = []
    
    def search_tasks(self, keyword=None, due_date=None):
        results = []
        if keyword:
            keyword = keyword.lower()
            results = [task for task in self.tasks if keyword in task.title.lower() or keyword in task.description.lower()]
        elif due_date:
            results = [task for task in self.tasks if task.due_date == due_date]
        else:
            print("❌ Please provide a keyword or due date to search.")
            return

        if results:
            print(f"\n🔍 Search Results ({len(results)} found):")
            for task in results:
                task.print_task()
        else:
            print("❌ No matching tasks found.")


def main():
    manager = TaskManager()

    while True:
        print("\n--------------------------------------------")
        print("📌 Menu")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Mark task as completed")
        print("4. Delete a task")
        print("5. Search tasks")
        print("6. Exit")

        choice = input("Select an option (1–6): ")

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
            print("\nSearch by:\n1. Keyword\n2. Due Date")
            search_choice = input("Select option (1 or 2): ")
            if search_choice == "1":
                keyword = input("Enter keyword: ")
                manager.search_tasks(keyword=keyword)
            elif search_choice == "2":
                due_date = input("Enter due date (YYYY-MM-DD): ")
                # Validate date format
                try:
                    datetime.strptime(due_date, "%Y-%m-%d")
                    manager.search_tasks(due_date=due_date)
                except ValueError:
                    print("❌ Invalid date format.")
            else:
                print("❌ Invalid choice.")

        elif choice == "6":
            print("🔚 Exiting program.")
            break

        else:
            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
