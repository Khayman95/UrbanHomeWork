class Vheicle:
    owner = []
    __model = []
    __engine_power = []
    __color = []
    __COLOR_VARIANS = ['Красный','Черный','Зеленый','Белый','Синий']

    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

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
        if new_color in self.__COLOR_VARIANS:
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
