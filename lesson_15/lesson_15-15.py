# Во вложении файл csv с данными про аэропорты мира, написать программу которая сможет
# вернуть данные по таким параметрам:
# --iata_code - код аэропорта, должно вернуть 1 запись по коду аэропорта(всю строку) или вернуть ошибку AirportNotFoundError
# --country - страна, должно вернуть все записи по аэропортам или
# CountryNotFoundError
# --name - значение имени аэропорта, допустимо вхождение строки хотябы
# минимально, т.е. liman должен вернуть строки с такими названиями:
# Ilimanaq Heliport
# Sidi Slimane Airport
# Kilimanjaro International Airport
# West Kilimanjaro Airport
# Limanske Airfield
# Liman Airfield
# или AirportNotFoundError
# Только один параметр обязателен, если выбрано несколько - вернуть
# ошибку:
# MultipleOptionsError, если ни одного - NoOptionsFoundError
# ** доп. ошибки принимают два аргумента, текст ошибки и входные данные,
# пример:
# AirportNotFoundError: ('Airport not found', 'OESD')
# CountryNotFoundError: ('Country not found', 'UGUGU')
# IATA код может быть только 3х буквенным в верхнем регистре, сделать валидацию на него
# или вернуть IATACodeError

import argparse
import csv
import re

class AirportNotFoundError(Exception):
    pass

class MultipleOptionsError(Exception):
    pass

class NoOptionsFoundError(Exception):
    pass

class AirportFounder:
    def __init__(self, arguments):
        self.args = self.check_arguments(arguments)

    def check_arguments(self, arguments):
        args = [('name', arguments.name), ('country', arguments.country), ('iata_code', arguments.iata_code)]
        res = []
        for a in args:
            if a[1] is not None:
                res.append(a)

        if len(res) > 1:
            raise MultipleOptionsError
        elif len(res) == 0:
            raise NoOptionsFoundError
        else:
            return res

    def find(self):
        filename = 'airport-codes_csv.csv'
        with open(filename, encoding='utf-8') as f:
            reader = csv.reader(f)
            header_row = next(reader)
            target_column = -1
            for index, column_header in enumerate(header_row):
                if(column_header==self.args[0][0]):
                    target_column = index
            result = []
            pattern = rf"[\w\s]*{self.args[0][1]}[\w\s]*"

            for row in reader:
                if (re.fullmatch(pattern, row[target_column], flags=re.IGNORECASE)):
                    result.append(row)
        if len(result) == 0:
            raise AirportNotFoundError

        for r in result:
            print(r)

parser = argparse.ArgumentParser(description='World Airports')
parser.add_argument('--iata_code')
parser.add_argument('--country')
parser.add_argument('--name')
arguments =  parser.parse_args()
a1 = AirportFounder(arguments)
a1.find()