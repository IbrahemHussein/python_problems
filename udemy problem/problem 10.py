#Todo:Write A Python Program to get 6 subject marks from the user and calculate total and average of that marks. And display to user.
from openpyxl.styles.builtins import total

markes=[int(input('enter the degree: ')) for _ in range(6)]
total_marks=sum(markes)
average_marks=total_marks/600
print("Total marks :",total_marks)
print("Average marks :",average_marks)

#Todo:Assignment
# Write A Python Program to get 6 subject marks from the user and calculate total and average of that marks. And display to user.
markes=[int(input('enter the degree: ')) for _ in range(6)]
total_marks=sum(markes)
average_marks=total_marks/600
percentage=average_marks*100
print("Total marks :",total_marks)
print("Average marks :",average_marks)
print("Percentage marks:",percentage)
