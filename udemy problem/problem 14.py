my_list=[]
for i in range(1,7):
    num=int(input('enter the number '))
    my_list.append(num)
my_tuple=tuple(my_list)

print('the sum of tuple is :',sum(my_tuple))