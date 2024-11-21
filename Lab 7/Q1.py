# Base class Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age) 
        self.student_id = student_id

    def show_details(self):
        self.display()  
        print(f"Student ID: {self.student_id}")


# Example usage
student = Student("Alice", 20, "S12345")
student.show_details()
