'''Create two classes Teacher and Author, each with their own description() method to describe
the profession. Then, create a subclass TutorAuthor that inherits from both Teacher and Author.
Use this subclass to call the description() method from each parent class. Use the super() 
function to resolve any conflicts if necessary.'''


# Base class Teacher
class Teacher:
    def description(self):
        print("I am a teacher.")


# Base class Author
class Author:
    def description(self):
        print("I am an author.")


# Subclass TutorAuthor inherits from both Teacher and Author
class TutorAuthor(Teacher, Author):
    def description(self):
        super().description()  # Use super to avoid conflict, call the method from both parent classes
        print("I am also a tutor-author.")


# Example usage
tutor_author = TutorAuthor()
tutor_author.description()  




# Name : Sanika Patil
# Section K
# 23FE10CSE00445