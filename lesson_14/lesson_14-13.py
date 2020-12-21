# Написать программу кофейный магазин.
# Обьекты:
#    Product
#    - свойства: наименование, тип, цена
#    - print обьекта продукта должен возвращать прим. "Кофе: Эспрессо, цена: 27грн."
#    Store
#    - может импортировать продукты из файла invertory.csv
#    (по-умолчанию по 5 шт. каждого наименования)
#    - может вернуть список продуктов нужного типа (tea, coffee или все продукты)
#    - может вернуть общую стоимость продуктов в наличии
#    - может продать продукт
# *доп. Научить Store запоминать выручку(сумма проданных продуктов) и выводить баланс.
# Тип продукта может быть только coffee или tea (нельзя создать обьект с другим типом).

import csv

product_list = 'inventory.csv'
with open(product_list) as f:
    reader = csv.reader(f)
    header_row = next(reader)
print(header_row)
class Product:

    def __init__(self, product_name, product_type, price):
        self.product_name = product_name
        self.product_type = self._check_product_type(product_type)
        self.price = float(price)

    def _check_product_type(self, product_type):
        if product_type == 'tea':
            return 'tea'
        elif product_type == 'coffee':
            return 'coffee'
        else:
            return None

    def print_product(self):
        if self.product_type is not None:
            print(self.product_type+':'+self.product_name+', цена: '+str(self.price) + 'грн')
        else:
            print('Странный продукт:' + self.product_name + ', цена: ' + str(self.price) + 'грн')


class Store:

    def __init__(self):
        self.ware_house = self.import_product()  # CSV
        self.transactions = []

    def import_product(self):
        product_list = [Product('Латте', 'coffee', 34),
                        Product('Черный чай', 'tea', 20),
                        Product('Earl Grey', 'tea', 25),
                        Product('Хлеб', 'bakery', 10)]
        return product_list

    def order(self):
        pass

    def balance_day(self):
        pass



# product_list = [Product('Латте','coffee',34),
#                 Product('Черный чай','tea',20),
#                 Product('Earl Grey','tea',25),
#                 Product('Хлеб','bakery',10)]

for product in product_list:
    product.print_product()