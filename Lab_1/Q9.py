"""WAP to check if a number is a prime or not"""
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

number = int(input("Enter a number: "))
if is_prime(number):
    print(f"{number} is a Prime Number")
else:
    print(f"{number} is not a Prime Number")




# Name : Sanika Patil
# Section K
# 23FE10CSE00445