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
