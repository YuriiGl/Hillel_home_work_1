# # 1. Описать класс "Банковский счет", атрибуты у которого:
# #    имя аккаунта - str
# #    уникальный id (uuid)
# #    баланс float
# #    транзакции (список)
# #    Методы
# #     депозит средств
# #     вывод средств
# #     получить баланс
# # При изменении баланса записывать в транзакции (сумма, тип операции, текущая_дата)
# # * доп. добавить и учитывать банковские комиссии (1%)
#
# import uuid
#
# class Bank_account:
#     def __init__(self, name_account, uuid, balance, transactions):
#         self.name_account = name_account
#         self.uuid = uuid
#         self.balance = balance
#         self.transactions = transactions
#
#     def print_info(self):
#         print(f'name_account: {self.name_account}, uuid: {self.uuid}, balance:{self.balance},'
#               f' transactions: {self.transactions}')
#
#     def deposit(self, deposit):
#         return deposit  # предполагаем, что "депозит" в условии предполагает внесение
#                         # дополнительных средств на счет.
#
#     #withdrawal_of_funds, new_balance, curent_date
#
from datetime import datetime
import uuid

class BankAccount:

    def __init__ (self, name):
        """Инициализирует атрибуты."""
        self.name = name
        self.account_id = uuid.uuid4()
        self.balance = 0.0
        self.transactions = []

    def deposit_of_funds(self, amount):
        self.balance += amount
        self.transactions.append((amount, 'deposit', datetime.now))

    def withdrawal_of_funds(self, amount):
        self.transactions -= amount
        self.transactions.append((amount, 'deposit', datetime.now))

    def get_balance(self):
        return self.balance
client_1 = BankAccount('client_1')
client_1.deposit_of_funds(250)
print(client_1.get_balance())
client_1.withdrawal_of_funds(150)
print(client_1.get_balance())


