def ceil(x):
    int_x=int(x)
    return int_x+1 if int_x < x else int_x
def theatre_square():
    numbers=input().split()
    n=int(numbers[0])
    m=int(numbers[1])
    a=int(numbers[2])
    square=ceil(n/a)*ceil(m/a)
    print(square)
    return
if __name__=='__main__':
    theatre_square()
