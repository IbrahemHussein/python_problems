def next_round(n,k):
    """the function take a list and k to check the number of user  who advance to the next round.

    Args:
        n (int): number of items of the list
        k (int): the number we used to check
    returns:
        the number of user who advance to the next round
    """
     
    
    num_list=[]
    num=input().split()
    
    if len(num)== n:
        for i in num:
            num_list.append(int(i))
    else:
        print('out of range k ')
    total=0
    for i in num_list:
        if i >= num_list[k-1] and i >0:
            total+=1
    print(total)
    return

    
if __name__=='__main__':
    n_k=input().split()
    next_round(n=int(n_k[0]),k=int(n_k[1]))
    
    
