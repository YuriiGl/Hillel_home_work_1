num_a = float(input('Введите первый параметр:'))
num_b = float(input('Введите второй параметр:'))
forma = input('Если вы хотите найти площадь квадрата. введите уеs: ')
if forma =='yes' and num_a == num_b:
    print('Некоректный ввод!')
    s = num_a ** 2
else:
    s = num_a * num_b * 0.5
print(s)



