class BankAccount:
    def __init__(self, account_number, customer_name, initial_balance=0.0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient balance")

account1 = BankAccount("123", "alice", 50.00)
account1.deposit(20)
account1.withdraw(10)
print(f"Final balance: {account1.balance}")
