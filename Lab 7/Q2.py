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
