# 3. Написать функцию которая сдвинет полученный список на N элементов вправо или влево,
# принимаемые аргументы - список и натуральное число(если отрицательное сдвигаем влево, положительное - вправо).

# any_str = list(map(int, input('Введите строку: ').split()))
# shift_index = int(input('Введите натуральное число: '))
# #any_len = len(any_str)
# #new_str = []
# def new_str(any_str_1, ):
#     if shift_index < 0:
#         x = any_str[0]
#         del any_str[0]
#         any_str.append(x)
#
#     if shift_index > 0:
# #         any_str[]
#         any_str.pop(-1)
#      #new_str = any_str.rotate(shift_index)
#     return new_str()
# print(new_str)


list_of_nums = list(map(int, input('Введите: ').split()))
shift_num = int(input('Введите индекс сдвига: '))
def shift_numbers(shifted_nums, func_for_shift):
    shift_num = shifted_nums[-func_for_shift:] + shifted_nums[:-func_for_shift]
    return shifted_nums
print(shift_numbers(list_of_nums, shift_num))