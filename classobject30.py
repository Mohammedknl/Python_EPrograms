class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance!")

    def get_balance(self):
        return self.balance


# Create two BankAccount objects
account1 = BankAccount(1234567890, "Alice", 1000)
account2 = BankAccount(9876543210, "Bob", 500)

# Deposit some money into the accounts
account1.deposit(500)
account2.deposit(1000)

# Withdraw some money from the accounts
account1.withdraw(200)
account2.withdraw(700)

# Print the remaining balance in each account
print("Account number:", account1.account_number)
print("Account holder:", account1.account_holder)
print("Balance:", account1.get_balance())

print("Account number:", account2.account_number)
print("Account holder:", account2.account_holder)
print("Balance:", account2.get_balance())
