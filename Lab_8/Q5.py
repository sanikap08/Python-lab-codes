'''Implement the linear search algorithm using python'''

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
target = 25
result = linear_search(arr, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")



# Name : Sanika Patil
# Section K
# 23FE10CSE00445