class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            return "Invalid deposit"
        self.balance += amount
        return "Deposit successful"

    def withdraw(self, amount):
        if amount <= 0:
            return "Invalid withdraw"
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return "Withdraw successful"

    def show_balance(self):
        return f"Balance: {self.balance}"


b1 = BankAccount("Gustavo", 1000)

print(b1.deposit(500))
print(b1.withdraw(200))
print(b1.withdraw(5000))
print(b1.show_balance())
