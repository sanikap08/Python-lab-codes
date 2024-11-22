'''Implement the binary search using Python (Element should be sorted)'''

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# Example usage
arr = [11, 12, 22, 25, 34, 64, 90]  
target = 25
result = binary_search(arr, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")




# Name : Sanika Patil
# Section K
# 23FE10CSE00445