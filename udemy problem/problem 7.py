# Todo:Write a Python Program to calculate intersection of two set
# A = {3,2,4,5,6,7,8} B = {4,12,5,1,6,8}

# Algorithm
# Step1: Get Set A
a = {3, 2, 4, 5, 6, 8}

# Step2: Get Set B
b = {4, 12, 5, 1, 6, 8}

# Step3: Get all the element from both set, don’t repeat
z = a.intersection(b)
print('the intersection of two set', z)

############################
# Assignment

# Todo:Write A Python Program To intersection  Of Three Set
# A = {5,2,4,6,7,1} B = {5,3,11}, C = {4,5,12,2,1,0}
A = {5, 2, 4, 6, 7, 1}
B = {5, 3, 11}
C = {4, 5, 12, 2, 1, 0}
z = A.intersection(B, C)
print('the intersection of three set', z)
