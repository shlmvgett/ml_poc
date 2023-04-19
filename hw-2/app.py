from car import Car
from plane import Plane
from engine import Engine
from exceptions import *


print('>>>>>>>>>>>> Car')
default_car = Car()
default_car.engine = Engine(10.0, 4)
print(default_car)

default_car.start()
default_car.start()

default_car.move(10)
try:
    default_car.move(100)
except NotEnoughFuel as e:
    print("NotEnoughFuel")


print('\n>>>>>>>>>>>> Plane')
plane = Plane(1000)
print(plane)

plane.load_cargo(10)
plane.load_cargo(10)

try:
    plane.load_cargo(10000)
except CargoOverload as e:
    print("CargoOverload")

plane.remove_all_cargo()
