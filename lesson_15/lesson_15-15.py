# # Во вложении файл csv с данными про аэропорты мира, написать программу которая сможет
# # вернуть данные по таким параметрам:
# # --iata_code - код аэропорта, должно вернуть 1 запись по коду аэропорта(всю строку) или вернуть ошибку AirportNotFoundError
# # --country - страна, должно вернуть все записи по аэропортам или
# # CountryNotFoundError
# # --name - значение имени аэропорта, допустимо вхождение строки хотябы
# # минимально, т.е. liman должен вернуть строки с такими названиями:
# # Ilimanaq Heliport
# # Sidi Slimane Airport
# # Kilimanjaro International Airport
# # West Kilimanjaro Airport
# # Limanske Airfield
# # Liman Airfield
# # или AirportNotFoundError
# # Только один параметр обязателен, если выбрано несколько - вернуть
# # ошибку:
# # MultipleOptionsError, если ни одного - NoOptionsFoundError
# # ** доп. ошибки принимают два аргумента, текст ошибки и входные данные,
# # пример:
# # AirportNotFoundError: ('Airport not found', 'OESD')
# # CountryNotFoundError: ('Country not found', 'UGUGU')
#
# import csv
#
# # filename = 'airport-codes_csv.csv'
# # with open(filename) as f:
# #     reader = csv.reader(f)
# #     header_row = next(reader)
# # print(header_row)
# class AirportFounder:
#     def __init__(self, arguments):
#         self.args = self.check_arguments(arguments)
#     def check_arguments(self, arguments):
#         my_args = ['iata_code', 'country', 'name']
#         if arguments in my_args:
#             return arguments
#         # доделать валидацию
#     def find(self):
#         filename = 'airport-codes_csv.csv'
#         with open(filename, encoding='utf-8') as f:
#             reader = csv.reader(f)
#             header_row = next(reader)
#             for index, column_header in enumerate(header_row):
#                 print(index, column_header)
#             iata_code_list,contry_list, name_list  = [], [], []
#             for row in reader:
#                 iata_code = str(row[9])
#                 contry = str(row[5])
#                 name = str(row[2])
#                 iata_code_list.append(iata_code)
#                 contry_list.append(contry)
#                 name_list.append(name)
#
# a1 = AirportFounder('name')
# a1.find()


import csv
import re
class AirportFounder:
    def __init__(self, arguments, value):
        self.args = self.check_arguments(arguments)
        self.value = value
    def check_arguments(self, arguments):
        my_args = ['iata_code', 'country', 'name']
        if arguments in my_args:
            return arguments
        # доделать валидацию
    def find(self):
        filename = 'airport-codes_csv.csv'
        with open(filename, encoding='utf-8') as f:
            reader = csv.reader(f)
            header_row = next(reader)
            target_column = -1
            for index, column_header in enumerate(header_row):
                if(column_header==self.args):
                    target_column = index
             #if(target_column==-1):
              #raise Error #кидаем ошибку что нет такой колонки
             #print('target index: ',target_column)
                #print(index, column_header)
            result = []

            for row in reader:
                if(row[target_column] == self.value):
                    result.append(row)
        for r in result:
            print(r)
#Lowell Field
a1 = AirportFounder('name','Lowell Field')
a1.find()