class House:
    def __init__(self, name, numbers_of_floors):
        self.name = name
        self.numbers_of_floors = numbers_of_floors

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

    def __eq__(self, other):
        return self.numbers_of_floors == other.numbers_of_floors

    def __lt__(self, other):
        return self.numbers_of_floors < other.numbers_of_floors

    def __le__(self, other):
        return self.numbers_of_floors <= other.numbers_of_floors

    def __gt__(self, other):
        return self.numbers_of_floors > other.numbers_of_floors

    def __ge__(self, other):
        return self.numbers_of_floors >= other.numbers_of_floors

    def __ne__(self, other):
        return self.numbers_of_floors != other.numbers_of_floors

    def __add__(self, value):
        self.numbers_of_floors = self.numbers_of_floors + value
        return self

    def __radd__(self, value):
        self.numbers_of_floors = value + self.numbers_of_floors
        return self


h1 = House('Колизей', 12)
h2 = House('Адмиралтейский', 3)

print(h1)
print(h2)
print(len(h1))
print(len(h2))

h1 = h1+10
print(h1)
print(h1 == h2)

h1 += 10
print(h1)

h2 = 29 + h2
print(h2)
print(h1 < h2)
print(h1 <= h2)
print(h1 > h2)
print(h1 >= h2)
print(h1 != h2)
