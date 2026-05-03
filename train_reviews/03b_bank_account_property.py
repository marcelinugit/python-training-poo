class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    # function = depositar
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self._balance += amount

    # function = retirar
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("withdraw must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient balance")
        self._balance -= amount

# where we test
account = BankAccount("Marcelinuu", 1000)
print(account.balance)

account.deposit(500)
print(account.balance)

account.withdraw(200)
print(account.balance)