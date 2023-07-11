#Todo: Write A Program To Get 6 Number In The TUPLE And Display All Number And Then Clear TUPLE And Then Display
my_list = []
for i in range (1,7):
    num= int(input(f'enter the number {i} :'))
    my_list.append(num)
print(tuple(my_list))

my_list.clear()
print(tuple(my_list))
