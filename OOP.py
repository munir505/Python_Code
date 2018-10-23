class Vehicle:
    def __init__(self, engine_type, wheels_amount):
        self.engine = engine_type
        self.wheels = wheels_amount

    def move_speed(self):
        if self.engine > 10:
            return 2
        elif self.engine < 10:
            return 1


class Car(Vehicle):
    def __init__(self, wheel_speed, car_name):
        Vehicle.__init__(self, 10, 4)
        self.speed = wheel_speed
        self.car_name = car_name

    def ground_speed(self):
        return self.speed * 10

    def get_name(self):
        return self.car_name


class Plane(Vehicle):
    def __init__(self, wings_speed):
        Vehicle.__init__(self, 20, 2)
        self.wings_speed = wings_speed

    def flight_speed(self):
        return self.wings_speed * 10


class Garage:
    def __init__(self, plane_amount, car_names, speed_list):
        self.plane_amount = plane_amount
        self.cars = car_names
        self.car_speeds = speed_list

    def create_car(self):
        counter = 0
        for car in self.cars:
            car_name = car
            car = Car(self.car_speeds[counter], car_name)
            print(car.get_name(), " ", car.ground_speed())
            counter = counter + 1


names = ["GTR", "Civic", "Golf", "F12", "McLaren-P1", "Polo"]
speeds = [23, 5, 12, 34, 12, 4]
gr1 = Garage(0, names, speeds)
gr1.create_car()
