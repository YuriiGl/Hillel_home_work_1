# 4. По данному натуральному `n ≤ 9` выведите лесенку из `n` ступенек, `i`-я ступенька состоит
# из чисел от 1 до `i` без пробелов.
#    1
#    12
#    123
#    1234
#    12345


n = range(1,9)
for i in n:
    i = [0]
    print(i, i + 1)


