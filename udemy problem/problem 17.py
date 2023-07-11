# Todo: Write a Python program to show a message in this format using print function.
"""
A
B C
D E F
G H I J
K L M N
O P Q R S
T U V W X Y
"""
import string

alphapt = string.ascii_uppercase
print(alphapt)
n = 1
start = 0
end = 1
while n < 8:
    print(alphapt[start:end])
    start = end
    n += 1
    end += n
