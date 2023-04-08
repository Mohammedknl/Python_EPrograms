from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car started")
    def stop(self):
        print("Car stopped")

class Bike(Vehicle):
    def start(self):
        print("Bike started")
    def stop(self):
        print("Bike stopped")
car = Car()
car.start()  # prints "Car started"
car.stop()  # prints "Car stopped"
bike = Bike()
bike.start()  # prints "Bike started"
bike.stop()  # prints "Bike stopped"

'''
So in the example I provided,
we're using abc and ABC to define an abstract base class called Shape and Vehicle, respectively, 
and we're using abstractmethod to define the abstract methods area, perimeter, start, and stop.
'''