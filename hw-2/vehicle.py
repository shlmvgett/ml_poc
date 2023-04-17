from exceptions import NotEnoughFuel


class Vehicle:

    def __init__(self, weight=1000.0, started=False, fuel=100.0, fuel_consumption=2.0):
        self.weight = float(weight)
        self.started = bool(started)
        self.fuel = float(fuel)
        self.fuel_consumption = float(fuel_consumption)

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
                print("Start successful")
            else:
                raise NotEnoughFuel()
        else:
            print("Vehicle is already started")

    def move(self, distance):
        required_fuel = distance * self.fuel_consumption
        if required_fuel <= self.fuel:
            self.fuel -= required_fuel
            print(f"Move successful: {self.fuel}")
        else:
            raise NotEnoughFuel()
