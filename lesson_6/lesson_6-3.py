# 3. Дан список значений. Вернуть словарь где каждый ключ - это индекс листа,
#   а значение листа - это значение ключа:
#    Input:
# ['a', 'b', 'c', 'd', 'e']
#    Output
# {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e'}

new_list = ['a', 'b', 'c', 'd', 'e']
new_dict = {}
for element in new_list:
    new_index = new_list.index(element)
    new_dict[new_index] = element
print(new_dict)



index_list = range(len(new_list))         # По аналогии с задачей 6-1
print(dict(zip(index_list, new_list)))


