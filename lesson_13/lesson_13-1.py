# Написать программу Город.
# Создать три отдельных объекта: City, Street, House.
# У города должны быть улицы (City -> [Street]), у улиц должны быть дома Street -> [House].
# У города есть улицы и дома и возможности их добавлять и удалять.
#    Улицы могут вместить случайное количество домов от 5 до 20.
#    Дома могут иметь случайное количество населения от 1 до 100.
#    Должна быть возможность наполнить город одним методом.
#    У города должен быть метод который вернет количество населения.
#    *доп. Написать метод который сможет напечатать таблицей:
# Улица Дом Население
#    1   1         5
#    1   2         10
#    1   3         25
#                 и т.д.


from random import randint

class House:
    def __init__(self):
        self.population = randint(1,100)

    def print_house(self):
        print('population: ', self.population)

class Street:
    def __init__(self):
        self.houses = []
        for i in range(randint(5, 20)):
 #           self.houses.append(House())
            self.houses.append((i, House()))

    def print_street(self):
        for house in self.houses:
            print('house#: ', house[0])
            house[1].print_house()


class City:
    def __init__(self, name):
        self.name = name
        self.streets = []
        for i in range(randint(1, 5)):
            self.streets.append((i, Street()))

    def print_city(self):
        print(self.name)
        for street in self.streets:
            print('street#:', street[0])
            street[1].print_street()


my_city = City('Мухосранск')
my_city.print_city()