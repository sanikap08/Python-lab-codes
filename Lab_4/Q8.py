user_input = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = sum(1 for char in user_input if char in vowels)
print(f"Number of vowels: {count}")
