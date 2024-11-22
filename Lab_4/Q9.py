''' Write a program to check if every word in a string begins with a capital letters or not.'''


user_input = input("Enter a string: ")
words = user_input.split()
if all(word[0].isupper() for word in words):
    print("Every word starts with a capital letter.")
else:
    print("Not every word starts with a capital letter.")




# Name : Sanika Patil
# Section K
# 23FE10CSE00445