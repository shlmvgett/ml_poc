from vehicle import Vehicle
from engine import Engine


class Car(Vehicle):
    _engine: Engine

    @property
    def engine(self):
        return self._engine

    @engine.setter
    def engine(self, value):
        self._engine = value

    def __str__(self):
        return f'{self.weight}, started: {self.started}, fuel: {self.fuel}, fuel_consumption: {self.fuel_consumption}'
