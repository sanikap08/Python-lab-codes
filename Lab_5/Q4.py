# Define the Student class
class Student:
    def __init__(self, name, age):
        """Constructor to initialize the name and age attributes."""
        self.name = name
        self.age = age

# Create objects for different students
student1 = Student("Alice", 20)
student2 = Student("Bob", 22)

# Print details of students
print(f"Student 1 - Name: {student1.name}, Age: {student1.age}")
print(f"Student 2 - Name: {student2.name}, Age: {student2.age}")
