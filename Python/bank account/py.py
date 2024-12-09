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


# Create two accounts
account1 = BankAccount(0.02, 1000)
account2 = BankAccount(0.01, 500)

account1.deposit(500)
account1.deposit(300)
account1.deposit(200)
account1.withdraw(400)
account1.yield_interest()
account1.display_account_info()

account2.deposit(100)
account2.deposit(200)
account2.withdraw(100)
account2.withdraw(200)
account2.withdraw(50)
account2.withdraw(150)
account2.yield_interest()
account2.display_account_info()
