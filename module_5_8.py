class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.numbers_of_floors = number_of_floors

    def go_to(self,new_floor):
        if new_floor<1 or new_floor>self.numbers_of_floors:
            print('Такого этажа не существует')
        else:
            for i in range(1,new_floor):
                print(i)

    def __len__(self):
        return self.numbers_of_floors

    def __str__(self):
        return (f'Название: {self.name}, кол-во этажей: {self.numbers_of_floors}')

h1 = House('Колизей', 12)
h2 = House('Адмиралтейский', 3)
print(h1)
print(h2)
print(len(h1))
print(len(h2))
