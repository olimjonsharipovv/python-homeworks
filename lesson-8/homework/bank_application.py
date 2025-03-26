
import json
import os
from uuid import uuid4

class Account:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False
    
    def __str__(self):
        return f"Account {self.account_number}\nOwner: {self.name}\nBalance: ${self.balance:.2f}"

class Bank:
    def __init__(self):
        self.accounts = {}
        self.load_from_file()
    
    def create_account(self, name, initial_deposit):
        account_number = str(uuid4())[:8]  
        new_account = Account(account_number, name, initial_deposit)
        self.accounts[account_number] = new_account
        self.save_to_file()
        return account_number
    
    def view_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            print(account)
        else:
            print("Account not found!")
    
    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account and account.deposit(amount):
            self.save_to_file()
            print(f"Deposited ${amount:.2f}. New balance: ${account.balance:.2f}")
        else:
            print("Invalid deposit amount or account not found!")
    
    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account and account.withdraw(amount):
            self.save_to_file()
            print(f"Withdrew ${amount:.2f}. New balance: ${account.balance:.2f}")
        else:
            print("Insufficient funds or invalid amount!")
    
    def save_to_file(self):
        accounts_data = {
            num: {"name": acc.name, "balance": acc.balance}
            for num, acc in self.accounts.items()
        }
        with open("accounts.json", "w") as f:
            json.dump(accounts_data, f)
    
    def load_from_file(self):
        if os.path.exists("accounts.json"):
            with open("accounts.json", "r") as f:
                accounts_data = json.load(f)
                for num, data in accounts_data.items():
                    self.accounts[num] = Account(num, data["name"], data["balance"])

def main_menu():
    bank = Bank()
    while True:
        print("\nBank Application")
        print("1. Create Account")
        print("2. View Account")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            name = input("Enter your name: ")
            deposit = float(input("Initial deposit amount: $"))
            acc_num = bank.create_account(name, deposit)
            print(f"Account created! Your account number is: {acc_num}")
        elif choice == "2":
            acc_num = input("Enter account number: ")
            bank.view_account(acc_num)
        elif choice == "3":
            acc_num = input("Enter account number: ")
            amount = float(input("Deposit amount: $"))
            bank.deposit(acc_num, amount)
        elif choice == "4":
            acc_num = input("Enter account number: ")
            amount = float(input("Withdrawal amount: $"))
            bank.withdraw(acc_num, amount)
        elif choice == "5":
            print("Thank you for banking with us!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()

























