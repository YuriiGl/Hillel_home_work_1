 # 1.Дано два кортежа, напишите функцию которая соединит их в один dict:
 # Input:
 # coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
 # code = ('BTC', 'ETH', 'XRP', 'LTC')
 # Output:
 #  {'Bitcoin': 'BTC', 'Ether': 'ETH', 'Ripple': 'XRP', 'Litecoin': 'LTC'}
#
#Вариант 1 решения задачи. Но без функции и поєтому тест проверяет только Вариант 2.
coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
code = ('BTC', 'ETH', 'XRP', 'LTC')

# new_dict = {}
# for i in code:
#     new_index = code.index(i)
#     i2 = coin[new_index]
#     new_dict[i2] = i
# print(new_dict)
#
#print(dict(zip(coin,code)))


def new_dict(*args):
    new_dict = {}
    for i in code:
        new_index = code.index(i)
        i2 = coin[new_index]
        new_dict[i2] = i
    return new_dict
print(new_dict())

