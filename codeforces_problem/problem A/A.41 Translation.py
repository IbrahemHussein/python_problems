def translation():
    string1 = input()
    string2 = input()
    if len(string1) == len(string2):
        if string1 == string2[::-1]:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')

if __name__ == '__main__':
    translation()
