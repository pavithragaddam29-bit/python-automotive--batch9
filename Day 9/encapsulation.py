class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # Private attribute
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}, New Balance: {self.__balance}")
        else:
            print("Invalid deposit amount")

    def get_balance(self):
        return self.__balance  # Accessor method

my_account = BankAccount("123456", 1000)
my_account.deposit(500)
print("Current Balance:", my_account.get_balance())
