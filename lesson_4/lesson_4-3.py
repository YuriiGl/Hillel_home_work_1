number1=int(input('Введите число А: '))
number2=int(input('Введите число В: '))
if number1 < number2:
    ourlist = list(range(number1, number2 + 1))
    print(ourlist)
elif number1 > number2:
    newourlist=list(range(number2, number1))
    print(newourlist)
else:
    print('Некорректный ввод')



