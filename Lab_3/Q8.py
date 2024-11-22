""""Pattern #8: Pyramid of Natural Numbers Less Than 10
Pattern:
1 
2 3 4 
5 6 7 8 9"""

num = 1
for i in range(1, 4):
    print(" ".join(str(num + x) for x in range(i)))
    num += i




# Name : Sanika Patil
# Section K
# 23FE10CSE00445
