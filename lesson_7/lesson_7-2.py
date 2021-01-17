any_temp = float(input('Введите температуру: '))
any_sist = str(input('Введите систему измерения температуры (C, K, F): '))
if any_sist == 'C':
    print(str(any_temp),'C   ', str(any_temp + 273.15),'K   ', str(any_temp * 1.8 + 32), 'F   ' )
elif any_sist == 'K':
    print(str(any_temp - 273.15), 'C   ', str(any_temp), 'K   ', str(any_temp * 1.8 - 459.67) + 'F   ')
elif any_sist == 'F':
    print(str((any_temp - 32)*1.8) + 'C   ', str((any_temp + 459.67)/1.8) + 'K   ', str(any_temp) + 'F   ')
else:
    print('Неправильный ввод!')

# Какая разница между запятой и "+" при конкатенации?

# В связи с тем, что проверять можно только функции, єто задание пришлось переделать с нуля. Представляю еще один вариант.

def temperature(sist, temp):
	if sist == 'C':
		return (temp, temp + 273.15, temp * 1.8 + 32)
	elif any_sist == 'K':
		return (temp - 273.15, temp, temp * 1.8 - 459.67)
	elif any_sist == 'F':
		return ((temp - 32)*1.8, (temp + 459.67)/1.8, temp)
	else:
		print('Неправильный ввод!')

def main():
	any_temp = float(input('Введите температуру: '))
	any_sist = str(input('Введите систему измерения температуры (C, K, F): '))

	(c, k, f) = temperature(any_sist, any_temp)
	print(str(c),'C   ', str(k),'K   ', str(f), 'F   ' )

if '__name__'=='__main__':
	main()