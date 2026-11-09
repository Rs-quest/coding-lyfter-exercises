class BankAccount:

    def __init__(self, balance):
        self.balance = balance

def enter_amount (self, amount): 
    amount = print(float (input("Enter balance: ")))
    return amount   

def deposit_money (self, amount):       
    self.balance += amount
    return self.balance
    
def withdraw_money (self, amount):  
    if amount > self.balance:         
            raise ValueError("Error! Insufficient funds")  
    self.balance -= amount
    return self.balance

class SavingsAccount (BankAccount):

    def __init__(self, balance, min_balance):
        super().__init__(balance)
        self.min_balance = min_balance

    def withdraw_money(self, amount):
        if self.balance - amount < self.min_balance:
            raise ValueError("Cannot withdraw. Minimum balance required.")

        self.balance -= amount
        return self.balance
