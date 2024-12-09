class BankAccount:
    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.balance -= 5
        else:
            print("Insufficient funds")

    def display_account_info(self):
        print(f"Balance: ${self.balance:.2f}")

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        print(f"User: {self.name}")
        self.account.display_account_info()
        return self


# Example Usage:

# Create users
user1 = User("raed", "raed@example.com")
user2 = User("fatma", "fatma@example.com")

# Perform operations
user1.make_deposit(500).make_deposit(200).make_withdrawal(100).display_user_balance()
user2.make_deposit(1000).make_withdrawal(200).display_user_balance()
