import os

# File name for storing employee records
EMPLOYEE_FILE = "employees.txt"

class Employee:
    def __init__(self, employee_id, name, position, salary):
        """
        Initialize an Employee object.
        """
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        """
        Return a string representation of the Employee object.
        """
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"

class EmployeeManager:
    def __init__(self):
        """
        Initialize the EmployeeManager and ensure the file exists.
        """
        if not os.path.exists(EMPLOYEE_FILE):
            with open(EMPLOYEE_FILE, "w") as file:
                file.write("Employee ID,Name,Position,Salary\n")

    def add_employee(self):
        """
        Add a new employee record to the file.
        """
        print("\nAdd New Employee Record")
        employee_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        position = input("Enter Position: ")
        salary = input("Enter Salary: ")
        
        # Create an Employee object
        employee = Employee(employee_id, name, position, salary)
        
        # Append the new record to the file
        with open(EMPLOYEE_FILE, "a") as file:
            file.write(f"{employee}\n")
        print("Employee added successfully!")

    def view_all_employees(self):
        """
        Display all employee records from the file.
        """
        print("\nEmployee Records:")
        with open(EMPLOYEE_FILE, "r") as file:
            lines = file.readlines()
            if len(lines) <= 1:
                print("No employee records found.")
                return
            for line in lines[1:]:  # Skip the header line
                print(line.strip())

    def search_employee(self):
        """
        Search for an employee by Employee ID and display their details.
        """
        employee_id = input("\nEnter Employee ID to search: ")
        with open(EMPLOYEE_FILE, "r") as file:
            lines = file.readlines()
            found = False
            for line in lines[1:]:  # Skip the header line
                if line.startswith(employee_id + ","):
                    print("\nEmployee Found:")
                    print(line.strip())
                    found = True
                    break
            if not found:
                print("Employee not found.")

    def update_employee(self):
        """
        Update an employee's information based on Employee ID.
        """
        employee_id = input("\nEnter Employee ID to update: ")
        updated = False
        with open(EMPLOYEE_FILE, "r") as file:
            lines = file.readlines()
        
        with open(EMPLOYEE_FILE, "w") as file:
            for line in lines:
                if line.startswith(employee_id + ","):
                    print("\nCurrent Employee Details:")
                    print(line.strip())
                    name = input("Enter new Name: ")
                    position = input("Enter new Position: ")
                    salary = input("Enter new Salary: ")
                    updated_employee = Employee(employee_id, name, position, salary)
                    file.write(f"{updated_employee}\n")
                    updated = True
                    print("Employee record updated successfully!")
                else:
                    file.write(line)
            if not updated:
                print("Employee not found.")

    def delete_employee(self):
        """
        Delete an employee's record based on Employee ID.
        """
        employee_id = input("\nEnter Employee ID to delete: ")
        deleted = False
        with open(EMPLOYEE_FILE, "r") as file:
            lines = file.readlines()
        
        with open(EMPLOYEE_FILE, "w") as file:
            for line in lines:
                if not line.startswith(employee_id + ","):
                    file.write(line)
                else:
                    deleted = True
            if deleted:
                print("Employee record deleted successfully!")
            else:
                print("Employee not found.")

    def main_menu(self):
        """
        Display the main menu and handle user input.
        """
        while True:
            print("\nWelcome to the Employee Records Manager!")
            print("1. Add new employee record")
            print("2. View all employee records")
            print("3. Search for an employee by Employee ID")
            print("4. Update an employee's information")
            print("5. Delete an employee record")
            print("6. Exit")
            
            choice = input("Enter your choice (1-6): ")
            
            if choice == "1":
                self.add_employee()
            elif choice == "2":
                self.view_all_employees()
            elif choice == "3":
                self.search_employee()
            elif choice == "4":
                self.update_employee()
            elif choice == "5":
                self.delete_employee()
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    manager = EmployeeManager()
    manager.main_menu()






























