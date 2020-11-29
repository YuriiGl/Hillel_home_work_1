# Написать функцию которая вернет строку введенную пользователем.
# Обернуть функцию в декоратор чтобы функция вместо строки целиком вернула список слов.

def to_list(any_str):
    return any_str.split(' ')

def user_input():
    user_str = str(input('Введите строку: '))
    return user_str

print(to_list(user_input()))
