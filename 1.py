class Car:
    def __init__(self, mark='', model='', color='', speed=0):
        self.mark = mark
        self.model = model
        self.color = color
        self.speed = speed
    def __del__(self):
        print('Сработал метод __del__')
my_car_1 = Car('Nissan', 'Juke', 'red', 0)
my_car_2 = Car()