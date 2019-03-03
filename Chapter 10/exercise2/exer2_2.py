import exer2

Car = exer2.Car('2009','Hyundai')
for x in range(5):
    Car.accelerate()
    print('Current speed is', Car.get_speed())
for y in range(5):
    Car.brake()
    print('Current speed is', Car.get_speed())