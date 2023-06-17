def watermelon():
    n = int(input())
    if n > 2:
        if n % 2 == 0:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
    return


if __name__ == '__main__':
    watermelon()
