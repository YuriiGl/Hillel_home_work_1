# 3. Вводимый пользователем пароль должен соответсвовать требованиям,
# 	1. Как минимум 1 символ от a-z
# 	2. Как минимум 1 символ от A-Z
# 	3. Как минимум 1 символ от 0-9
# 	4. Как минимум 1 символ из $#@-+=
# 	5. Минимальная длина пароля 8 символов.
# Программа принимает на ввод строку, в случае если пароль не верный -
# пишет какому требованию не соответствует и спрашивает снова,
#  в случае если верный - пишет 'Password is correct'.

# passw = dfg2847gGHJKF6
# def valid_passw(passw):
#     if len(passw) >= 8:
#         return True
#     else:
#         return False
#Вариант 1, не доделан. Поскольку тема:"Регулярные выражения", второй вариант сделан по теме.
# def check_passw(passw):
#     for lit in passw:
#         lowwers = False
#         uppers = False
#         digits = False
#         if lit.islower():
#             lowwers = True
#         if lit.isupper():
#             uppers = True
#         if lit.isdigit():
#             digits = True
#         return  lowwers and uppers and digits

import re
any_str = input('Введите пароль: ')
pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@+=-])[a-zA-Z0-9$#@+=-]{8,}$'
match = re.fullmatch(pattern, any_str)
print('Password is correct' if match else 'the password was entered incorrectly')
