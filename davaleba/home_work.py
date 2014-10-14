__author__ = 'guga'

class Drive:
    def __init__(self):
        self.__speed = 0

    def get_speed(self):
        return self.__speed

    def increase(self):
        if self.__speed == 110:
            print('You can\'t increase your speed, man')
        else:
            self.__speed += 10

    def decrease(self):
        if self.__speed == 0:
            print('You can\'t decrease your speed, man')
        else:
            self.__speed -= 10

car1 = Drive()
car1.increase()
car1.increase()
print(car1.get_speed())
