n = int(input())
l = [4, 7, 47, 74, 777, 774, 747, 744, 444, 477, 474, 477]
for i in l:
    if n % i == 0:
        print('YES')
        break
    else:
        continue
else:
    print('NO')
