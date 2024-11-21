# Define the Student class
class Student:
    def __init__(self, name, roll_no):
        """Constructor to initialize the name and roll number."""
        self.name = name
        self.roll_no = roll_no

# Create an object of the Student class
student = Student("John", 2)

# Print student details
print(f"Name: {student.name}, Roll No: {student.roll_no}")
