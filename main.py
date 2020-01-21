from vehicle import AllTerrainVehicle, Scooter, Rocket, BulletTrain, ElectricCar

gator = AllTerrainVehicle("black", "2 stroke", 27, 60)
gator.drive()
gator.turn("left")
gator.stop()

saturn_v = Rocket("black and white", "Rocketdyne F-1", 160000000, 6164)
saturn_v.drive()
saturn_v.turn("left")
saturn_v.stop()

vespa = Scooter("yellow", "2-stroke", 26, 45)
vespa.drive()
vespa.turn("right")
vespa.stop()

maglev = BulletTrain("silver", "electric coils", 188, 270)
maglev.drive()
maglev.turn("left")
maglev.stop()

leaf = ElectricCar("white", "electric motor", 110, 93)
leaf.drive()
leaf.turn("right")
leaf.stop()