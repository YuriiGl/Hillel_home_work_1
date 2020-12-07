any_str = input('Введите любую строку: ')
any_str_2 = any_str.split()
result_str = ''
max_len = len(any_str_2[0])
for i in any_str_2:
    sam_num = len(i)
    if max_len < sam_num:
        max_len = sam_num
        result_str = i
print(result_str)