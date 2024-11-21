# Base class Animal
class Animal:
    def sound(self):
        print("Animals make sound")


# Derived class Dog inherits from Animal
class Dog(Animal):
    def sound(self):
        print("Dog barks")


# Derived class Cat inherits from Animal
class Cat(Animal):
    def sound(self):
        print("Cat meows")


# Example usage
dog = Dog()
dog.sound()  

cat = Cat()
cat.sound() 
