'''Create a class Vehicle with a method info() that prints "This is a vehicle". Inherit Car 
from Vehicle and add a method car_info() to print "This is a car". Further, create another 
subclass ElectricCar that inherits from Car and adds a method battery_info() to print "This 
car has a battery." Demonstrate how multilevel inheritance works by calling all methods from 
an ElectricCar object.'''


# Base class Vehicle
class Vehicle:
    def info(self):
        print("This is a vehicle")


# Derived class Car inherits from Vehicle
class Car(Vehicle):
    def car_info(self):
        print("This is a car")


# Further derived class ElectricCar inherits from Car
class ElectricCar(Car):
    def battery_info(self):
        print("This car has a battery.")


# Example usage
electric_car = ElectricCar()
electric_car.info()  # Inherited from Vehicle
electric_car.car_info()  # Inherited from Car
electric_car.battery_info()  # Defined in ElectricCar




# Name : Sanika Patil
# Section K
# 23FE10CSE00445