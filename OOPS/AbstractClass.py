from abc import ABC, abstractmethod

class Vehicle(ABC): # Abstacct class
    @abstractmethod # Decorator
    def start():
        pass
    def checkFuel():
        pass

class Car(Vehicle):
    def start(self):
        print('Starting car...')

    def checkFuel(self):
        print("Checking fuel in car")

class Bike(Vehicle):
    def start(self):
        print('Starting bike...')

    def checkFuel(self):
        print("Checking fuel in bike")