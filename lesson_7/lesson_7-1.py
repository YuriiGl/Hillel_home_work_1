def to_list(func):
    print(func().split(' '))
@to_list
def user_input():
    user_str = str(input('Введите строку: '))
    return user_str

# Запутался.  Где вызывается функция user_input??? Декоратором???


