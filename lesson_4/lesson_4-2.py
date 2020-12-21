import math
#
# new_number=int(input('Введите целое не отрицательное число: '))
# all_number=[new_number]
# while new_number != 0:
#     print('Введите еще одно число ')
#     new_number=int(input())
#     all_number.append(new_number)
#     if new_number == 0:
#         break
# all_number_1 = all_number[:-1]
# print(len(all_number_1), sum(all_number_1), sum(all_number_1)/len(all_number_1), max(all_number_1))
#2. Программа запрашивает ввод последовательности целых неотрицательных чисел, пока не будет введён 0.
# Как только будет введён 0 (ноль), программа должна посчитать и вывести на экран:
#- количество введённых чисел (завершающий 0 не считается)
#- их сумму
#- произведение
#- среднее арифметическое (не считая завершающего числа 0)
#- определить значение и порядковый номер наибольшего элемента последовательности.
# Если наибольших элементов несколько, выведите порядковый номер первого из них.
#- определить количество чётных и не чётных элементов в последовательности
#- определить значение второго по величине элемента в этой последовательности
#- определите, сколько элементов этой последовательности равны ее наибольшему элементу
new_number = None
all_number = []

while new_number != 0:
    print('Введите неотрицательное целое число: ')
    new_number = int(input())
    if new_number == 0:
        break
    all_number.append(new_number)

def make_calculation(all_number):
    digits_count = 0
    digits_sum = 0
    digits_multiply = 1
    digits_count_1 = 0
    digits_count_2 = 0
    max_digit = 0
    last_element = 0
    max_elements = 0
    max_digit_index = 0
    second_max_digit = 0
    second_max_index = 0
    for i, value in enumerate(all_number):
        digits_count += 1
        digits_sum += value
        digits_multiply *= value
        if value > max_digit:
            max_digit = value
            max_digit_index = 1
        if value < max_digit:
            second_max_digit = value
            second_max_index = 1
        if value % 2 == 0:
            digits_count_1 += 1
        if value + last_element == max_digit:
            max_elements += 1
        else:
            digits_count_2 += 1
        last_element = value
    digits_avg = digits_sum/digits_count
    return (digits_count, digits_sum, digits_multiply, digits_avg, max_digit,
            max_digit_index, second_max_digit, second_max_index, digits_count_1,
            digits_count_2, max_elements)

print(make_calculation (all_number))