def new_text(fake_string, old_word, new_word, rep_num):
    new_string = fake_string.replace(old_word, new_word, rep_num)
    return new_string

fake_string = 'DS makes good movies, DS makes good comics'
rep_num = int(input('Введите колличество замен (1 или 2): '))
print(new_text(fake_string, 'DS', 'Marvel', rep_num))