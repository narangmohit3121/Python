import datetime


class Account(object):
    def __init__(self, name, balance=0):
        self._transactions = []
        self.name = name
        if balance > 0:
            self._balance = balance
            self._transactions.append(f"{self.name} opened account with balance {balance} on {current_time()}")
        else:
            print("Can't open account with a negative balance")

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self._transactions.append(f"Deposited {amount} on {current_time()}")
            self.show_balance()
        else:
            print("The deposit amount should be greater than 0")

    def withdraw(self, amount):
        if 0 < amount < self._balance:
            self._balance -= amount
            self._transactions.append(f"Withdrew {amount} on {current_time()}")
            self.show_balance()
        else:
            print("Not enough balance")

    def show_balance(self):
        print(f"Current balance for {self.name} is {self._balance}")

    def show_transactions(self):
        print("Displaying transaction history for Amy")
        for transaction in self._transactions:
            print(transaction)


def current_time():
    return datetime.datetime.utcnow()


print(current_time())

amy = Account("Amy", 100)

amy.deposit(10)
amy.withdraw(20)
amy.withdraw(5)
amy.withdraw(2)
amy.deposit(5)
amy.show_balance()
amy.show_transactions()
