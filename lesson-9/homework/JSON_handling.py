
import json
import csv

def load_tasks(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def save_tasks(filename, tasks):
    with open(filename, 'w') as file:
        json.dump(tasks, file, indent=4)

def display_tasks(tasks):
    print("\nCurrent Tasks:")
    print("{:<5} {:<20} {:<10} {}".format("ID", "Task Name", "Completed", "Priority"))
    print("-" * 45)
    for task in tasks:
        print("{:<5} {:<20} {:<10} {}".format(
            task['id'],
            task['task'],
            str(task['completed']),
            task['priority']
        ))

def calculate_stats(tasks):
    total = len(tasks)
    completed = sum(1 for task in tasks if task['completed'])
    pending = total - completed
    avg_priority = sum(task['priority'] for task in tasks) / total if total > 0 else 0
    
    print("\nTask Statistics:")
    print(f"Total tasks: {total}")
    print(f"Completed tasks: {completed}")
    print(f"Pending tasks: {pending}")
    print(f"Average priority: {avg_priority:.1f}")

def json_to_csv(json_file, csv_file):
    tasks = load_tasks(json_file)
    
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'Task', 'Completed', 'Priority'])
        
        for task in tasks:
            writer.writerow([
                task['id'],
                task['task'],
                task['completed'],
                task['priority']
            ])

def main():
    tasks = load_tasks('tasks.json')

    display_tasks(tasks)

    calculate_stats(tasks)

    for task in tasks:
        if task['id'] == 1:
            task['completed'] = True

    save_tasks('tasks.json', tasks)
    print("\nTask 1 marked as completed and saved to tasks.json")

    json_to_csv('tasks.json', 'tasks.csv')
    print("Tasks converted to CSV format in tasks.csv")

if __name__ == "__main__":
    main()



















