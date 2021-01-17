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