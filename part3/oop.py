class Car:
    mark = 'Toyota'
    model = 'Corolla'
    color = 'white'
    speed = 0

my_car1 = Car()
# print(my_car1)
# print(type(my_car1))
print(my_car1.color)
# print(my_car1.model)
my_car1.color = 'black'
print(my_car1.color)
my_car2 = Car()
my_car2.model = "Tundra"
print(my_car2.color)
print(my_car2.model)
print(my_car1.model)