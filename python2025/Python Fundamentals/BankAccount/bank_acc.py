class BankAccount:
    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self  

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self  

    def display_account_info(self):
        print(f"Balance: ${self.balance:.2f}")
        return self 

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self  

# First account: 3 deposits, 1 withdrawal, yield interest, display info
account1 = BankAccount(0.02, 1000)
account1.deposit(500).deposit(300).deposit(200).withdraw(400).yield_interest().display_account_info()

# Second account: 2 deposits, 4 withdrawals, yield interest, display info
account2 = BankAccount(0.01, 500)
account2.deposit(100).deposit(200).withdraw(100).withdraw(200).withdraw(50).withdraw(150).yield_interest().display_account_info()
