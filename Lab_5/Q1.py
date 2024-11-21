# Define the Person class
class Person:
    def __init__(self, name, age):
        """Constructor to initialize the name and age attributes."""
        self.name = name
        self.age = age

# Create two instances of the Person class
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

# Print their details
print(f"Name: {person1.name}, Age: {person1.age}")
print(f"Name: {person2.name}, Age: {person2.age}")
