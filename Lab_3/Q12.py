""""Pattern #12: Even Number Pyramid Pattern
Pattern:
10 
10 8 
10 8 6 
10 8 6 4 
10 8 6 4 2"""

num = 10
for i in range(1, 6):
    print(" ".join(str(num - 2 * x) for x in range(i)))
    num -= 2




# Name : Sanika Patil
# Section K
# 23FE10CSE00445
