# 1. Написать функцию `is_prime`, принимающую 1 аргумент — число от 0 до 1000, и возвращающую `True`,
# если оно простое, и `False` - иначе. (Простые числа - те которые делятся без остатка только на само себя или 1,
# например 2, 3, 5, 7, 11...)
any_num = int(input('Введите число от 0 до 1000:  '))
def is_prime(arg_1):
    for i in range(2, arg_1, 1):
        if arg_1 % i == 0:
            return False
    return True
new_result = is_prime(any_num)
print(new_result)

