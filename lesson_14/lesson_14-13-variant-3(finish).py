import csv


class Product:
    def __init__(self, product_name, product_type, price):
        self.product_name = product_name
        self.product_type = self._check_product_type(product_type)
        self.price = float(price)

    def __eq__(self, other):
        return self.product_name == other.product_name and self.product_type == other.product_type and self.price == other.price

    def _check_product_type(self, product_type):
        if product_type == 'tea':
            return 'tea'
        elif product_type == 'coffee':
            return 'coffee'
        else:
            return None

    def print_product(self):
        if self.product_type is not None:
            print(self.product_type + ': ' + self.product_name + ', цена: ' + str(self.price) + 'грн')
        else:
            print('Странный продукт: ' + self.product_name + ', цена: ' + str(self.price) + 'грн')

class Store:
    def __init__(self):
        self.ware_house = []
        self.transactions = []

    def add_product(self, row, count):
        product = Product(row['Наименование'], row['Тип'], row['Цена'])
        self.ware_house.extend([product] * count)

    def inventory(self):
        with open('invertory.csv', 'r') as inventory:
            reader = csv.DictReader(inventory)
            for row in reader:
                self.add_product(row, 5)

    def print_all_products(self):
        for p in self.ware_house:
            p.print_product()

    def get_products_by_type(self, product_type):
        filtered_products = []
        if product_type == "все продукты":
            return self.ware_house

        for p in self.ware_house:
            if p.product_type == product_type:
                filtered_products.append(p)
        return filtered_products

    def total_cost(self):
        cost = 0
        for p in self.ware_house:
            cost += p.price
        return cost

    def sell(self, product):
        if product in self.ware_house:
            self.ware_house.remove(product)
            self.transactions.append(product)
        else:
            print("Невозможно продать продукт")

    def total_selled(self):
        total_selled = 0
        for t in self.transactions:
            total_selled += t.price
        return total_selled

    def add_new_product(self, product):
        self.ware_house.append(product)


my_store = Store()

my_store.inventory()
my_store.print_all_products()

coffee = my_store.get_products_by_type('coffee')
print("Only coffee: \n")
print("len: " + str(len(coffee)))
for p in coffee:
    p.print_product()

p1 = Product("Латте 1", "coffee", 60.0)
my_store.add_new_product(Product("Латте 1", "coffee", 60.0))
my_store.print_all_products()

c = my_store.total_cost()
print("total cost: ", c)

my_store.sell(p1)
my_store.sell(Product("Зеленый чай с жасмином", "tea", 28.0))

c2 = my_store.total_cost()
print("total cost: ", c2)

selled = my_store.total_selled()
print("selled: ", selled)

my_store.print_all_products()