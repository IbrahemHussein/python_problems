#Todo: Write a Python program to display following output using for loop
"""
        *
     *  *
    * * *
  * * * *
* * * * *

"""

for i in range (1,6):
    for j in range (1,6-i):
        print(" ",end=" ")

    for j in range (1,i+1):
        print('*',end=' ')
    print()