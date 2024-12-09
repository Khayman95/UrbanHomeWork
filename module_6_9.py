from random import randint


class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self._cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        self.dx = dx
        self.dy = dy
        self.dz = dz
        if dz <= 0:
            self.x = dx
            self.y = dy
            self.z = 0
            print('Слишком глубоко, я не могу плавать')
            return self.x, self.y, self.z
        else:
            self.x = dx*self.speed
            self.y = dy*self.speed
            self.z = dz*self.speed
            return self.x, self.y, self.z

    def get_cords(self):
        print(f'X: {self.x}, Y: {self.y}, Z {self.z}')

    def attack(self):
        if self._DEGREE_OF_DANGER <= 5:
            print('Извините я мирный')
        else:
            print('Осторожно, я атакую')

    def speak(self):
        print(self.sound)

class Bird(Animal):
    beak = True
    def lay_eggs(self):
        print(f'Есть {randint(1, 4)} яиц для тебя')

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3
    def dive_in(self, dz):
        self.z = abs(self.z - dz*(self.speed/2))

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class DuckBill(Bird, PoisonousAnimal, AquaticAnimal, Animal):
    sound = 'Click-click-click'
    def __init__(self, speed):
        super().__init__(speed)



db = DuckBill(10)

print(db.live)

print(db.beak)

db.speak()

db.attack()

db.move(1, 2, 1)

db.get_cords()

db.dive_in(6)

db.get_cords()

db.lay_eggs()

