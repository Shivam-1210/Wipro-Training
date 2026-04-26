'''
class BankAccount:
    def __init__(self, account_number, account_holder_name, balance=0):

        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__balance = balance


    def get_account_number(self):
        return self.__account_number

    def get_account_holder_name(self):
        return self.__account_holder_name

    def get_balance(self):
        return self.__balance

    def set_account_holder_name(self, name):
        self.__account_holder_name = name

    def set_balance(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Withdraw amount must be positive.")
        else:
            self.__balance -= amount
            print(f"₹{amount} withdrawn successfully.")


    def display_info(self):
        print(f"Account Number: {self.__account_number}")
        print(f"Account Holder: {self.__account_holder_name}")
        print(f"Balance: ₹{self.__balance}")



# driver

account1 = BankAccount("12345", "Ram", 500)
account2 = BankAccount("67890", "Sita", 1000)

account1.display_info()
print()
account2.display_info()
print("\n--- Transactions ---\n")


account1.deposit(200)
account2.deposit(500)

account1.withdraw(100)
account2.withdraw(2000)  # Should show insufficient balance


print("\n--- Updated Account Info ---\n")
account1.display_info()
print()
account2.display_info()'''



class Employee:
    def __init__(self, employee_id, name, salary):
        # Private instance variables
        self.__employee_id = employee_id
        self.__name = name
        self.__salary = salary


    def get_employee_id(self):
        return self.__employee_id

    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__salary


    def set_name(self, name):
        self.__name = name

    def set_salary(self, salary):
        self.__salary = salary


    def display_info(self):
        print(f"Employee ID: {self.__employee_id}")
        print(f"Name: {self.__name}")
        print(f"Salary: ${self.__salary:.2f}")


    def give_salary_hike(self, percentage):
        if percentage > 0:
            increment = self.__salary * (percentage / 100)
            self.__salary += increment
            print(f"Salary increased by {percentage}% (${increment:.2f})")
        else:
            print("Percentage must be positive.")



# driver

emp1 = Employee(101, "Alice", 50000)
emp2 = Employee(102, "Bob", 60000)


print("--- Employee Information ---")
emp1.display_info()
print()
emp2.display_info()

print("\n--- Giving Salary Hikes ---")
emp1.give_salary_hike(10)
emp2.give_salary_hike(5)

print("\n--- Updated Employee Information ---")
emp1.display_info()
print()
emp2.display_info()