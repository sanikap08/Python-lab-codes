'''Create a class Animal with a method sound() that prints "Animals make sound". Then create 
two subclasses Dog and Cat, each with their own version of sound() method that prints "Dog 
barks" and "Cat meows" respectively. Demonstrate hierarchical inheritance by calling the 
sound() method from both Dog and Cat objects.'''


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




# Name : Sanika Patil
# Section K
# 23FE10CSE00445
