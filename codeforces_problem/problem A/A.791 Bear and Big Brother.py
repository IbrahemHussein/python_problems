def who_bigger():
    ages=input().split()
    a=int(ages[0])
    b=int(ages[1])
    year=0
    while a<=b:
        year+=1
        a*=3
        b*=2
    print(year)
if __name__ == '__main__':
    who_bigger()
