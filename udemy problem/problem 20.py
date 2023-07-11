#todo :Write a Python Program to get 5 number from user in array,
# AND find maximum number.
import  array as arr

a=arr.array('i',[])

for _ in range(4):
    a.append(int(input('enter the number ')))

print('the max number is : ',max(a))
