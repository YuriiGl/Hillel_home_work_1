# 2. Написать программу которая будет форматировать номер телефона к единому виду.
# На ввод программа принимает строку введенного номера телефона, например:
# 063-999-99-99 вывод (+38) 063 999-99-99
# 063 999-99-99 вывод (+38) 063 999-99-99
# 063-99999-99 вывод (+38) 063 999-99-99
# +3806399-999-99 вывод (+38) 063 999-99-99
# 380639999999 вывод (+38) 063 999-99-99
# Если что-то не так с номером - пишет 'Failed to recognize number'.

# import re
# any_num = input('Введите номер телефона: ')
# pattern = r'\b[(]?[+]?(?:38){0,1}[)]?[- ]?([\d]{3})[- ]?([\d]{3})[- ]?([\d]{2})[- ]?([\d]{2})\b'
# match = re.findall(pattern, any_num)
# try:
#  (d1, d2, d3, d4) = re.findall(pattern, any_num)[0]
#  print('(+38)' + ' ' + d1 + ' ' + d2 + '-' + d3 + '-' + d4)
# except IndexError:
#  print('Failed to recognize number')

import re

def format_phone(num):
    pattern = r'\b[(]?[+]?(?:38){0,1}[)]?[- ]?([\d]{3})[- ]?([\d]{3})[- ]?([\d]{2})[- ]?([\d]{2})\b'
    match = re.findall(pattern, num)
    try:
       (d1, d2, d3, d4) = re.findall(pattern, num)[0]
       return '(+38)' + ' ' + d1 + ' ' + d2 + '-' + d3 + '-' + d4
    except IndexError:
        return 'Failed to recognize number'

def main():
    any_num = input('Введите номер телефона: ')
    print(format_phone(any_num))


if '__name__'=='__main__':
    main()