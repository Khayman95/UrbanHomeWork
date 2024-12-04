class House:

    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, numbers_of_floors):
        self.name = name
        self.numbers_of_floors = numbers_of_floors

    def __del__(self):
        print(f'{self.name} снесён, но останется в истории')

h1 = House('Колизей', 12)
print(House.houses_history)
h2 = House('Адмиралтейский', 3)
print(House.houses_history)
h3 = House('Авторский', 5)
print(House.houses_history)

del h2

del h3
print(House.houses_history)