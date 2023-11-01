from pprint import pprint
class Car:
    def __init__(self,mark = 'Toyota',model = 'Corolla',color = 'white',speed = 0):
        self.mark = mark
        self.model = model
        self.color = color
        self.speed = speed

    def set_power_engine(self, power):
        self.power_engine = power
    def get_params(self):
        return (self.mark, self.model, self.color, self.speed)
    def show_info(self):
        print(f'Марка: {self.mark}')
        print(f'Модель: {self.model}')
        print(f'Цвет: {self.color}')
        print(f'Скорость: {self.speed}')
    def __del__(self):
        print('Сработал метод __del__')
my_car1 = Car('УАЗ', 'Буханка', 'white', 60)
my_car2 = Car()
# my_car2.model = "Tundra"
# my_car2.set_power_engine(100)
# my_car1.set_power_engine(200)
# print(my_car2.__dict__)
print(my_car1.get_params())
print(my_car2.get_params())
# pprint(Car.__dict__)
# my_car1.show_info()
# my_car2.show_info()
# print(my_car1.get_params())