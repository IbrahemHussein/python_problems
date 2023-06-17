def helpful_math():
    operation=input().split('+')
    t=''
    if len(operation)>1:
       num=[int(i) for i in operation]
       num.sort()
       for i in num: 
        t+=str(i)+'+'
       return t[:-1]
    else:
        return ''.join(operation)
if __name__ == "__main__":
    print(helpful_math())