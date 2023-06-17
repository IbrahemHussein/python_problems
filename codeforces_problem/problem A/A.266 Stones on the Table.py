def stones():
    num=int(input())
    string=input()
    total=0
    for i in range (num-1):
        if string[i]==string[i+1]:
            total+=1
    print(total)
if __name__=='__main__':
    stones()