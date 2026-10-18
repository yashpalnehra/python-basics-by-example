class InsufficientFunds(Exception):
    pass


class BankAccount:
    def __init__(self, owner, balance=0):
        if balance < 0:
            raise ValueError("opening balance cannot be negative")
        self.owner = owner
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        self._check_amount(amount)
        self.balance += amount
        self.history.append(("deposit", amount))

    def withdraw(self, amount):
        self._check_amount(amount)
        if amount > self.balance:
            raise InsufficientFunds(f"balance is {self.balance}, asked for {amount}")
        self.balance -= amount
        self.history.append(("withdraw", amount))

    def transfer(self, other, amount):
        self.withdraw(amount)
        other.deposit(amount)

    @staticmethod
    def _check_amount(amount):
        if amount <= 0:
            raise ValueError("amount must be positive")

    def __str__(self):
        return f"{self.owner}: {self.balance:.2f}"


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, rate=0.02):
        super().__init__(owner, balance)
        self.rate = rate

    def add_interest(self):
        interest = round(self.balance * self.rate, 2)
        # an empty account earns nothing, and deposit(0) would complain
        if interest:
            self.deposit(interest)
        return interest


if __name__ == "__main__":
    alice = BankAccount("Alice", 100)
    bob = SavingsAccount("Bob", 50)
    alice.transfer(bob, 30)
    bob.add_interest()
    print(alice)
    print(bob)
