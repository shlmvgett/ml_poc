from vehicle import Vehicle
from exceptions import CargoOverload


class Plane(Vehicle):
    cargo = 0.0
    max_cargo: float

    def __init__(self, max_cargo):
        super().__init__()
        self.max_cargo = max_cargo

    def load_cargo(self, cargo):
        if self.cargo + cargo <= self.max_cargo:
            self.cargo += cargo
            print(f"Current cargo: {self.cargo}")
        else:
            raise CargoOverload

    def remove_all_cargo(self):
        temp_cargo = self.cargo
        self.cargo = 0
        print(f"Cargo was reset: {self.cargo}")
        return temp_cargo

    def __str__(self):
        return f'{self.weight}, ' \
               f'started: {self.started}, ' \
               f'fuel: {self.fuel}, ' \
               f'fuel_consumption: {self.fuel_consumption}, ' \
               f'max_cargo: {self.max_cargo}, ' \
               f'cargo: {self.cargo}'
