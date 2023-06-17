def Bitland ():
    """the function take an operation and return the final value of X
        the operator can be ++X in this case X increase 
        the operator can be --X in this case X decrease
    """
    iter=int(input())
    X=0
    text=[input() for i in range (iter)]
    for operator in text:
        if operator =='++X' or operator =='X++':
            X+=1
        elif operator =='--X' or operator =='X--':
            X-=1
    print(X)
    return 

if __name__=='__main__':
    Bitland()