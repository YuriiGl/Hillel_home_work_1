 # 1.Дано два кортежа, напишите функцию которая соединит их в один dict:
 # Input:
 # coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
 # code = ('BTC', 'ETH', 'XRP', 'LTC')
 # Output:
 #  {'Bitcoin': 'BTC', 'Ether': 'ETH', 'Ripple': 'XRP', 'Litecoin': 'LTC'}

coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
code = ('BTC', 'ETH', 'XRP', 'LTC')
new_dict = {}
for i in code:
    new_index = code.index(i)
    i2 = coin[new_index]
    new_dict[i2] = i
print(new_dict)



print(dict(zip(coin,code)))    # сам в шоке, как получилось. но вариантов перед этим было 14 или 16

