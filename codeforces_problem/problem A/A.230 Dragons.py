s,n=map(int,input().split(' '))
dragons=[]
for _ in range(n):
    x,y=map(int,input().split(' '))
    dragons.append((x,y))

dragons.sort()
for i in range(n):
    if s> dragons[i][0]:
         s+=dragons[i][1]
    else:
        print('NO')
        break
else:
    print('YES')