def who_win():
    num = int(input())
    string = input().lower()
    if len(string)==num:
        if string.count('a') > string.count('d'):
            print('Anton')
        elif string.count('a') < string.count('d'):
            print('Danik')
        else:
            print('Friendship')
    else:
        print('invalid string')


if __name__ == '__main__':
    who_win()
