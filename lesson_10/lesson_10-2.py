# 2. Написать функцию которая определит является ли введенная строка палиндромом
# (та которая читается одинаково с любой стороны), пример:
# ШАЛАШ, КАЗАК, ДЕД, ДОХОД, 13231 и т.д.

any_word = str(input('Введите любое слово: '))
new_word = any_word[::-1]
if any_word == new_word:
  print('Это слово палиндром.')
else:
  print('Это слово не является палиндромом.')


any_word = str(input('Введите любое слово: '))
len_word = len(any_word)
i = 0
len_word = len_word - 1
k = 0
while len_word - i >= i:
    if any_word[len_word - i] == any_word[i]:
        i += 1
    else:
        k = 1
        break
if k == 1:
  print('Это слово не является палиндромом')
else:
  print("Это слово палиндром")


