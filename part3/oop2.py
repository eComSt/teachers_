class SportCar:
    mark = ''
    model = ''
    engine_power = 0
    max_speed = 0

cars = []
for _ in range(3):
    car = SportCar()
    car.mark = input('Введите марку:')
    car.model = input('Введите модель:')
    car.engine_power = int(input('Введите мощность двигателя:'))
    car.max_speed = int(input('Введите максимальную скорость:'))
    cars.append(car)
    print("_"*15)
for car in cars:
    print(f"Марка {car.mark}")
    print(f"Модель {car.model}")
    print(f"Мощность двигателя {car.engine_power}")
    print(f"Максимальная скорость {car.max_speed}")
    print("_"*15)
