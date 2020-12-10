import datetime
import uuid

class BankAccount:

    def __init__(self, name):
        self.name = name
        self.account_id = uuid.uuid4()
        self.balance = 0.0
        self.transactions = []

    def deposit_of_funds(self, amount):
        self.balance += amount - amount * 0.01
        self.transactions.append((amount, 'deposit', datetime.datetime.today().strftime('%d %m %Y')))

    def withdrawal_of_funds(self, amount):
        self.balance -= amount - amount * 0.01
        self.transactions.append((amount, 'withdrawal', datetime.datetime.today().strftime('%d %m %Y')))

    def get_balance(self):
        return self.balance

