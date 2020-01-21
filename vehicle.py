class Vehicle:

    def __init__(self, color, engine_type, horsepower, max_mph):
        self.color = color
        self.engine_type = engine_type
        self.horsepower = horsepower
        self.max_mph = max_mph

    def drive(self):
        print('vroooom')

    def turn(self, direction):
        print(f'The vehicle turned {direction}')

    def stop(self):
        print('The vehicle has stopped.')

    def __repr__(self):
        return 'cool vehicle'

class Rocket(Vehicle):

    def __init__(self, color, engine_type, horsepower, max_mph):
        super().__init__(color, engine_type, horsepower, max_mph)

    def drive(self):
        print(f'The {self.color} {self} blasted off into space!')

    def turn(self, direction):
        print(f'The {self} adjusted trajectory banking slightly to the {direction}.')

    def stop(self):
        print(f'The {self} re-entered the atmosphere and splashed down in the Indian Ocean.')

    def __repr__(self):
        return "rocket"
class Scooter(Vehicle):

    def __init__(self, color, engine_type, horsepower, max_mph):
        super().__init__(color, engine_type, horsepower, max_mph)

    def drive(self):
        print(f'The {self.color} {self} is scooting down the avenue!')

    def turn(self, direction):
        print(f'The {self.color} {self} made a fun little {direction} turn.')

    def stop(self):
        print(f'The {self} stopped and everyone stopped to stare!')

    def __repr__(self):
        return "scooter"

class ElectricCar(Vehicle):

    def __init__(self, color, engine_type, horsepower, max_mph):
        super().__init__(color, engine_type, horsepower, max_mph)

    def drive(self):
        print(f'The {self.color} {self} is silently moving!')

    def turn(self, direction):
        print(f'The {self} silently turned {direction}.')

    def stop(self):
        print(f'The {self} stopped and nobody heard it...')

    def __repr__(self):
        return "electric car"

class AllTerrainVehicle(Vehicle):

    def __init__(self, color, engine_type, horsepower, max_mph):
        super().__init__(color, engine_type, horsepower, max_mph)

    def drive(self):
        print(f'The {self.color} {self} is goin mudding!')

    def turn(self, direction):
        print(f'The {self} rocked that {direction} turn!')

    def stop(self):
        print(f'The {self} stopped and flung mud everywhere!')

    def __repr__(self):
        return "ATV"

class BulletTrain(Vehicle):

    def __init__(self, color, engine_type, horsepower, max_mph):
        super().__init__(color, engine_type, horsepower, max_mph)

    def drive(self):
        print(f'The {self.color} {self} is floating down the tracks!')

    def turn(self, direction):
        print(f"The {self} came to a fork in the track and went {direction}.")

    def stop(self):
        print(f'The {self} slowed to a stop with the help of MAGNETS!')

    def __repr__(self):
        return "bullet train"