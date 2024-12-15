class Vheicle:
    owner = []

    __COLOR_VARIANS = ['Красный','Черный','Зеленый','Белый','Синий']

    def __init__(self, owner, model, color, engine_power):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        return (f'Модель: {self.__model}')

    def get_horsepower(self):
        return (f'Мощность двиигателя: {self.__engine_power}')

    def get_color(self):
        return (f'Цвет машины: {self.__color}')

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
        stra = ''.join(self.__COLOR_VARIANS)
        if new_color.lower() in stra.lower():
            self.__color = new_color
            return self.__color
        else:
            print(f'Цвет нельзя изменить на {new_color}')
#
class Sedan(Vheicle):
    __PASSENGERS_LIMIT = 5

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

vehicle1.print_info()

vehicle1.set_color('Розовый')

vehicle1.set_color('Черный')

vehicle1.owner = 'Vasyok'

vehicle1.print_info()
