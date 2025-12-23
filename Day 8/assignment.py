class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ₹{amount:.2f}. New balance: ₹{self.balance:.2f}")
        else:
            print("Error: Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            # Check minimum balance rule
            if self.balance <= 500:
                print(f"Error: Cannot withdraw. Balance (₹{self.balance:.2f}) is too low. Minimum balance required: ₹500")
            elif amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ₹{amount:.2f}. New balance: ₹{self.balance:.2f}")
            else:
                print(f"Error: Insufficient balance. Available: ₹{self.balance:.2f}, Requested: ₹{amount:.2f}")
        else:
            print("Error: Withdrawal amount must be positive.")
            #----------------------------2-------------------------#

    def display_balance(self):
        print(f"Account: {self.account_number}")
        print(f"Holder: {self.account_holder_name}")
        print(f"Balance: ₹{self.balance:.2f}")
        print("-" * 40)  # Account detail

if __name__ == "__main__":
    account = BankAccount("123456789", "Rakesh", 1000.00)
    print("=== Bank Account Management System ===")
    print("Account created!")
    account.display_balance()

    # menu for deposit/withdraw
    while True:
        print("\nOptions:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Display Balance")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            try:
                amount = float(input("Enter deposit amount: ₹"))
                account.deposit(amount)
            except ValueError:
                print("Error: Please enter a valid number for deposit amount!")
        elif choice == '2':
            try:
                amount = float(input("Enter withdrawal amount: ₹"))
                account.withdraw(amount)
            except ValueError:
                print("Error: Please enter a valid number for withdrawal amount!")
        elif choice == '3':
            account.display_balance()
        elif choice == '4':
            print("Thank you for using Bank Account System!")
            break
        else:
            print("Invalid choice. Please try again.")

