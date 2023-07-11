n=int(input())
home_list=[]
away_list=[]
count=0
for _ in range(n):
    home,away=map(int,input().split(' '))
    home_list.append(home)
    away_list.append(away)
for i in home_list:
    count+=away_list.count(i)
print(count)