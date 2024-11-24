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

h1 = House('Колизей', 12)
h2 = House('Адмиралтейский', 3)
h1.go_to(6)
h2.go_to(5)