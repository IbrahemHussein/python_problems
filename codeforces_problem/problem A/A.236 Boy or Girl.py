def boy_or_girl():
    user_name=set(input().lower())
    return 'CHAT WITH HER!' if len(user_name)%2 == 0 else 'IGNORE HIM!'

if __name__=='__main__':
    print(boy_or_girl()) 