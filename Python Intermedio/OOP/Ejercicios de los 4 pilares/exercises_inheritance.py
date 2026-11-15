
class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def deposit_money(self, amount):

        if amount <= 0:
            raise ValueError("Deposit amount must be positive")

        self.balance += amount
        return self.balance

    def withdraw_money(self, amount):

        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")

        if amount > self.balance:
            raise ValueError("Insufficient funds")

        self.balance -= amount
        return self.balance


class SavingsAccount(BankAccount):

    def __init__(self, balance, min_balance):
        super().__init__(balance)
        self.min_balance = min_balance

    def withdraw_money(self, amount):

        if self.balance - amount < self.min_balance:
            raise ValueError("Minimum balance requirement not met")

        return super().withdraw_money(amount)


# Testing BankAccount

account = BankAccount(1000)

print("Bank Account:")
print("Initial balance:", account.balance)

account.deposit_money(500)
print("After deposit:", account.balance)

account.withdraw_money(200)
print("After withdrawal:", account.balance)


# Testing SavingsAccount

savings = SavingsAccount(1000, 200)

print("\nSavings Account:")
print("Initial balance:", savings.balance)

savings.deposit_money(500)
print("After deposit:", savings.balance)

savings.withdraw_money(300)
print("After withdrawal:", savings.balance)

# Testing minimum balance restriction

try:
    savings.withdraw_money(1001)
except ValueError as error:
    print("Error:", error)

# Testing negative amounts

try:
    savings.deposit_money(-500)
except ValueError as error:
    print("Error:", error)

try:
    savings.withdraw_money(-500)
except ValueError as error:
    print("Error:", error)

