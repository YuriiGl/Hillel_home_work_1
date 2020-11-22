any_list=[2, 3, 5, 6, 87, 43, 24]
def nechet (any_list_arg):
    new_list = []
    my_count = 0
    for num in any_list_arg:
        if num % 2 != 0:
            my_count += 1
            new_list.append(0)
        else:
            new_list.append(num)
print(new_list, my_count)
def nechet_2 (any_list_arg_2):
    my_count = 0
    for index in range(len(any_list_arg_2)):
        num = any_list_arg_2[index]
        if num % 2 != 0:
            my_count = my_count + 1
            any_list_arg_2[index] = 0
    print(any_list_arg_2, my_count)
nechet_2(any_list)

nechet(any_list)
# print(len(any_list))
# print(range(len(any_list)))
# for i in range(len(any_list)):
#     print(i, any_list[i])
#     any_list[i]=0
# print(any_list)
