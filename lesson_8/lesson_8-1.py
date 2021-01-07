#Написать приложение "Онлайн конвертер валют". =)
#Приложение спрашивает пользователя:
#  currency_from: string (default USD)
#  currency_to: string (default UAH)
#Проверка ввода параметра валют (from, to) должна быть в symbols.json по ключу symbols)

#  amount: float (default 100.00)
#  start_date: string
#(пример. 2020-09-22 если дата не в этом формате, выставлять по-умолчанию дату текущего дня,
# если дата превышает текущий день, тоже выставляем дату текущего дня)
#Если дата меньше или равна текущему дню, то от start_date до текущего идет итерация:
#Приложение делает GET запрос:
#  https://api.exchangerate.host/convert
#  Принимаемые параметры from, to, amount, date
#  (from=USD&to=UAH&amount=10000.5&date=2020-09-18)
#Итоговый вывод должен быть точно в таком же формате (пример если start_date == 2020-09-18):
#[['date', 'from', 'to', 'amount', 'rate', 'result'],
#   ['2020-09-18', 'USD', 'UAH', 10000.5, 28.163466, 281648.743085],
#   ['2020-09-19', 'USD', 'UAH', 10000.5, 28.163466, 281648.737791],
#   ['2020-09-20', 'USD', 'UAH', 10000.5, 28.163455, 281648.630637],
#   ['2020-09-21', 'USD', 'UAH', 10000.5, 28.23733, 282387.419415],
#   ['2020-09-22', 'USD', 'UAH', 10000.5, 28.265772, 282671.854989]]

#** доп. задание. ввод данных должен приниматься парсингом аргументов, модуль
#      argparse.
#          Только --start_date опциональный параметр.
#          В итоге чтобы была возможность запустить приложение командой:
#          python exchange_rates.py USD UAH 100 --start_date 2020-09-18
#В данном случае пользователя спрашивать не нужно.

import datetime
import json
import argparse
import requests

#from pprint import pprint as

def symbols():
    with open('symbols.json', 'r', encoding="utf-8") as file:
        symbols_file = json.load(file)
    return symbols_file

def get_values(arguments):
    symbols_file = symbols()
    currency_from = arguments.currency_from
    if currency_from.upper() not in symbols_file['symbols']:
        print('Нет такой валюты!')
        currency_from = 'USD'
    currency_to = arguments.currency_to
    if currency_to.upper() not in symbols_file['symbols']:
        print('Нет такой валюты!')
        currency_to = 'UAH'
    try:
        amount = float(arguments.amount)
    except ValueError:
        amount = 100.00
        print('Неправильный ввод!')
    try:
        if arguments.start_date:
            start_date = datetime.datetime.strptime(arguments.start_date, '%Y-%m-%d' )
            if start_date > datetime.datetime.now():
                start_date = datetime.datetime.now()
        else:
            start_date = datetime.datetime.now()
    except ValueError:
        start_date = datetime.datetime.now()
        print(f'Некорректный ввод даты!')
    return convert(currency_from, currency_to, amount, start_date)

def convert(currency_from, currency_to, amount, start_date):
    result = [['date','from','to','amount','rate','result']]
    while start_date <= datetime.datetime.now():
        request = requests.get('https://api.exchangerate.host/convert',
                               params={'from': currency_from, 'to': currency_to, 'amount': amount, 'date': start_date})
        data = request.json()
        result.append([data['date'],
                       data['query']['from'],
                       data['query']['to'],
                       data['query']['amount'],
                       data['info']['rate'],
                       data['result']])
        start_date += datetime.timedelta(days=1)
    print(result)

parser = argparse.ArgumentParser(description='Exchenge rates')
parser.add_argument('currency_from')
parser.add_argument('currency_to')
parser.add_argument('amount')
parser.add_argument('--start_date')
arguments =  parser.parse_args()
get_values(arguments)