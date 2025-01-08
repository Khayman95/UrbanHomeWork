from pprint import pprint

class Product:

    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return str(f'{self.name}, {self.weight}, {self.category} \n')

class Shop:

    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        return (file.read())
        file.close()

    def add(self, *products):
        product_dict = {}
        with open(self.__file_name, 'r') as file:
            for line in file:
                name, weight, category = line.strip().split(", ")
                product_dict[(name, category)] = float(weight)

        for product in products:
            key = (product.name, product.category)
            if key in product_dict:
                product_dict[key] += product.weight
                print(f"Продукт {product.name} уже был в магазине, его общий вес теперь равен {product_dict[key]}")
            else:
                product_dict[key] = product.weight
                print(f"{product.name}, {product_dict[key]}, {product.category}")

        with open(self.__file_name, 'w') as file:
            for (name, category), weight in product_dict.items():
                file.write(f"{name}, {weight}, {category}\n")

s1 = Shop()

p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

s1.add(p1, p2, p3)

print(s1.get_products())