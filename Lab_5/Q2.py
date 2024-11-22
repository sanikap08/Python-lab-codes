'''Create a class named 'Student' with String variable 'name' and integer variable 'roll_no'. 
Assign the value of roll no as '2' and that of name as "John" by creating an object of the 
class Student. '''


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





# Name : Sanika Patil
# Section K
# 23FE10CSE00445