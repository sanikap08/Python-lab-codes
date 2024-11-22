'''Create a class ComplexNumber that represents a complex number with real and imaginary parts 
and contain following methods: 
1. A constructor to initialize the complex number. 
2. add(ComplexNumber c): Returns a new ComplexNumber that is the sum of the current object and 
another complex number. 
3. magnitude(): Returns the magnitude of the complex number. Write a java program to create 
two ComplexNumber objects, perform operation, and print the results along with their magnitudes.'''



import math

# Define the ComplexNumber class
class ComplexNumber:
    def __init__(self, real, imag):
        """Constructor to initialize the complex number with real and imaginary parts."""
        self.real = real
        self.imag = imag

    def add(self, c):
        """Add the current complex number to another complex number."""
        new_real = self.real + c.real
        new_imag = self.imag + c.imag
        return ComplexNumber(new_real, new_imag)

    def magnitude(self):
        """Return the magnitude (modulus) of the complex number."""
        return math.sqrt(self.real**2 + self.imag**2)

    def __str__(self):
        """Return a string representation of the complex number."""
        return f"{self.real} + {self.imag}i"

# Example usage
if __name__ == "__main__":
    # Create two complex numbers
    c1 = ComplexNumber(3, 4)  # 3 + 4i
    c2 = ComplexNumber(1, 2)  # 1 + 2i

    # Perform addition of the two complex numbers
    c3 = c1.add(c2)
    
    # Display the result of addition
    print(f"Sum of {c1} and {c2} is: {c3}")

    # Print the magnitudes of the complex numbers
    print(f"Magnitude of {c1}: {c1.magnitude()}")
    print(f"Magnitude of {c2}: {c2.magnitude()}")
    print(f"Magnitude of {c3}: {c3.magnitude()}")





# Name : Sanika Patil
# Section K
# 23FE10CSE00445