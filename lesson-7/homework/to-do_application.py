
import os
import abc
import csv
import json
from typing import List, Dict

# Task class to represent individual tasks
class Task:
    def __init__(self, task_id: int, title: str, description: str, due_date: str = "", status: str = "Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def __str__(self):
        return f"{self.task_id}, {self.title}, {self.description}, {self.due_date}, {self.status}"

# Abstract base class for file storage
class FileStorage(abc.ABC):
    @abc.abstractmethod
    def save_tasks(self, tasks: List[Task], file_path: str):
        pass

    @abc.abstractmethod
    def load_tasks(self, file_path: str) -> List[Task]:
        pass

# CSV storage implementation
class CSVStorage(FileStorage):
    def save_tasks(self, tasks: List[Task], file_path: str):
        with open(file_path, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Task ID", "Title", "Description", "Due Date", "Status"])
            for task in tasks:
                writer.writerow([task.task_id, task.title, task.description, task.due_date, task.status])

    def load_tasks(self, file_path: str) -> List[Task]:
        tasks = []
        if os.path.exists(file_path):
            with open(file_path, mode="r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    tasks.append(Task(
                        task_id=int(row["Task ID"]),
                        title=row["Title"],
                        description=row["Description"],
                        due_date=row["Due Date"],
                        status=row["Status"]
                    ))
        return tasks

# JSON storage implementation
class JSONStorage(FileStorage):
    def save_tasks(self, tasks: List[Task], file_path: str):
        task_list = []
        for task in tasks:
            task_list.append({
                "task_id": task.task_id,
                "title": task.title,
                "description": task.description,
                "due_date": task.due_date,
                "status": task.status
            })
        with open(file_path, mode="w") as file:
            json.dump(task_list, file, indent=4)

    def load_tasks(self, file_path: str) -> List[Task]:
        tasks = []
        if os.path.exists(file_path):
            with open(file_path, mode="r") as file:
                task_list = json.load(file)
                for task_data in task_list:
                    tasks.append(Task(
                        task_id=task_data["task_id"],
                        title=task_data["title"],
                        description=task_data["description"],
                        due_date=task_data["due_date"],
                        status=task_data["status"]
                    ))
        return tasks

# To-Do application class
class ToDoApp:
    def __init__(self, storage: FileStorage, file_path: str):
        self.storage = storage
        self.file_path = file_path
        self.tasks = self.storage.load_tasks(self.file_path)

    def add_task(self):
        print("\nAdd a New Task")
        task_id = int(input("Enter Task ID: "))
        title = input("Enter Title: ")
        description = input("Enter Description: ")
        due_date = input("Enter Due Date (YYYY-MM-DD, optional): ")
        status = input("Enter Status (Pending/In Progress/Completed): ")
        self.tasks.append(Task(task_id, title, description, due_date, status))
        print("Task added successfully!")

    def view_tasks(self):
        print("\nTasks:")
        for task in self.tasks:
            print(task)

    def update_task(self):
        task_id = int(input("\nEnter Task ID to update: "))
        for task in self.tasks:
            if task.task_id == task_id:
                task.title = input("Enter new Title: ")
                task.description = input("Enter new Description: ")
                task.due_date = input("Enter new Due Date (YYYY-MM-DD, optional): ")
                task.status = input("Enter new Status (Pending/In Progress/Completed): ")
                print("Task updated successfully!")
                return
        print("Task not found.")

    def delete_task(self):
        task_id = int(input("\nEnter Task ID to delete: "))
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                print("Task deleted successfully!")
                return
        print("Task not found.")

    def filter_tasks(self):
        status = input("\nEnter status to filter (Pending/In Progress/Completed): ")
        filtered_tasks = [task for task in self.tasks if task.status.lower() == status.lower()]
        if filtered_tasks:
            print(f"\nTasks with status '{status}':")
            for task in filtered_tasks:
                print(task)
        else:
            print(f"No tasks found with status '{status}'.")

    def save_tasks(self):
        self.storage.save_tasks(self.tasks, self.file_path)
        print("Tasks saved successfully!")

    def load_tasks(self):
        self.tasks = self.storage.load_tasks(self.file_path)
        print("Tasks loaded successfully!")

    def main_menu(self):
        while True:
            print("\nWelcome to the To-Do Application!")
            print("1. Add a new task")
            print("2. View all tasks")
            print("3. Update a task")
            print("4. Delete a task")
            print("5. Filter tasks by status")
            print("6. Save tasks")
            print("7. Load tasks")
            print("8. Exit")
            
            choice = input("Enter your choice (1-8): ")
            
            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.update_task()
            elif choice == "4":
                self.delete_task()
            elif choice == "5":
                self.filter_tasks()
            elif choice == "6":
                self.save_tasks()
            elif choice == "7":
                self.load_tasks()
            elif choice == "8":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    # Choose storage format (CSV or JSON)
    storage_format = input("Choose storage format (csv/json): ").lower()
    file_path = "tasks.csv" if storage_format == "csv" else "tasks.json"
    
    if storage_format == "csv":
        storage = CSVStorage()
    elif storage_format == "json":
        storage = JSONStorage()
    else:
        print("Invalid storage format. Defaulting to CSV.")
        storage = CSVStorage()
        file_path = "tasks.csv"
    
    app = ToDoApp(storage, file_path)
    app.main_menu()


























































