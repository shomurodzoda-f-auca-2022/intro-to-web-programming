from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def startEngine(self):
        pass

class Car(Vehicle):
    def startEngine(self):
        print("Car is starting...")

class Motorcycle(Vehicle):
    def startEngine(self):
        print("Motorcycle is starting...")

car = Car()
motorcycle = Motorcycle()

car.startEngine()
motorcycle.startEngine()