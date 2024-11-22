'''  Write a program to find the number of vowels in the string. '''

user_input = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = sum(1 for char in user_input if char in vowels)
print(f"Number of vowels: {count}")




# Name : Sanika Patil
# Section K
# 23FE10CSE00445
