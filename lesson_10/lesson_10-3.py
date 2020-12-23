# 3. Написать функцию которая сдвинет полученный список на N элементов вправо или влево,
# принимаемые аргументы - список и натуральное число(если отрицательное сдвигаем влево, положительное - вправо).


list_of_nums = list(map(int, input('Введите: ').split()))
shift_num = int(input('Введите индекс сдвига: '))

def shift_numbers(shifted_nums, func_for_shift):
    shift_num = shifted_nums[-func_for_shift:] + shifted_nums[:-func_for_shift]
    return shifted_nums

print(shift_numbers(list_of_nums, shift_num))