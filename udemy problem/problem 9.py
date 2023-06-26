# Todo:Write A Python Program To Get Number From The User, And Display Table For That Number.
number = int(input('enter the number fot table :'))
print(f'the table of number{number} is :')
print('=' * 30)
for i in range(1, 12):
    print(f'{i} x {number} = {i * number}')
# Todo:Assignment
# Write A Python Program To Get 2 Number From The User, And Display 2 Table For That Number.
numbers = []
for _ in range(2):
    numbers.append(int(input('enter the numbers fot table')))
for n in numbers:
    for i in range(1, 12):
        print(f'{i} x {n} = {i * n}')
