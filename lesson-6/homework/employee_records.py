

import os

EMPLOYEE_FILE = "employees.txt"

if not os.path.exists(EMPLOYEE_FILE):
    with open(EMPLOYEE_FILE, "w") as file:
        file.write("Employee ID,Name,Position,Salary\n")

def add_employee():
   
    print("\nAdd New Employee Record")
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    position = input("Enter Position: ")
    salary = input("Enter Salary: ")
    
    with open(EMPLOYEE_FILE, "a") as file:
        file.write(f"{emp_id},{name},{position},{salary}\n")
    print("Employee record added successfully!")

def view_all_employees():
   
    print("\nAll Employee Records")
    with open(EMPLOYEE_FILE, "r") as file:
        lines = file.readlines()
        if len(lines) <= 1:
            print("No employee records found.")
            return
        for line in lines[1:]:  
            print(line.strip())

def search_employee():
    
    emp_id = input("\nEnter Employee ID to search: ")
    with open(EMPLOYEE_FILE, "r") as file:
        lines = file.readlines()
        found = False
        for line in lines[1:]:  
            if line.startswith(emp_id + ","):
                print("\nEmployee Details:")
                print(line.strip())
                found = True
                break
        if not found:
            print("Employee not found.")

def update_employee():
   
    emp_id = input("\nEnter Employee ID to update: ")
    updated = False
    with open(EMPLOYEE_FILE, "r") as file:
        lines = file.readlines()
    
    with open(EMPLOYEE_FILE, "w") as file:
        for line in lines:
            if line.startswith(emp_id + ","):
                print("\nCurrent Employee Details:")
                print(line.strip())
                name = input("Enter new Name: ")
                position = input("Enter new Position: ")
                salary = input("Enter new Salary: ")
                file.write(f"{emp_id},{name},{position},{salary}\n")
                updated = True
                print("Employee record updated successfully!")
            else:
                file.write(line)
        if not updated:
            print("Employee not found.")

def delete_employee():
    
    emp_id = input("\nEnter Employee ID to delete: ")
    deleted = False
    with open(EMPLOYEE_FILE, "r") as file:
        lines = file.readlines()
    
    with open(EMPLOYEE_FILE, "w") as file:
        for line in lines:
            if not line.startswith(emp_id + ","):
                file.write(line)
            else:
                deleted = True
        if deleted:
            print("Employee record deleted successfully!")
        else:
            print("Employee not found.")

def main_menu():
   
    while True:
        print("\nEmployee Management System")
        print("1. Add new employee record")
        print("2. View all employee records")
        print("3. Search for an employee by Employee ID")
        print("4. Update an employee's information")
        print("5. Delete an employee record")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            add_employee()
        elif choice == "2":
            view_all_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            update_employee()
        elif choice == "5":
            delete_employee()
        elif choice == "6":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    