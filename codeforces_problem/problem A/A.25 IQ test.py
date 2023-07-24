num=int(input())
numbers=list(map(int,input().split(' ')))

odd_count=0
event_count=0

odd_index=-1
event_index=-1

for number in range(num):
    if numbers[number]%2==0:
        event_count+=1
        event_index=number
    else:
        odd_count+=1
        odd_index=number


if event_count>odd_count:
    print(odd_index+1)
else:
    print(event_index+1)
