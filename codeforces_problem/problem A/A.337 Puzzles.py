n,m=map(int,input().split(' '))
pazz=sorted(list(map(int,input().split(' '))))
min_diff=float('inf')
for i in range(n-1,m):
    diff=pazz[i]-pazz[i-n+1]
    if diff<min_diff:
        min_diff=diff
print(min_diff)
