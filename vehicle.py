class Vehicle:

    def __init__(self, engine_type, horsepower, max_mph):
        self.engine_type = engine_type
        self.horsepower = horsepower
        self.max_mph = max_mph

    def drive(self):
        print('vroooom')

    def __repr__(self):
        return 'cool vehicle'

class Rocket(Vehicle):

    def __init__(self):
        pass

class Scooter(Vehicle):

    def __init__(self):
        pass

class ElectricCar(Vehicle):

    def __init__(self):
        pass

class AllTerrainVehicle(Vehicle):

    def __init__(self, engine_type, horsepower, max_mph):
        super().__init__(engine_type, horsepower, max_mph)
        pass

class BulletTrain(Vehicle):

    def __init__(self):
        pass