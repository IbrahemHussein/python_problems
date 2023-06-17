def banana_price():
    nums=input().split()
    k=int( nums[0])
    n=int(nums[1])
    w=int(nums[2])
    total=0
    for i in range(w+1):
        total+=i*k
    if total > n:
        return total- n
    else:
        return 0
    
if __name__=='__main__':
    print(banana_price())