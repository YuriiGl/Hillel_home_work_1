import math

new_number=int(input('Введите целое не отрицательное число: '))
all_number=[new_number]
while new_number != 0:
    print('Введите еще одно число ')
    new_number=int(input())
    all_number.append(new_number)
    if new_number == 0:
        break
all_number_1 = all_number[:-1]1
print(len(all_number_1), sum(all_number_1), sum(all_number_1)/len(all_number_1), max(all_number_1))
